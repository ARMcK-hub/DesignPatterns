from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional


class Observer(ABC):
    # abstract observer defining interface to recieve notifications
    @abstractmethod
    def update(self, subject: Subject) -> None:
        raise NotImplementedError


class ConcreteObserver(Observer):
    # implemented notification interface for an observing object
    def __init__(self, observer_name: str, state_attributes: List[str]) -> None:
        self._observer_name = observer_name
        self._state_attributes = state_attributes

    def update(self, subject: Subject) -> None:
        if subject._state in self._state_attributes:
            print(f"{self._observer_name} likes {subject._state}")


class Subject(ABC):
    # abstract subject that stores and notifies observing objects
    _observers: List[Observer] = []
    _state: Optional[str] = None

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify(self) -> None:
        raise NotImplementedError


class ConcreteSubject(Subject):
    # concrete subject that can change its state
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def change_state(self, state: str) -> None:
        self._state = state
        self.notify()


if __name__ == "__main__":
    subject = ConcreteSubject()
    bob = ConcreteObserver("bob ross", ["bob", "ross", "money"])
    joe = ConcreteObserver("joe dirt", ["joe", "dirt", "money"])

    subject.attach(bob)
    subject.attach(joe)

    subject.change_state("bob")
    subject.change_state("joe")
    subject.change_state("money")

    print("Removing Joe from oberserving")
    subject.detach(joe)
    subject.notify()
