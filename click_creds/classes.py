import pathlib
from tinynetrc import Netrc as _TinyNetrc

from .defaults import DEFAULT_MAPPING
from .utils import ThreadSafeSingleton


class ClickCreds(metaclass=ThreadSafeSingleton):
    pass


class NetrcStore(ClickCreds):
    """
    A tiny wrapper class over the :class:`tinynetrc.Netrc` class.
    """

    __name: str
    __mapping: dict

    def __init__(self, name: str, mapping: dict = DEFAULT_MAPPING):
        """Create a NetrcStore instance.

        Args:
            name (str):
                host name
            mapping (dict, optional):
                custom mapping for the netrc's host dictionary.
                Defaults to DEFAULT_MAPPING.
        """
        self.__name = name
        self.__mapping = mapping

    @property
    def mapping(self) -> dict:
        """
        Current host mapping as a dictionary.
        """
        return self.__mapping

    @property
    def __netrc_obj(self) -> _TinyNetrc:
        if not hasattr(self, "__internal_netrc_obj"):
            filepath = pathlib.Path().home().joinpath(".netrc")
            filepath.touch(exist_ok=True)
            self.__internal_netrc_obj = _TinyNetrc(str(filepath))

        return self.__internal_netrc_obj

    @property
    def host_with_mapping(self) -> dict:
        host_dict = self.host
        return {self.mapping[k]: v for k, v in host_dict.items()}

    @property
    def host(self) -> dict:
        host_dict = self.__netrc_obj[self.__name]
        return host_dict

    def save(self, host: dict) -> None:
        obj = self.__netrc_obj
        obj[self.__name] = host
        obj.save()
