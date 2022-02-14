from abc import ABC, abstractmethod


class Product(ABC):
    # abstract product that defines some general interface
    def print_self(self) -> None:
        print(f"class: {self.__class__.__name__}")


class ConcreteProductA(Product):
    # implementation of Product
    pass


class ConcreteProductB(Product):
    # implementation of Product
    pass


class Creator(ABC):
    # abstract creator that defines the interface for a factory method

    @abstractmethod
    def factory_method(self) -> Product:
        # abstract method that is implemented due to not knowing what product might be needed
        raise NotImplementedError

    def create_product(self) -> Product:
        # operational method that is used to create a product of unknown type
        product = self.factory_method()
        return product()


class ConcreteCreatorA(Creator):
    # example implementation that uses a ConcreteProductA product
    def factory_method(self) -> Product:
        return ConcreteProductA


class ConcreteCreatorB(Creator):
    # example implementation that uses a ConcreteProductB product
    def factory_method(self) -> Product:
        return ConcreteProductB


if __name__ == "__main__":
    # example ConcreteCreatorA
    creator_a = ConcreteCreatorA()
    product_a = creator_a.create_product()
    product_a.print_self()

    # example ConcreteCreatorB
    creator_b = ConcreteCreatorB()
    product_b = creator_b.create_product()
    product_b.print_self()
