from abc import ABC, abstractmethod

from src.utils.container import Container


class Product(ABC):
    """
    Abstract Product that defined the interface of the product that is shared with its implementations.
    Generally This bins Abstract Factories to be used for similar Product Families.
    """

    def __init__(self, input: str) -> None:
        self.attribute1: str = input

    @abstractmethod
    def operation1(self) -> None:
        """Sample product interface operation."""
        raise NotImplementedError


class Factory(ABC):
    """
    Abstract Factory that controls building of a product.
    """

    @abstractmethod
    def build_product(self) -> Product:
        """
        docstring
        """
        raise NotImplementedError


class ConcreteProduct(Product):
    """
    A concrete implemntation of Product
    """

    def operation1(self) -> None:
        """Sample product interface"""
        print(f"Executed {self.operation1.__name__} with id: {self.attribute1}")


class ConcreteFactory(Factory):
    def build_product(self) -> Product:
        return ConcreteProduct("Standard")


class IocFactory(ABC):
    @abstractmethod
    def build_product(self, ioc_product: Product.__class__) -> None:
        raise NotImplementedError


class IocConcreteFactory(IocFactory):
    def build_product(self, ioc_product: Product.__class__) -> None:
        return ioc_product("Ioc")


if __name__ == "__main__":
    # Example: General Application
    factory = ConcreteFactory()
    product = factory.build_product()

    product.operation1()

    # Example: Product DI -
    product_type = ConcreteProduct
    factory = (
        IocConcreteFactory()
    )  # Note that the IoC could have occured on initializing of the factory
    product = factory.build_product(product_type)  # Implementing DI
    product.operation1()

    # Example: Factory IoC - Allows application to request the type of factory / product
    container = Container()
    container.register_service(
        Factory, ConcreteFactory()
    )  # register in application configuration

    factory: Factory = container.get_service(Factory)  # access throughout application
    product: Product = factory.build_product()
    product.operation1()
