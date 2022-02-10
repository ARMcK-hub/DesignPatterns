from __future__ import annotations

import inspect
from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Type


class Colleague(ABC):
    # a 'subsystem' that doesn't know or communicate with other subsystems
    _mediator: Mediator


class Mediator(ABC):
    # an abstract mediator that manages and operates on colleagues
    def __init__(self, colleagues: List[Colleague]) -> None:
        self._colleagues = {col.__class__: col for col in colleagues}
        self.self_mediate()

    def self_mediate(self) -> None:
        # assigns self as mediator to its colleagues
        for colleague in self._colleagues:
            colleague._mediator = self

    def get_colleague(self, colleague_type: Type[Colleague]) -> Colleague:
        return self._colleagues.get(colleague_type)

    @abstractmethod
    def notify(self, sender: Colleague, event: str) -> None:
        # used to mediate between colleagues
        raise NotImplementedError


class ColleagueA(Colleague):
    # a ConcreteColleague that has operations
    def operation_a(self) -> None:
        print(f"{self.__class__.__name__} :  operation_a")
        self._mediator.notify(self.__class__.operation_a)

    def operation_b(self) -> None:
        print(f"{self.__class__.__name__} :  operation_b")
        self._mediator.notify(self.__class__.operation_b)


class ColleagueB(Colleague):
    # a ConcreteColleague that has operations
    def operation_a(self) -> None:
        print(f"{self.__class__.__name__} :  operation_a")
        self._mediator.notify(self.__class__.operation_a)

    def operation_b(self) -> None:
        print(f"{self.__class__.__name__} :  operation_b")
        self._mediator.notify(self.__class__.operation_b)


class ConcreteMediator(Mediator):
    def notify(self, event: Type[Callable]) -> None:
        # listens for an event and runs operations listed in the event_map
        ops = self._get_operations(event)

        for op in ops:
            op_class = self._get_class_from_method(op)
            # acquires the specific colleague in order to ensure the proper instance is used
            colleague = self.get_colleague(op_class)
            try:
                func = getattr(colleague, op.__name__)
                func()
            except ValueError:
                raise Exception(
                    f"Colleague {colleague.__class__.__name__} does not have operation {op.__name__}"
                )

    def _get_class_from_method(self, method: Callable) -> Type[Type]:
        # acquires class from a class method
        return getattr(inspect.getmodule(method), method.__qualname__.split(".")[0])

    def _get_operations(self, event: Type[Callable]) -> List[Callable]:
        # acquires operations from event_map
        event_map = self.get_event_map()
        return event_map[event]

    def get_event_map(self) -> Dict[Callable, List[Callable]]:
        # mapping of operations to events
        return {
            ColleagueA.operation_a: [ColleagueA.operation_b, ColleagueB.operation_a],
            ColleagueA.operation_b: [ColleagueB.operation_b],
            ColleagueB.operation_a: [ColleagueB.operation_b],
            ColleagueB.operation_b: [],
        }


if __name__ == "__main__":
    colleague_a = ColleagueA()
    colleague_b = ColleagueB()
    mediator = ConcreteMediator([colleague_a, colleague_b])

    print("\nRunning Operations of ColleagueA.operation_a")
    colleague_a.operation_a()

    print("\nRunning Operations from CollegueB.operation_a")
    colleague_b.operation_a()
