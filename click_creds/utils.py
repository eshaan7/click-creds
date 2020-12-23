import threading
import click

from .defaults import MODULE_KEY


class ThreadSafeSingleton(type):
    _instances = {}
    _singleton_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # double-checked locking pattern
        # (https://en.wikipedia.org/wiki/Double-checked_locking)
        name = args[0]
        if name not in cls._instances.keys():
            with cls._singleton_lock:
                if name not in cls._instances.keys():
                    cls._instances[name] = super(ThreadSafeSingleton, cls).__call__(
                        *args, **kwargs
                    )
        return cls._instances[name]


def get_netrc_object_from_ctx(ctx: click.Context):
    return ctx.meta[MODULE_KEY]


'''
from typing import List, Callable
def apply_decorators_from_func(decorators_func):
    """
    A decorator which takes
    function which returns list of callables
    which are applied as decorators.
    """

    def wrapper(f):
        decorators: List[Callable] = decorators_func()
        for deco in reversed(decorators):
            f = deco(f)
        return f

    return wrapper


def apply_decorators(decorators: List[Callable]):
    """
    A decorator which takes list of callables
    which are applied as decorators.
    """

    def wrapper(f):
        for deco in reversed(decorators):
            f = deco(f)
        return f

    return wrapper
'''
