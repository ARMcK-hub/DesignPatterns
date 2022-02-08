
from typing import Dict, List


class Flyweight:
    # a concrete object that needs to be managed
    def __init__(self, state: Dict[str, str]) -> None:
        self.__state = state

    def get_state(self) -> None:
        # used to obtain the extrensic state of a flyweight, 
        # intrensic states (actual object) should not be used to create / obtain flyweights
        # as this should be managed by the factory
        return self.__state


class FlyweightFactory:
    # a factory that controls creation and management of flyweights
    __flyweights: Dict[str, Flyweight]

    def __init__(self, flyweights: List[Flyweight]) -> None:
        # intialize flyweights available, not required
        self.__flyweights = {self.get_key(fw): fw for fw in flyweights}

    def get_key(self, state: Dict[str, str]) -> str:
        # key method to managing flyweight in hash-map, dict
        atteibute_list = state.values()
        return "_".join(sorted(atteibute_list))

    def get_flyweight(self, state: Dict[str, str]) -> Flyweight:
        # makes flyweight if not exists, creates otherwise
        key = self.get_key(state)

        if not self.__flyweights.get(key):
            self.__flyweights[key] = Flyweight(state)

        return self.__flyweights.get(key)

    def list__flyweights(self) -> List[Flyweight]:
        # used to demonstating list of flyweights
        return self.__flyweights.keys()


if __name__ == "__main__":
    # creating and viewing flyweights mapped to Flyweight Factory
    initial__flyweights = [
        {"state_attribute": str(i)} for i in range(5)
    ]

    flyweight_factory = FlyweightFactory(initial__flyweights)
    print("Factory Flyweights :  ", flyweight_factory.list__flyweights())

    new_flyweight = flyweight_factory.get_flyweight({"state_attribute": "420"})
    print("New Flyweight :  ", new_flyweight.get_state())
    print("Factory Flyweights :  ", flyweight_factory.list__flyweights())

    reget_flyweight = flyweight_factory.get_flyweight(new_flyweight.get_state())
    print("Factory Flyweights :  ", flyweight_factory.list__flyweights())
    print(f"Validating Object IDs : (Match={id(new_flyweight) == id(reget_flyweight)})", id(new_flyweight), id(reget_flyweight))
