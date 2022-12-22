#single inheritance

class Parent:
    def __init__(self, val) -> None:
        #constructor returns None
        self.value = val

    def method1(self):
        print(self.value)

class Child(Parent):
    
    def method2(self):
        print('hello '+self.value)


#driver code
child = Child('Auroshis')
child.method2() # prints 'hello Auroshis')