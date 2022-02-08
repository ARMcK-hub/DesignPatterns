# Creational Pattern Overview
-----
## Abstract Factory
**Alias:** `Kit` 
**Intent:** Create objects without specifying concrete classes
**Components:** `AbstractFactory`, `ConcreteFactory`, `AbstractProduct`, `ConcreteProduct`, `Client`
**Implementation:** [abstract_factory.py](/src/patterns/creational/abstract_factory.py)
**Related:** 
- `ConcreteFactory` is usually a [Singleton](/docs/creational_patterns/creational_patterns.md#singleton)
- Can be implemented via [Prototype](/docs/creational_patterns/creational_patterns.md#prototype)
- Can be implemented via [Factory Method](/docs/creational_patterns/creational_patterns.md#factory-method)
- Similar to [Builder](/docs/creational_patterns/creational_patterns.md#builder), but not step-by-step building

## Builder
**Intent:** Create complex objects step-by-step via same construction process
**Components:** `Builder`, `ConcreteBuilder`, `Director`, `Product`
**Implementation:** [builder.py](/src/patterns/creational/builder.py)
**Related:** 
- Similar to [Abstract Factory](/docs/creational_patterns/creational_patterns.md#abstract-factory), but uses step-by-step building
- [Composite](/docs/structural_patterns/structural_patterns.md#composite) is often built by Builders

## Factory Method
**Alias:** `Virtual Constructor`
**Intent:** Create subclass-altered/defined superclass objects
**Components:** `Product`, `ConcreteProduct`, `Creator`, `ConcreteCreator`
**Implementation:** [factory_method.py](/src/patterns/creational/factory_method.py)
**Related:**
- Often implements [Abstract Factory](/docs/creational_patterns/creational_patterns.md#abstract-factory)
- Usually called within [Template Method](/docs/behavioral_patterns/behavioral_patterns.md#template-method)
- Similar to [Prototype](/docs/creational_patterns/creational_patterns.md#prototype) but doesn't require `Product` initialization

## Prototype
**Intent:** Create replica objects from a prototype
**Components:** `Prototype`, `ConcretePrototype`, `Client`
**Implementation:** [prototype.py](/src/patterns/creational/prototype.py)
**Related:**
- Similar to [Abstract Factory](/docs/creational_patterns/creational_patterns.md#abstract-factory), but requires `Product` initialization
- Typically integrates will with heavy use of [Composite](/docs/structural_patterns/structural_patterns.md#composite) and [Decorator](/docs/structural_patterns/structural_patterns.md#decorator) patterns

## Singleton
**Intent:** Ensure a class only has one instance
**Components:** `Singleton`
**Implementation:** [singleton.py](/src/patterns/creational/singleton.py)
**Related:**
- Can implement many other patterns, for example [Abstract Factory](/docs/creational_patterns/creational_patterns.md#abstract-factory)
