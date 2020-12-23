import click
from typing import List

from .classes import NetrcStore
from .decorators import pass_netrcstore_obj
from .defaults import MODULE_KEY


@click.group("config")
def config_group():
    """
    Set or view config variables
    """
    pass


@config_group.command("get")
@click.option("-m", "--default-mapping", is_flag=True, default=False, show_default=True)
@pass_netrcstore_obj
def _config_get(store: NetrcStore, default_mapping: bool):
    """
    Echo config variables
    """
    if default_mapping:
        host_dict = store.host
    else:
        host_dict = store.host_with_mapping
    click.echo(host_dict)


class _ConfigSetter(click.Command):
    """
    To lazy load :class:`click.Context` via :meth:`click.get_current_context`
    and make options programatically.
    """

    def get_params(self, ctx):
        def _make_config_options() -> List[click.Option]:
            opts: List[click.Option] = []
            ctx = click.get_current_context()
            store: NetrcStore = ctx.meta.get(MODULE_KEY, None)
            if not store:
                raise RuntimeError("No NetrcStore object found.")
            flags = set()
            for k, v in store.mapping.items():
                f = "-{}".format(v[0])
                if f in flags:
                    f += v[1]
                flags.add(f)
                opt = click.Option(
                    (f, "--{}".format(v), k),
                    required=False,
                    help="Set {}".format(v),
                )
                opts.append(opt)
            return opts

        rv = super().get_params(ctx)
        extra_opts = _make_config_options()
        return rv + extra_opts


@config_group.command("set", cls=_ConfigSetter)
@pass_netrcstore_obj
def _config_set(store: NetrcStore, login, password, account):
    """
    Update config variables
    """
    host = store.host.copy()
    if login:
        host["login"] = login
    if password:
        host["password"] = password
    if account:
        host["account"] = account
    # finally save
    store.save(host)
    click.echo("Successfully saved config variables!")
