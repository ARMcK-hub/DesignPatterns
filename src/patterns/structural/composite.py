from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List

from src.utils import stdout_var


class Component(ABC):
    # an abstract interface for a leaf or primitive component
    _parent: Component

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        raise NotImplementedError


class Leaf(Component):
    # a concrete leaf component, it is not intended to be a composite
    def operation(self) -> str:
        return self.__class__.__name__


class Composite(Component):
    # a composite componenet that can have and manage child components
    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch[{', '.join(results)}]"


class DynamicComponent(ABC):
    # an abstract self-promoting/demoting componenet
    # uses and implementated_operation to call underlying functionality if the component is not a composite
    parent: DynamicComponent

    def __init__(self) -> None:
        self._children: List[DynamicComponent] = []

    @abstractmethod
    def _implemented_operation(self) -> Any:
        raise NotImplementedError

    def add(self, component: DynamicComponent) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: DynamicComponent) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True if len(self._children) > 0 else False

    def operation(self) -> str:
        if not self.is_composite():
            return self._implemented_operation()
        else:
            results = []
            for child in self._children:
                results.append(child.operation())
            return f"Branch[{', '.join(results)}]"


class LeafDC(DynamicComponent):
    # example dynamic component
    def _implemented_operation(self) -> Any:
        return self.__class__.__name__


class OtherDC(DynamicComponent):
    # example dynamic component
    def _implemented_operation(self) -> Any:
        return self.__class__.__name__


# this script is an example of an executing client, in which might be an object in itself
if __name__ == "__main__":
    # example of a simple operation with a single leaf object
    simple_comp = Leaf()
    simple_ops = simple_comp.operation()
    stdout_var(f"{simple_ops=}", simple_ops)

    # example of a complex operation with 2 branches and a leaf object
    tree = Composite()
    branch_a = Composite()
    branch_a.add(Leaf())
    branch_a.add(Leaf())

    branch_b = Composite()
    branch_b.add(Leaf())

    tree.add(branch_a)
    tree.add(branch_b)
    tree.add(Leaf())
    complex_ops = tree.operation()
    stdout_var(f"{complex_ops=}", complex_ops)

    # example of a self-promoting/demoting DynamicComponent
    comp = LeafDC()
    print("With no child components - comp.is_composite(): ", comp.is_composite())

    comp_1 = LeafDC()
    comp_1.add(OtherDC())
    comp_1.add(LeafDC())

    comp_2 = OtherDC()
    comp_2.add(LeafDC())

    added_comps = [comp_1, comp_2, LeafDC()]
    [comp.add(c) for c in added_comps]
    print("After adding child components, self-promotion - comp.is_composite(): ", comp.is_composite())
    controlled_complex_ops = comp.operation()
    stdout_var(f"{controlled_complex_ops=}", controlled_complex_ops)

    [comp.remove(c) for c in added_comps]
    print("After removing child components, self-demotion - comp.is_composite(): ", comp.is_composite())
