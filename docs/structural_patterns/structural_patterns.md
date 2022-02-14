# Structural Pattern Overview
-----

## Adapter  
**Alias:** `Wrapper`  
**Intent:** Translate an interface to be client compatible  
**Components:** `Target`, `Client`, `Adaptee`, `Adapter`  
**Implementation:** [adapter.py](/src/patterns/creational/adapter.py)  
**Related:**  
- Similar to [Bridge](/docs/structural_patterns/structural_patterns.md#bridge), except Adapters are applied after a system is designed
- Similar to [Proxy](/docs/structural_patterns/structural_patterns.md#proxy), except designed to change interface, where Proxy is meant for access control

## Bridge  
**Alias:** `Handle/Body`  
**Intent:** Decouple an abstraction from its implementation  
**Components:** `Abstraction`, `RefmedAbstraction`, `Implementor`, `ConcreteImplementor`  
**Implementation:** [bridge.py](/src/patterns/creational/bridge.py)  
**Related:**  
- [Abstract Factory](/docs/creational_patterns/creational_patterns.md#abstract-factory) can be used to create and configure Bridges
- Similar to [Adapter](/docs/structural_patterns/structural_patterns.md#adapter), except Bridges are applied before systems are designed

## Composite  
**Intent:** Form objects into parent-child tree structures  
**Components:** `Component`, `Leaf`, `Composite`, `Client`  
**Implementation:** [composite.py](/src/patterns/creational/composite.py)  
**Related:**  
- `Component`-`Parent` link often used in [Chain of Responsibility](/docs/behavioral_patterns/behavioral_patterns.md#chain-of-responsibility)
- Often implements [Decorator](/docs/structural_patterns/structural_patterns.md#decorator)(s)
- An [Iterator](/docs/behavioral_patterns/behavioral_patterns.md#iterator) can be used to traverse a Composite
- Similar to [Visitor](/docs/behavioral_patterns/behavioral_patterns.md#visitor), except Composite have distributed operations and behavior where as Visitors are localized
- Often combined with [Flyweight](/docs/structural_patterns/structural_patterns.md#flyweight)(s) to share `Leaf` nodes

## Decorator  
**Alias:** `Wrapper`  
**Intent:** Extend functionality with wrapper classes  
**Components:** `Component`, `ConcreteComponent`, `Decorator`, `ConcreteDecorator`  
**Implementation:** [decorator.py](/src/patterns/creational/decorator.py)  
**Related:**  
- Opposite to [Strategy](/docs/behavioral_patterns/behavioral_patterns.md#strategy), where Decorator changes an object's "skin", a Strategy changes its "guts"

## Facade  
**Intent:** Simplify complex subsystems with a unified interface  
**Components:** `Facade`, `SubSystem`(s)  
**Implementation:** [facade.py](/src/patterns/creational/facade.py)  
**Related:**  
- [Abstract Factory](/docs/creational_patterns/creational_patterns.md#abstract-factory) can be used to create a Facade's subsystems
- [Abstract Factory](/docs/creational_patterns/creational_patterns.md#abstract-factory) can also be used in place of a Facade to hide subsystems
- Similar to [Mediator](/docs/behavioral_patterns/behavioral_patterns.md#mediator), except a Facade's subsystems might know of and communicate with eachother
- Facade(s) are often [Singleton](/docs/creational_patterns/creational_patterns.md#singleton)(s)

## Flyweight  
**Intent:** Reduce object instances by sharing them through a management `FlyweightFactory`  
**Components:** `Flyweight`, `ConcreteFlyweight`, `UnsharedConcreteFlyweight`, `FlyweightFactory`, `Client`  
**Implementation:** [flyweight.py](/src/patterns/creational/flyweight.py)  
**Related:**  
- Often implemented in a [Composite](/docs/structural_patterns/structural_patterns.md#composite) to enable `Leaf` sharing
- Often best to implement [State](/docs/behavioral_patterns/behavioral_patterns.md#state)(s) and [Strategy](/docs/behavioral_patterns/behavioral_patterns.md#strategy)(s) as Flyweights

## Proxy  
**Alias:** `Surrogate`  
**Intent:** Control access to an underlying object  
**Components:** `Proxy`, `Subject`, `RealSubject`  
**Implementation:** [proxy.py](/src/patterns/creational/proxy.py)  
**Related:**  
- Similar to [Adapter](/docs/structural_patterns/structural_patterns.md#adapter), except not designed to change interface, where Proxy is meant for access control
