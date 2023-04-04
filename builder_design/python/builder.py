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
