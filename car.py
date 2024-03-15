class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

car1 = Car("Toyota", "Camry", 2022)

print("Initial Make:", car1.get_make())
print("Initial Model:", car1.get_model())
print("Initial Year:", car1.get_year())

car1.set_make("Honda")
car1.set_model("Accord")
car1.set_year(2023)

print("\nUpdated Make:", car1.get_make())
print("Updated Model:", car1.get_model())
print("Updated Year:", car1.get_year())
