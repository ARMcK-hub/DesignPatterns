Behavioral Pattern Overview
-----

## Chain of Responsibility  
**Intent:** Chain functionality together by pointing to the next object in line  
**Components:** `Handler`, `ConcreteHandler`, `Client`  
**Implementation:** [chain_of_responsibility.py](/src/patterns/creational/chain_of_responsibility.py)  
**Related:**  
- TODO

## Command  
**Alias:** `Action`, `Transaction`  
**Intent:** Parameterize commands for run-time, in-code management  
**Components:** `Command`, `ConcreteCommand`, `Client`, `Invoker`, `Receiver`  
**Implementation:** [command.py](/src/patterns/creational/command.py)  
**Related:**  
- TODO

## Interpreter  
**Intent:** Interpret a language into comprehensible grammar  
**Components:** `AbstractExpression`, `TerminalExpression`, `NonterminalExpression`, `Context`, `Client`  
**Implementation:** [interpreter.py](/src/patterns/creational/interpreter.py)  
**Related:**  
- TODO

## Iterator  
**Alias:** `Cursor`  
**Intent:** Access aggregate objects without exposing the underlying represenation  
**Components:** `Iterator`, `ConcreteIterator`, `Aggregator`, `ConcreteAggregator`  
**Implementation:** [iterator.py](/src/patterns/creational/iterator.py)  
**Related:**  
- TODO

## Mediator  
**Intent:** Reduce dependencies by restricting direct object communications to a mediator  
**Components:** `Mediator`, `ConcreteMediator`, `Colleague`(s)  
**Implementation:** [mediator.py](/src/patterns/creational/mediator.py)  
**Related:**  
- TODO

## Memento  
**Alias:** `Token`  
**Intent:** Restore an object later by storing it as a momento via a caregiver  
**Components:** `Momento`, `Originator`, `Caretaker`  
**Implementation:** [memento.py](/src/patterns/creational/memento.py)  
**Related:**  
- TODO

## Observer  
**Alias:** `Dependents`, `Publish-Subscribe`  
**Intent:** Notify multiple objects when the state of one changes  
**Components:** `Subject`, `Observer`, `ConcreteSubject`, `ConcreteObserver`  
**Implementation:** [observer.py](/src/patterns/creational/observer.py)  
**Related:**  
- TODO

## State  
**Alias:** `Objects for States`  
**Intent:** Allow an object to change its class via a handler  
**Components:** `Context`, `State`, `ConcreteStateSubclass`(s)  
**Implementation:** [state.py](/src/patterns/creational/state.py)  
**Related:**  
- TODO

## Strategy  
**Alias:** `Policy`  
**Intent:** Vary algorithms at runtime by making them interchangable  
**Components:** `Strategy`, `ConcreteStrategy`, `Context`  
**Implementation:** [strategy.py](/src/patterns/creational/strategy.py)  
**Related:**  
- TODO

## Template Method  
**Intent:** Alter pre-structured, algorithm steps via subclass overrides  
**Components:** `AbstractClass`, `ConcreteClass`  
**Implementation:** [template_method.py](/src/patterns/creational/template_method.py)  
**Related:**  
- TODO

## Visitor  
**Intent:** Form new algorithms by decoupling algorithms and the objects the operate on  
**Components:** `Visitor`, `ConcreteVisitor`, `Element`, `ConcreteElement`, `ObjectStructure`  
**Implementation:** [visitor.py](/src/patterns/creational/visitor.py)  
**Related:**  
- TODO
