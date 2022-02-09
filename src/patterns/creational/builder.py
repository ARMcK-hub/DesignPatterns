from abc import ABC, abstractmethod, abstractproperty
from typing import Optional, Type


class Product:
    # a general, but concrete Product
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: str) -> None:
        self.parts.append(part)


class Builder(ABC):
    # abstract way of building a product
    @abstractproperty
    def product(self) -> Product:
        raise NotImplementedError

    @abstractmethod
    def build_part_a(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def build_part_b(self) -> None:
        raise NotImplementedError


class ConcreteBuilder(Builder):
    # concrete implementation of a Builder that defines how to build the actual parts of a product
    def __init__(self, product_type: Type[Product]) -> None:
        self.product_type = product_type
        self.reset()

    def reset(self) -> None:
        # resets the product
        self._product = self.product_type()

    @property
    def product(self) -> Product:
        # resetting the product is required so that it is released, and a new product can be made
        # building all in one operation is generally not desired as the point of a Builder is to
        # break part-building into steps
        product = self._product
        self.reset()
        return product

    def build_part_a(self) -> None:
        self._product.add("PartA")

    def build_part_b(self) -> None:
        self._product.add("PartB")


class Director:
    # a Director orchestrates the building of a product through a builder,
    # Directors generally do not know what products they are building
    # they are optional, as client code could be considered a director
    builder: Optional[Builder] = None

    def build_small_product(self) -> None:
        self.builder.build_part_a()
        return self.builder.product

    def build_large_product(self) -> None:
        self.builder.build_part_a()
        self.builder.build_part_b()
        return self.builder.product


if __name__ == "__main__":
    # initializing a director with a configured builder
    director = Director()
    builder = ConcreteBuilder(Product)
    director.builder = builder

    # the same director can be used to build different products
    small_product = director.build_small_product()
    large_product = director.build_large_product()

    # NOTE: that parts is unknown because the type of product is unknown to the Director
    print(f"Small Product : {small_product.parts}")
    print(f"Large Product : {large_product.parts}")
