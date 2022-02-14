from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class StateNotSetError(Exception):
    # sample exception to raise when calling a
    # Context without underlying State set
    pass


class State(ABC):
    # abstract interface for States
    _context: Context


class Context(ABC):
    # abstract context manager
    _state: Optional[State] = None

    @abstractmethod
    def transition_to(self, state: State) -> None:
        raise NotImplementedError


class FunctionalObject(ABC):
    # abstract interface of a functional object
    @abstractmethod
    def operation_a(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def operation_b(self) -> None:
        raise NotImplementedError


class AbstractState(FunctionalObject, State):
    # used to override the typing of _context
    # & build Concrete interface
    _context: AbstractContext


class AbstractContext(FunctionalObject, Context):
    # used to override the typing of _state
    # & build Concrete interface
    _state: Optional[AbstractState] = None


class ConcreteStateA(AbstractState):
    # implements the abstract definition of a Concrete interface
    def operation_a(self) -> None:
        new_state = ConcreteStateB()
        print(
            f"operation_a - Transitioning to New State :  {new_state.__class__.__name__}"
        )
        self._context.transition_to(new_state)

    def operation_b(self) -> None:
        print(f"{self.__class__.__name__} :  operation_b")


class ConcreteStateB(AbstractState):
    # implements the abstract definition of a Concrete interface
    def operation_a(self) -> None:
        print(f"{self.__class__.__name__} :  operation_a")

    def operation_b(self) -> None:
        new_state = ConcreteStateA()
        print(
            f"operation_b - Transitioning to New State :  {new_state.__class__.__name__}"
        )
        self._context.transition_to(new_state)


class ConcreteContext(AbstractContext):
    # an interface to client
    # NOTE: here we build this using inherited-built objects
    def __init__(self, state: AbstractState) -> None:
        self.transition_to(state)

    def transition_to(self, state: AbstractState) -> None:
        # sets the new state and defines self as the context manager for that state
        self._state = state
        self._state._context = self
        print(f"New State set :  {self._state.__class__.__name__}")

    def operation_a(self) -> None:
        if self._state is None:
            raise StateNotSetError("State has not been set in the Context.")
        self._state.operation_a()

    def operation_b(self) -> None:
        if self._state is None:
            raise StateNotSetError("State has not been set in the Context.")
        self._state.operation_b()


if __name__ == "__main__":
    initial_state = ConcreteStateA()
    context = ConcreteContext(initial_state)

    context.operation_b()
    context.operation_a()  # transitions to ConcreteStateB
    context.operation_a()
    context.operation_b()  # transitions to ConcreteStateA
