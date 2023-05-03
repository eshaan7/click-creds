#!/usr/bin/env python3
import click

import click_creds


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click_creds.use_netrcstore(
    name="myawesomeapp",
    mapping={"login": "username", "password": "api_key", "account": "url"},
)
@click.pass_context
def cli(ctx: click.Context):
    netrc = click_creds.get_netrc_object_from_ctx(ctx)
    uname = netrc.host_with_mapping["username"]
    _ = "Hello {}!\n".format(uname)


@click_creds.config_group.command("echo", help="echo the config params")
@click_creds.pass_netrcstore_obj
def run_cmd(store: click_creds.NetrcStore):
    host = store.host_with_mapping
    click.echo(host)


# Register "config" group
cli.add_command(click_creds.config_group)

# Register example command
cli.add_command(run_cmd)

# Entrypoint/executor
if __name__ == "__main__":
    cli()
