#Example of hierarchical inheritance

class Parent:
    def __init__(self) -> None:
        pass

    def printName(self):
        print("My name is .. oops there is no name variable")

class Child1(Parent):
    def __init__(self) -> None:
        pass

    def printName(self,name):
        print("my name is {0}".format(name))

class Child2(Parent):
    def __init__(self) -> None:
        pass

    def printName(self):
        print("my name is Child2")

class Child3(Parent):
    def __init__(self) -> None:
        pass

Auro = Child1()
Auro.printName('Lubu')

Subho = Child2()
Subho.printName()

Pagal = Child3()
Pagal.printName()# uses Parent's printName method
