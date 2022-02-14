from abc import ABC, abstractmethod


class AbstractClass(ABC):
    # defines interface for a class that has a template method or algorithm

    def template_method(self) -> None:
        # the template algorithm
        self.base_op()
        self.config_op()
        self.other_base_op()
        self.other_config_op()
        self.hook()

    def base_op(self) -> None:
        # base_ops are required executables in the template algorithm
        print("Running base_op")

    def other_base_op(self) -> None:
        print("Running other_base_op")

    def hook(self) -> None:
        # hooks are usually optional portions
        pass

    @abstractmethod
    def config_op(self) -> None:
        # config_ops are parts of template algorithm that
        # are to be configured by subclasses
        raise NotImplementedError

    @abstractmethod
    def other_config_op(self) -> None:
        raise NotImplementedError


class ConcreteClass(AbstractClass):
    # a type of concrete implementation used to
    # alter the template algorithm
    def config_op(self) -> None:
        print(f"Running -  {self.__class__.__name__} :  config_op")

    def other_config_op(self) -> None:
        print(f"Running -  {self.__class__.__name__} :  other_config_op")

    def hook(self) -> None:
        print(f"{self.__class__.__name__} has a hook")


class OtherConcreteClass(AbstractClass):
    # another type of concrete implementation used to
    # alter the template algorithm
    def config_op(self) -> None:
        print(f"Running Other Type -  {self.__class__.__name__} :  config_op")

    def other_config_op(self) -> None:
        print(f"Running Other Type -  {self.__class__.__name__} :  other_config_op")


def client_run(_class: AbstractClass) -> None:
    # sample client code
    print(f"\nClient running with {_class.__class__.__name__}")
    _class.template_method()


if __name__ == "__main__":
    # running same code with different Concrete implementations
    client_run(ConcreteClass())
    client_run(OtherConcreteClass())
