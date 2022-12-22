# example of multilevel inheritance
class GrandFather:
    def __init__(self, name) -> None:
        self.name = name
    
    def buy_land(self):
        print("{0} bought land".format(self.name))
    
class Father(GrandFather):
    def __init__(self, name, salary) -> None:
        self.income = salary
        super().__init__(name)
    
    def buy_house(self):
        print("{0} bought house with salary {1}".format(self.name, self.income))

class Son(Father):
    def __init__(self, name, salary, job) -> None:
        self.income = salary
        self.position = job
        super().__init__(name, salary)
    
    def buy_flat(self):
        print("{0} bought flat with salary {1} being a {2}".format(self.name, self.income, self.position))


Auroshis = Son('Auroshis', '8000$', 'Software Engineer')

# prints 'Auroshis bought land'
Auroshis.buy_land()
# prints 'Auroshis bought house with salary 8000$'
Auroshis.buy_house()
# prints 'Auroshis bought flat with salary 8000$ being a Software Engineer'
Auroshis.buy_flat()