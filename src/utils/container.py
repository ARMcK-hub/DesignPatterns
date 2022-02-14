from typing import Any, Dict

from .singleton import Singleton


class Container(metaclass=Singleton):
    """
    Example DI Container to be used for IoC & DI examples.
    Represented as a Singleton so that it can only be instantiated once.
    """

    _services: Dict[type, Any] = {}

    def register_service(self, service_type: type, registered_service: Any) -> None:
        self._services[service_type] = registered_service

    def get_service(self, service_type: type) -> None:
        return self._services[service_type]
