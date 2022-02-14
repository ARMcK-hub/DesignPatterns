class Subsystem:
    # a complex subsystem, intended to be hidden, but available, from client
    def operation(self) -> None:
        return f"{self.__class__.__name__} :  operation"


class OtherSubsystem:
    # another hidden, but available, subsystem
    def other_operation(self) -> None:
        return f"{self.__class__.__name__} :  other_operation"


class Facade:
    # a general facade that calls the underlying subsystems and acts as an interface to the client
    # does not need to be customizable, can have default subsystems like ExposedFacade
    def __init__(self, sub: Subsystem, other_sub: OtherSubsystem) -> None:
        self.subsystem = sub
        self.other_subsystem = other_sub

    def interface_op(self) -> None:
        print("Doing interface_op, calling subsystems:")
        print(self.subsystem.operation())
        print(self.other_subsystem.other_operation())


class ExposedFacade(Facade):
    # configured Facade
    def __init__(self) -> None:
        # NOTE: could also use *args, **kwargs to pass subsystem / runtime config to the underlying facade
        super().__init__(Subsystem(), OtherSubsystem())


if __name__ == "__main__":
    # client use of Facade and subsystems
    interfacing_facade = ExposedFacade()
    interfacing_facade.interface_op()
