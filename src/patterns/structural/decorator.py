
from abc import ABC, abstractmethod

from src.utils import stdout_var


class Component(ABC):
    # abstract interface of an object
    @abstractmethod
    def operation(self) -> str:
        raise NotImplementedError


class ConcreteComponent(Component):
    # concrete implementation of object
    def operation(self) -> str:
        return self.__class__.__name__


class ComponentDecorator(Component, ABC):
    # abstract decorator with interface mirroring standard component
    def __init__(self, component: Component) -> None:
        self.__component = component

    @property
    def _component(self) -> str:
        # restricted available property for wrapped component
        return self.__component

    def operation(self) -> str:
        # performs the wrapped components operation
        return self.__component.operation()


class ConcreteDecorator(ComponentDecorator):
    # concrete implementation of a decorator
    def operation(self) -> str:
        # performs the decorator function and calls the wrapped component operation
        return f"{self.__class__.__name__}({self._component.operation()})"


if __name__ == "__main__":
    # wrapping components
    component = ConcreteComponent()
    decorated = ConcreteDecorator(component)
    decorated2 = ConcreteDecorator(decorated)

    # outputting component call sequence
    stdout_var(f"{component=}", component.operation())
    stdout_var(f"{decorated=}", decorated.operation())
    stdout_var(f"{decorated2=}", decorated2.operation())
