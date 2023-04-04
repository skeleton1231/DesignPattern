The **Builder pattern** is a creational design pattern that aims to separate the construction of a complex object from its representation. By doing so, the same construction process can be used to create different representations of the object. This pattern is useful when you need to separate the specification of an object from its actual representation, which is generally required for abstraction.

The example you mentioned uses an abstract base class for a building. The initializer (i.e., the `__init__` method) specifies the steps needed to construct the object, while the concrete subclasses implement these steps. This approach allows for the creation of objects from the same family using the same construction process, but with different representations.

In some programming languages, like C++, more complex arrangements may be necessary to achieve the same behavior. However, in Python, the technique shown in the example is usually sufficient.

```
from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

class ConcreteBuilder1(Builder):
    def build_part_a(self):
        print("Part A1 created")

    def build_part_b(self):
        print("Part B1 created")

class ConcreteBuilder2(Builder):
    def build_part_a(self):
        print("Part A2 created")

    def build_part_b(self):
        print("Part B2 created")

class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.build_part_a()
        self._builder.build_part_b()

# Usage
builder1 = ConcreteBuilder1()
director1 = Director(builder1)
director1.construct()

builder2 = ConcreteBuilder2()
director2 = Director(builder2)
director2.construct()
```

In next example, we have an abstract SandwichBuilder class with methods to add bread, meat, vegetables, and condiments. We then create two concrete builder classes, VeggieSandwichBuilder and TurkeyClubSandwichBuilder, each implementing the abstract methods to build different types of sandwiches.

The SandwichMaker class is responsible for managing the sandwich construction process. It takes a builder instance as a parameter and calls the builder's methods to construct the sandwich. By changing the builder instance used by the sandwich maker, we can create different types of sandwiches using the same construction process.

This approach allows us to create new sandwich types easily by adding new concrete builder classes without having to modify the existing code.


```
from abc import ABC, abstractmethod

class SandwichBuilder(ABC):
    def __init__(self):
        self.sandwich = None

    def create_new_sandwich(self):
        self.sandwich = Sandwich()

    @abstractmethod
    def add_bread(self):
        pass

    @abstractmethod
    def add_meat(self):
        pass

    @abstractmethod
    def add_vegetables(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.bread = "Whole wheat"

    def add_meat(self):
        self.sandwich.meat = None

    def add_vegetables(self):
        self.sandwich.vegetables = ["Lettuce", "Tomato", "Cucumber"]

    def add_condiments(self):
        self.sandwich.condiments = ["Mustard", "Mayonnaise"]

class TurkeyClubSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.bread = "White"

    def add_meat(self):
        self.sandwich.meat = "Turkey"

    def add_vegetables(self):
        self.sandwich.vegetables = ["Lettuce", "Tomato"]

    def add_condiments(self):
        self.sandwich.condiments = ["Mayonnaise"]

class Sandwich:
    def __init__(self):
        self.bread = None
        self.meat = None
        self.vegetables = None
        self.condiments = None

    def __str__(self):
        return f"Bread: {self.bread}, Meat: {self.meat}, Vegetables: {self.vegetables}, Condiments: {self.condiments}"

class SandwichMaker:
    def __init__(self, builder):
        self.builder = builder

    def prepare_sandwich(self):
        self.builder.create_new_sandwich()
        self.builder.add_bread()
        self.builder.add_meat()
        self.builder.add_vegetables()
        self.builder.add_condiments()
        return self.builder.sandwich

# Usage
veggie_builder = VeggieSandwichBuilder()
sandwich_maker = SandwichMaker(veggie_builder)
veggie_sandwich = sandwich_maker.prepare_sandwich()
print(veggie_sandwich)

turkey_club_builder = TurkeyClubSandwichBuilder()
sandwich_maker.builder = turkey_club_builder
turkey_club_sandwich = sandwich_maker.prepare_sandwich()
print(turkey_club_sandwich)
```