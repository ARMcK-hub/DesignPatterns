from __future__ import annotations

from src.utils import Singleton


class ConcreteSingleton(metaclass=Singleton):
    """
    A concrete implementation of a Singleton.
    """
    def __init__(self, instance_value: str) -> None:
        self.instance_value = instance_value

    def print_instance_value(self, check_value: str) -> None:
        # validates and print check value
        check_msg = "Instance Values match" if self.instance_value == check_value else "Instance Values DO NOT match"
        print(f"{check_msg} - Instance Value: {self.instance_value}    Check Value: {check_value}")

    def validate_instance(self, initial_instance: ConcreteSingleton) -> None:
        print(f"Is initial instance: {id(self) == id(initial_instance)}")


if __name__ == "__main__":
    # creating instance check value
    instance_value = "Instance 1"

    # trying to create 2 seperate instances
    initial_instance = ConcreteSingleton(instance_value)
    new_instance = ConcreteSingleton()

    # validating that instance 2 is actually instance 1
    new_instance.print_instance_value(instance_value)
    new_instance.validate_instance(initial_instance)
