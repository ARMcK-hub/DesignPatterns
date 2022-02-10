from abc import ABC, abstractmethod


class Command(ABC):
    # abstract Command defining interface
    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError


class NoCommand(Command):
    # example of a Command that does 'nothing'
    def execute(self) -> None:
        print("NoCommand Executed")


class ConcreteCommand(Command):
    # ConcreteCommand implementing abstract interface
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"{self.__class__.__name__} payload :  {self._payload}")


class Receiver:
    # a subsystem-like object that receives commands from somewhere else
    # NOTE: could be just a normal object, doesn't have to be built
    # to act as a receiver
    def operation(self, input: str) -> None:
        print(f"{self.__class__.__name__} :  operation on {input}")

    def other_operation(self, input: str) -> None:
        print(f"{self.__class__.__name__} :  other_operation on {input}")


class ReceiverConcreteCommand(Command):
    # calls a receiver to execute opertaions instead of executing direcly itself
    def __init__(self, receiver: Receiver, payload: str) -> None:
        self._receiver = receiver
        self._payload = payload

    def execute(self) -> None:
        # calling reciever to delegate operations
        self._receiver.operation(self._payload)
        self._receiver.other_operation(f"modified! {self._payload}")


class Invoker:
    # Invoker, similar to Facade,
    # sends requests to Commands
    def __init__(
        self,
        start_command: Command = NoCommand(),
        finish_command: Command = NoCommand(),
    ) -> None:
        self._start_command = start_command
        self._finish_command = finish_command

    def invoked_operation(self, command: Command = NoCommand()) -> None:
        # invoked operations do not nessecarily have to have cusomizable commands
        # command could be hard-coded for this to enforce operation
        self._start_command.execute()
        command.execute()
        self._finish_command.execute()


if __name__ == "__main__":
    print("\nRunning Direct Command")
    direct_command = ConcreteCommand("DIRECT")
    direct_command.execute()

    print("\nRunning Command via Receiver")
    receiver = Receiver()
    receiver_command = ReceiverConcreteCommand(receiver, "RECEIVER")
    receiver_command.execute()

    print("\nRunning Commands via Invoker")
    invoker = Invoker(ConcreteCommand("ON_START"))
    invoker.invoked_operation(receiver_command)
