from abc import ABC, abstractmethod
from typing import Optional


class Target(ABC):
    # abstract target interface, to be used by a concrete implementation and proxy
    _auth: Optional[str] = None

    @abstractmethod
    def request(self) -> str:
        raise NotImplementedError


class ConcreteTarget(Target):
    # concrete implementation of service
    def request(self) -> str:
        return self.__class__.__name__


class UnauthenticateRequestError(Exception):
    # example exception
    pass


class Proxy(Target):
    # proxy used to validate authentication and access to underlying target service
    def __init__(self, target: Target) -> None:
        self.__target = target

    def request(self) -> str:
        if self.check_access():
            return self.__target.request()
        else:
            raise UnauthenticateRequestError(f"Not authenticated to request from {self.__target.__class__.__name__} as user {self.__user}")

    def check_access(self) -> bool:
        # example form of checking access
        if self.__target._auth is None:
            self.__target._auth = self.__user
        return self.__target._auth == self.__user

    def set_auth(self, user: str) -> None:
        self.__user = user


if __name__ == "__main__":
    # creating proxy interface and setting target auth
    proxy = Proxy(ConcreteTarget())
    proxy.set_auth("bob")
    print(proxy.request())

    # changing auth of proxy does not change auth of underlying target,
    # proxy will then not allow new user to access target
    proxy.set_auth("ross")
    try:
        # this should raise exception
        proxy.request()
    except UnauthenticateRequestError as e:
        print(e)
