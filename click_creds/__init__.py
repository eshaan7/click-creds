# flake8: noqa
"""
    click_creds
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    click-creds
    :copyright: (c) 2020 by Eshaan Bansal.
    :license: BSD, see LICENSE for more details.
"""

from .classes import NetrcStore
from .decorators import use_netrcstore, pass_netrcstore_obj
from .groups import config_group
from .utils import get_netrc_object_from_ctx
