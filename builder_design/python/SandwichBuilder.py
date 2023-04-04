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
