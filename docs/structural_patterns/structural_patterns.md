# Structural Pattern Overview
-----

## Adapter  
**Alias:** `Wrapper`  
**Intent:** Translate an interface to be client compatible  
**Components:** `Target`, `Client`, `Adaptee`, `Adapter`  
**Implementation:** [adapter.py](/src/patterns/creational/adapter.py)  
**Related:**  
- TODO

## Bridge  
**Alias:** `Handle/Body`  
**Intent:** Decouple an abstraction from its implementation  
**Components:** `Abstraction`, `RefmedAbstraction`, `Implementor`, `ConcreteImplementor`  
**Implementation:** [bridge.py](/src/patterns/creational/bridge.py)  
**Related:**  
- TODO

## Composite  
**Intent:** Form objects into parent-child tree structures  
**Components:** `Component`, `Leaf`, `Composite`, `Client`  
**Implementation:** [composite.py](/src/patterns/creational/composite.py)  
**Related:**  
- TODO

## Decorator  
**Alias:** `Wrapper`  
**Intent:** Extend functionality with wrapper classes  
**Components:** `Component`, `ConcreteComponent`, `Decorator`, `ConcreteDecorator`  
**Implementation:** [decorator.py](/src/patterns/creational/decorator.py)  
**Related:**  
- TODO

## Facade  
**Intent:** Simplify complex subsystems with a unified interface  
**Components:** `Facade`, `SubSystem`(s)  
**Implementation:** [facade.py](/src/patterns/creational/facade.py)  
**Related:**  
- TODO

## Flyweight  
**Intent:** Reduce object instances by sharing them through a management factory  
**Components:** `Flyweight`, `ConcreteFlyweight`, `UnsharedConcreteFlyweight`, `FlyweightFactory`, `Client`  
**Implementation:** [flyweight.py](/src/patterns/creational/flyweight.py)  
**Related:**  
- TODO

## Proxy  
**Alias:** `Surrogate`  
**Intent:** Control access to an underlying object  
**Components:** `Proxy`, `Subject`, `RealSubject`  
**Implementation:** [proxy.py](/src/patterns/creational/proxy.py)  
**Related:**  
- TODO
