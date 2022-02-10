from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    # abstract Handler that defines handler operations
    # typically it would be best to identify how the handling occurs
    # i.e. run handle_next before current handler
    # or do not handle next if current handler conditions met, etc.
    _next_handler: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle_next(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        raise NotImplementedError


class CoolConcreteHandler(Handler):
    # example ConcreteHandler
    attribute: str = "cool"

    def handle(self, request: str) -> Optional[str]:
        if self.attribute in request:
            print(f"{self.__class__.__name__} is {self.attribute}")
        self.handle_next(request)


class BobConcreteHandler(Handler):
    # example ConcreteHandler
    attribute: str = "bob"

    def handle(self, request: str) -> Optional[str]:
        if self.attribute in request:
            print(f"{self.__class__.__name__} is {self.attribute}")
        self.handle_next(request)


class RossConcreteHandler(Handler):
    # example ConcreteHandler
    attribute: str = "ross"

    def handle(self, request: str) -> Optional[str]:
        if self.attribute in request:
            print(f"{self.__class__.__name__} is {self.attribute}")
        self.handle_next(request)


if __name__ == "__main__":
    cool = CoolConcreteHandler()
    bob = BobConcreteHandler()
    ross = RossConcreteHandler()

    # creating chain of responsibility
    cool.set_next(bob).set_next(ross)

    print("\nFully Handling 'bob ross is cool': ")
    cool.handle("bob ross is cool")

    # should be able to call any object in chain
    print("\nPartially Handling 'bob ross is cool': ")
    bob.handle("bob ross is cool")

    print("\nFully Handling 'bob ross is lame' : ")
    cool.handle("bob ross is lame")
