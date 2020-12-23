import click
from functools import update_wrapper

from .classes import NetrcStore
from .defaults import DEFAULT_MAPPING, MODULE_KEY


def use_netrcstore(name, mapping=DEFAULT_MAPPING):
    """Sets :attr:`click.Context.obj` to a :class:`NetrcStore` instance."""

    def decorator(f):
        @click.pass_context
        def new_func(ctx: click.Context, *args, **kwargs):
            ctx.meta[MODULE_KEY] = NetrcStore(name, mapping=mapping)
            return ctx.invoke(f, *args, **kwargs)

        return update_wrapper(new_func, f)

    return decorator


def pass_netrcstore_obj(f):
    """Similar to :func:`click.pass_obj`,
    this passes the current :class:`NetrcStore` instance as the first argument.
    """

    @click.pass_context
    def new_func(ctx, *args, **kwargs):
        netrc_obj = ctx.meta[MODULE_KEY]
        return ctx.invoke(f, netrc_obj, *args, **kwargs)

    return update_wrapper(new_func, f)
