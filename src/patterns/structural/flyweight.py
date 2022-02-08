
from typing import Dict, List


class Flyweight:
    # a concrete object that needs to be managed
    def __init__(self, state: Dict[str, str]) -> None:
        self._state = state

    def operation(self) -> None:
        return self._state


class FlyweightFactory:
    # a factory that controls creation and management of flyweights
    _flyweights: Dict[str, Flyweight]

    def __init__(self, flyweights: List[Flyweight]) -> None:
        # intialize flyweights available, not required
        self._flyweights = {self.get_key(fw): fw for fw in flyweights}

    def get_key(self, state: Dict[str, str]) -> str:
        # key method to managing flyweight in hash-map, dict
        atteibute_list = state.values()
        return "_".join(sorted(atteibute_list))

    def get_flyweight(self, state: Dict[str, str]) -> Flyweight:
        # makes flyweight if not exists, creates otherwise
        key = self.get_key(state)

        if not self._flyweights.get(key):
            self._flyweights[key] = Flyweight(state)

        return self._flyweights.get(key)

    def list_flyweights(self) -> List[Flyweight]:
        # used to demonstating list of flyweights
        return self._flyweights.keys()


if __name__ == "__main__":
    # creating and viewing flyweights mapped to Flyweight Factory
    initial_flyweights = [
        {"state_attribute": str(i)} for i in range(5)
    ]

    flyweight_factory = FlyweightFactory(initial_flyweights)
    print("Factory Flyweights :  ", flyweight_factory.list_flyweights())

    new_flyweight = flyweight_factory.get_flyweight({"state_attribute": "420"})
    print("New Flyweight :  ", new_flyweight._state)
    print("Factory Flyweights :  ", flyweight_factory.list_flyweights())

    reget_flyweight = flyweight_factory.get_flyweight({"state_attribute": "420"})
    print("Factory Flyweights :  ", flyweight_factory.list_flyweights())
    print(f"Validating Object IDs : (Match={id(new_flyweight) == id(reget_flyweight)})", id(new_flyweight), id(reget_flyweight))
