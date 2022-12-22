# Example of multiple inheritance
class Papa:
    def __init__(self, name) -> None:
        self.name = name
    
    def resilience(self):
        print("{0} is resilient".format(self.name))
    
    def study(self):
        print("{0} studies Physics".format(self.name))

class Mama:
    def __init__(self, name) -> None:
        self.name = name
    
    def kindness(self):
        print("{0} is kind hearted".format(self.name))
    
    def study(self):
        print("{0} studies Mathematics".format(self.name))
    
class Son1(Mama, Papa):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def character(self):
        self.kindness()
        self.resilience()
    
    def studies(self):
        self.study()

class Daughter1(Papa, Mama):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def character(self):
        self.kindness()
        self.resilience()
    
    def studies(self):
        self.study()

son = Son1('Lubu')
son.character()
son.studies()

daughter = Daughter1("Lubu's imaginary sister")
daughter.character()
daughter.studies()