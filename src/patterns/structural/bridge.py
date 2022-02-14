from abc import ABC


class Implementation(ABC):
    # an abstract interface that defines how ConcreteImplementations will be called
    # NOTE: does not have to match the inteded Abstraction interface
    def operation_implemented(self) -> str:
        raise NotImplementedError


class ConcreteImplementationA(Implementation):
    # example ConcreteImplementation that defines how to accomplish something
    def operation_implemented(self) -> str:
        return self.__class__.__name__


class ConcreteImplementationB(Implementation):
    # example ConcreteImplementation that defines how to accomplish something
    def operation_implemented(self) -> str:
        return self.__class__.__name__ + " WOW!"


class Abstraction:
    # Abstraction defining an interface that will be called by a client
    # NOTE: could be an abstract interface as well

    def __init__(self, implementation: Implementation) -> None:
        # accepting implentation definition from client
        # NOTE: the implentation could be hard-coded, or could be defined at runtime
        self.__implementation = implementation

    def operation(self) -> None:
        # example operation that uses its implementation
        implementation_use = self.__implementation.operation_implemented()
        print(f'{self.__class__.__name__}: {implementation_use}')


class ExtendedAbstraction(Abstraction):
    # an extended Abstraction that could include similar functionality
    def operation(self) -> None:
        super().operation()
        print('! Extended Functionality !')


# this script is an example of an executing client, in which might be an object in itself
if __name__ == "__main__":
    # example of an abstraction and implementation combination
    implementation_a = ConcreteImplementationA()
    abstraction_a = Abstraction(implementation_a)
    abstraction_a.operation()

    # example of an extended abstraction and a different implementation
    # NOTE: could have used the same implementation
    implementation_b = ConcreteImplementationB()
    abstraction_b = ExtendedAbstraction(implementation_b)
    abstraction_b.operation()
