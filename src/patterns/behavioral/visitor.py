from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional


class Element(ABC):
    # abstract interface for visitor using an element
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        # tells visitor how to use itself
        raise NotImplementedError


class ConcreteElement(Element):
    # type of element or component, used by visitor
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_element(self)

    def element_op(self) -> None:
        return f"{self.__class__.__name__}(element_op)"


class OtherConcreteElement(Element):
    # another type of element or component, used by visitor
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_other_element(self)

    def other_element_op(self) -> None:
        return f"{self.__class__.__name__}(other_element_op)"


class Visitor(ABC):
    # abstract interface to interact with different kinds of elements
    @abstractmethod
    def visit_element(self, element: ConcreteElement) -> None:
        # tells how to visit a ConcreteElement
        raise NotImplementedError

    @abstractmethod
    def visit_other_element(self, element: OtherConcreteElement) -> None:
        # tells how to visit an OtherConcreteElement
        raise NotImplementedError


class ConcreteVisitor(Visitor):
    # concrete implementation of a Visitor
    def visit_element(self, element: ConcreteElement) -> None:
        print(f"{self.__class__.__name__} - {element.element_op()} :  visit_element")

    def visit_other_element(self, element: OtherConcreteElement) -> None:
        print(
            f"{self.__class__.__name__} - {element.other_element_op()} :  visit_other_element"
        )


class OtherConcreteVisitor(Visitor):
    # another concrete implementation of a Visitor
    def visit_element(self, element: ConcreteElement) -> None:
        print(
            f"[MODIFIED] {self.__class__.__name__} - {element.element_op()} :  visit_element"
        )

    def visit_other_element(self, element: OtherConcreteElement) -> None:
        print(
            f"[MODIFIED] {self.__class__.__name__} - {element.other_element_op()} :  visit_other_element"
        )


class VisitorNotSetError(Exception):
    # generic error for when a visitor is not set in an ObjectStructure
    pass


class ObjectStructure:
    # effectively a client interface for running elements with visitors
    _visitor: Optional[Visitor] = None

    def __init__(self, elements: List[Element] = []) -> None:
        self._elements = elements

    def set_visitor(self, visitor: Visitor) -> None:
        self._visitor = visitor

    def run_ops(self) -> None:
        if self._visitor is None:
            raise VisitorNotSetError

        print(f"\nVisiting elements with {visitor.__class__.__name__}")
        for element in self._elements:
            element.accept(self._visitor)


if __name__ == "__main__":
    # running same element list with varying visitors
    elements = [ConcreteElement(), OtherConcreteElement()]
    client_object = ObjectStructure(elements)

    visitors = [ConcreteVisitor(), OtherConcreteVisitor()]

    for visitor in visitors:
        client_object.set_visitor(visitor)
        client_object.run_ops()
