# Behavioral Pattern Overview
-----

## Chain of Responsibility  
**Intent:** Chain functionality together by pointing to the next object in line  
**Components:** `Handler`, `ConcreteHandler`, `Client`  
**Implementation:** [chain_of_responsibility.py](/src/patterns/behavioral/chain_of_responsibility.py)  
**Related:**  
- Often applied in conjunction with [Composite](/docs/structural_patterns/structural_patterns.md#composite)

## Command  
**Alias:** `Action`, `Transaction`  
**Intent:** Parameterize `Command`(s) for run-time, in-code management  
**Components:** `Command`, `ConcreteCommand`, `Client`, `Invoker`, `Receiver`  
**Implementation:** [command.py](/src/patterns/behavioral/command.py)  
**Related:**  
- [Composite](/docs/structural_patterns/structural_patterns.md#composite) can be used to implement MacroCommands
- [Memento](/docs/behavioral_patterns/behavioral_patterns.md#memento) cane be used to undo a `Command`
- Can append `Commands` to execution history by making them [Prototype](/docs/behavioral_patterns/behavioral_patterns.md#prototype)(s)

## Interpreter  
**Intent:** Interpret a language into comprehensible grammar  
**Components:** `AbstractExpression`, `TerminalExpression`, `NonterminalExpression`, `Context`, `Client`  
**Implementation:** [interpreter.py](/src/patterns/behavioral/interpreter.py)  
**Related:**  
- An [Iterator](/docs/behavioral_patterns/behavioral_patterns.md#iterator) can be used to traverse the structure
- The abstract syntax tree is typically a [Composite](/docs/structural_patterns/structural_patterns.md#composite), and can generally benefit from implementing [Flyweight](/docs/structural_patterns/structural_patterns.md#flyweight)(s) and [Visitor](/docs/behavioral_patterns/behavioral_patterns.md#visitor)(s)

## Iterator  
**Alias:** `Cursor`  
**Intent:** Access aggregate objects without exposing the underlying represenation  
**Components:** `Iterator`, `ConcreteIterator`, `Aggregator`, `ConcreteAggregator`  
**Implementation:** [iterator.py](/src/patterns/behavioral/iterator.py)  
**Related:**  
- Can be used to traverse [Composite](/docs/structural_patterns/structural_patterns.md#composite)(s)
- Can store iteration states internally by using [Memento](/docs/behavioral_patterns/behavioral_patterns.md#memento)(s)

## Mediator  
**Intent:** Reduce dependencies by restricting direct object communications to a `Mediator`  
**Components:** `Mediator`, `ConcreteMediator`, `Colleague`(s)  
**Implementation:** [mediator.py](/src/patterns/behavioral/mediator.py)  
**Related:**  
- Similar to [Facade](/docs/structural_patterns/structural_patterns.md#facade), except is responsible for communication between `Colleague`(s)
- `Colleagues`(s) can communicate with the `Mediator` using an [Oberserver](/docs/behavioral_patterns/behavioral_patterns.md#observer)

## Memento  
**Alias:** `Token`  
**Intent:** Restore an object later by storing it as a momento via a `Caretaker`  
**Components:** `Momento`, `Originator`, `Caretaker`  
**Implementation:** [memento.py](/src/patterns/behavioral/memento.py)  
**Related:**  
- Can be used to store undoable states for [Command](/docs/behavioral_patterns/behavioral_patterns.md#command)(s)
- Can be used to store iteration states for [Iterators](/docs/behavioral_patterns/behavioral_patterns.md#iterator)(s)

## Observer  
**Alias:** `Dependents`, `Publish-Subscribe`  
**Intent:** Notify multiple objects when the state of one changes  
**Components:** `Subject`, `Observer`, `ConcreteSubject`, `ConcreteObserver`  
**Implementation:** [observer.py](/src/patterns/behavioral/observer.py)  
**Related:**  
- Can be used to communicate to a [Mediator](/docs/behavioral_patterns/behavioral_patterns.md#mediator) and/or between a Mediator's `Colleagues`
- Typically a [Singleton](/docs/creational_patterns/creational_patterns.md#singleton)

## State  
**Alias:** `Objects for States`  
**Intent:** Allow an object to change its class via a `Context` handler  
**Components:** `Context`, `State`, `ConcreteStateSubclass`(s)  
**Implementation:** [state.py](/src/patterns/behavioral/state.py)  
**Related:**  
- Can be used in a [Flyweight](/docs/structural_patterns/structural_patterns.md#flyweight) to determine how a State objects can be shared
- Typically a [Singleton](/docs/creational_patterns/creational_patterns.md#singleton)

## Strategy  
**Alias:** `Policy`  
**Intent:** Vary algorithms at runtime by making them interchangable  
**Components:** `Strategy`, `ConcreteStrategy`, `Context`  
**Implementation:** [strategy.py](/src/patterns/behavioral/strategy.py)  
**Related:**  
- Typically make good [Flyweight](/docs/structural_patterns/structural_patterns.md#flyweight)(s)

## Template Method  
**Intent:** Alter pre-structured, algorithm steps via subclass overrides  
**Components:** `AbstractClass`, `ConcreteClass`  
**Implementation:** [template_method.py](/src/patterns/behavioral/template_method.py)  
**Related:**  
- Typically call [Factory Method](/docs/creational_patterns/creational_patterns.md#factory-method)(s)
- Similar to [Strategy](/docs/behavioral_patterns/behavioral_patterns.md#strategy), except vary only part of a algorithm, where Strategies try to cary it entirely

## Visitor  
**Intent:** Form new algorithms by decoupling algorithms and the objects the operate on  
**Components:** `Visitor`, `ConcreteVisitor`, `Element`, `ConcreteElement`, `ObjectStructure`  
**Implementation:** [visitor.py](/src/patterns/behavioral/visitor.py)  
**Related:**  
- Can be used to apply operations over a [Composite](/docs/structural_patterns/structural_patterns.md#composite)'s strucuture
- Can be applied to to complete the interpretation in an [Interpreter](/docs/behavioral_patterns/behavioral_patterns.md#interpreter)
