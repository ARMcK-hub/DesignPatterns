# Object Orieted Priciples

There are a few principles that are handy to remmeber when implemented OOP designs in which greatly add value to their implementations.

## DRY

**Don't Repeat Yourself.**

A good rule-of-thumb in general when writing code. You should look to modularize code where possible and implement reusable code in super classes where possible in order to make it available in subclasses.

## YAGNI 

**You Ain't Gonna Need It.**

Don't look to over engineer. It's easy to get caught up in implementing design patterns and complex object classes for every solution. You might find that the return-on-investment for time is not worth actually investing in heavily engineering code like this - as it's might not be intended to be extended, updates, or even used over a long period of time.

Look to invest time and energy where it is deemed effective, you can always make changes later if the scoped changes.

## SOLID

SOLID principles are vital to OOP. Here are some key notes of each of those principles:

- Single Responsibility
  - Each module/class/function should have one and only one reason to change
	- Do not make classes/function multipurpose
	-  Coupling
	  - Have multiple details interact with each other loosely, typically via interface, to keep from a change in one of them impacting the other
		- Keep high-level business logic separate from how things are completed, i.e. should not know how things are done specifically
	- Cohesion
	  - Functionality should be cohesive with others in its group, meaning that functionality that exists in a group that does not directly impact other functionality, should not be apart of the group, i.e. 2 functions that do not interact with similar variables
  - Example - Separating Logging and Persistence from a function
- Open-Closed
  - Software entities (classes, modules, functions) should be open for extension but closed for modification
	  - Modification can introduce downtime and bugs
		- Extension introduces maintainability
	- Balancing between abstraction and concreteness - dependent on future needs of an application
	  - Development Approach: Start concrete, modify towards abstraction if many changes start to occur
	- OCP Implementation Methods
	  - Parameterization
		- Inheritance
		- Composition / Injection
- Liskov Substitution
  - Subtypes must be substitutable for their base/Abstract types
	- Detecting LSP Violations
	  - Type checking a subtype
		- Null checks (effectively a null type check)
		- NotImplementedException in Concrete classes (incomplete interface implementation)
	- Fixing LSP Violations
	  - "Tell, Don’t Ask" for types
		- Null Object Patterns (implement a NullObjkect that shares the same interface as the standard interface)
		- Fully implement interfaces
- Interface Segregation
  - Clients (calling code) should not be forced to depend on methods they do not use
	- Prefer small, cohesive interfaces to large ones
	  - Large interfaces have more dependencies which means more
		  - Coupling
	    - Brittle code
			- Difficult testing
			- Difficult deployments
  - Detecting ISP violations 
	  - Large Interfaces
    - Partially implemented interfaces
  - Fixing ISP Violations
		- Break up large interfaces into smaller ones, then can compose an aggregated interface using inheritance
		- Possible to fix unreplaceable interfaces by using Adapter design pattern to implement your own interface
		- Clients should own and define their interfaces 
- Dependency Inversion
  - High-level models should not depend on low-level models, but abstractions. Abstractions should not depend on details, but vice versa.
  - Typical Low Level dependencies
		- Database
		- File system
		- Email
		- Web APIs
		- Configuration
		- Clock
  - Dependency Injection
		- Do not create your dependencies, but request them from executing / client code.
		- Preferred use
		- Can leverage IOC or DI Containers
