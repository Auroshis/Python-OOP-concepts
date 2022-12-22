# class method v/s static method
"""
class methods have access to class state(variables and methods) but static methods don't have access to class variables.
classmethod() function are used in factory design patterns where we want to call many functions with the class name rather than an object.
Static methods are used as utility functions along with class.
self is not passed to either classmethod or staticmethod methods.
"""

class A:
    b = 'joking'
    def __init__(self, a_var= 'haha') -> None:
        self.a = a_var
    
    @classmethod
    def testmethod(cls):
        cls.b = 'changes using cls'
        print(cls.b)
    
    @classmethod
    def factorymethod(cls, value):
        return cls(value)

    @staticmethod
    def testmethod2():
        # will not work as static method can't access class methods or variables
        print(b)
        b = 'changed in static'
        print(b)
    
    @staticmethod
    def stringmodifier(val):
        return val+val


# driver code
obj = A()
print(obj.b) # this will give 'joking' 
A.testmethod() #changes the state of b for the class and it's object
A.b = 'changes directly' # works the same as above
print(obj.b) # prints 'changes directly' if the above line was not there it would have printed 'changes using cls'
obj.b = 'changed using object' # this changes the values of b but only for the object
print(A.b) # print 'changes directly' as it was the last value assigned using the class
obj2 = A.factorymethod('nothing') # creates a class object using the factory method similar to constructor

A.stringmodifier('hello') # prints 'hellohello'
A.testmethod2() # error as b is not accessible inside the static method



