from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Callable, List, Union


class SequentialIterator(Iterator):
    # an interator that can
    def __init__(self, collection: SequentialCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        # default function used to iterate through an Iterable
        try:
            iteration = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return iteration


class SequentialCollection(list):
    # an example collection that sorts itself
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._collection.sort()

    def __iter__(self) -> SequentialIterator:
        # implement standard iterator via default function
        return SequentialIterator(self._collection)

    def reverse(self) -> SequentialIterator:
        # implement reverse iterator
        return [i for i in SequentialIterator(self._collection, True)]

    def invoke(self, command: Union[Callable, str], *args, **kwargs) -> None:
        # allowing all functions pf list to be used, but sorting afterwards
        # NOTE: this is probably not best implementation, better would be to have a Command Invoker
        if isinstance(command, Callable):
            command = command.__name__
        try:
            function = getattr(self._collection, command)
        except AttributeError:
            raise Exception(
                f"SequentialCollection has no function {command}, please use functions from 'list'."
            )

        function(*args, **kwargs)
        self._collection.sort()

    def __repr__(self) -> str:
        # overwritten for printing
        return str(self._collection)

    def __str__(self) -> str:
        # overwriten for printing
        return str(self._collection)


if __name__ == "__main__":
    init_list = [1, 3, 2]
    collection = SequentialCollection(init_list)

    # using standard iterator
    collection.invoke(list.extend, ([1, 2]))
    print(collection)

    # using reverse iterator
    collection.invoke("pop")
    print(collection.reverse())
