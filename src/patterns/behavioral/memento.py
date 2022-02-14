from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Any, List
from uuid import uuid4


@dataclass
class MementoMetadata:
    # not-required, used to store structured metadata about a memento
    id: str
    state: str
    timestamp: datetime.timestamp = datetime.now()


class MementoOriginator(ABC):
    # enforcing a memento originator must have attribute _state
    _state: Any


class Memento:
    # a save-state of an Originator, that is not actually an Originator
    def __init__(self, originator: MementoOriginator) -> None:
        self.__metadata = MementoMetadata(uuid4(), originator._state)

    def get_id(self) -> str:
        return self.__metadata.id

    def get_state(self) -> str:
        return self.__metadata.state

    def get_timestamp(self) -> datetime.timestamp:
        return self.__metadata.timestamp


class Originator(MementoOriginator):
    # an object that can save its state to a Memento
    def __init__(self, state: str) -> None:
        self._state = state

    def save(self) -> Memento:
        return Memento(self)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Restoring Originator to state {self._state}")

    def change_state(self, change_state: str) -> None:
        print(f"Changing State to {change_state}")
        self._state = change_state


class Caretaker:
    # manager of a Originator and its save-states (Mementos)
    def __init__(self, originator: Originator) -> None:
        self._mementos: List[Memento] = []
        self._originator: Originator = originator
        self.backup()

    def backup(self) -> None:
        print(f"Backing up Originator with state {self._originator._state}")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        self._mementos.pop()
        memento = self._mementos[-1]
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def history(self) -> None:
        return [m.get_id() for m in self._mementos]


if __name__ == "__main__":
    originator = Originator("First")
    caretaker = Caretaker(originator)

    originator.change_state("Second")
    caretaker.backup()

    originator.change_state("Third")
    caretaker.backup()

    print("Caretaker History :  ", caretaker.history())

    caretaker.undo()
    print("Current State :  ", originator._state)
