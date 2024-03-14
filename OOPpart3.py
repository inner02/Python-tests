# Part 3
class Bird:
    def __init__(self, species):
        self.species = species

    def fly(self):
        print(f"{self.species} is flying.")

class Owl(Bird):
    def __init__(self):
        super().__init__("Owl")

    def hoot(self):
        print("Hoot hoot!")

class Dodo(Bird):
    def __init__(self):
        super().__init__("Dodo")

    def extinct(self):
        print("Dodo is extinct.")

# Example usage
owl = Owl()
owl.fly()
owl.hoot()

dodo = Dodo()
dodo.extinct()
