from abc import ABC


class Target(ABC):
    # an ansbtract interface class that a client would use
    def request(self) -> None:
        raise NotImplementedError


class Adaptee:
    # adaptee class that is not compatible with the Target interface
    def adaptee_request1(self) -> None:
        return "Adaptee"

    def adaptee_request2(self) -> None:
        return "Request"


class InheritedAdapter(Target, Adaptee):
    # concrete target interface that uses inheritence to interface with the adaptee
    def request(self) -> None:
        print(f"{self.__class__.__name__} - {self.adaptee_request1()} {self.adaptee_request2()}")


class InstanceAdapter(Target):
    # concrete target interface that uses an instance of the adaptee to interface with it
    def __init__(self) -> None:
        self.adaptee = Adaptee()

    def request(self) -> None:
        print(f"{self.__class__.__name__} - {self.adaptee.adaptee_request1()} {self.adaptee.adaptee_request2()}")


# this script is an example of an executing client, in which might be an object in itself
if __name__ == "__main__":
    # inheritence adapter example
    inh_adapter = InheritedAdapter()
    inh_adapter.request()

    # instance adapter example
    ins_adapter = InstanceAdapter()
    ins_adapter.request()
