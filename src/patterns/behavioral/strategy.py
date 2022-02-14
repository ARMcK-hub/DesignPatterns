from abc import ABC, abstractmethod


class Strategy(ABC):
    # abstract interface to Strategy
    @abstractmethod
    def operation(self) -> None:
        raise NotImplementedError


class Context:
    # defines interface to clients & manages Strategies
    _strategy: Strategy

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def operation(self) -> None:
        # calls underlying Strategies
        # NOTE: does not have to implement the same interface
        # as strtegies (like a Context Manager)
        self._strategy.operation()


class ConcreteStrategy(Strategy):
    # a functional type of Strategy
    def operation(self) -> None:
        print(f"Operation with {self.__class__.__name__}")


class OtherConcreteStrategy(Strategy):
    # another functional type of Strategy
    def operation(self) -> None:
        print(f"Another Operation with {self.__class__.__name__}")


if __name__ == "__main__":
    strategy = ConcreteStrategy()
    context = Context(strategy)
    context.operation()

    # swapping out strategy
    context._strategy = OtherConcreteStrategy()
    context.operation()
