from __future__ import annotations

import copy
from abc import ABC


class Prototype(ABC):
    # example prototype class that implements a clone interface.
    # Note that cloning interface could be overwritten in subclasses.
    def __init__(self, sample_attribute: str) -> None:
        # used to set an sample attribute to show that clones keep attributes
        self.attribute = sample_attribute

    def clone(self) -> Prototype:
        # returns a clone of self
        return copy.copy(self)

    def print_prototype(self) -> None:
        # class to show that even clones keep their creator's attributes
        print(f"class: {self.__class__.__name__}  attribute: {self.attribute}")


class ConcretePrototypeA(Prototype):
    # example subclass implementation of a prototype
    pass


class ConcretePrototypeB(Prototype):
    # example subclass implementation of a prototype
    pass


# this script is an example of an executing client, in which might be an object in itself
if __name__ == "__main__":
    # PrototypeA sample
    proto_a = ConcretePrototypeA("proto_a")
    new_a = proto_a.clone()
    new_a.print_prototype()

    # PrototypeB sample
    proto_b = ConcretePrototypeB("proto_b")
    new_b = proto_b.clone()
    new_b.print_prototype()
