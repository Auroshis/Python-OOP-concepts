# example of polymorphism - > same method name that can be used differently under different circumstances
# Python does not suport method overloading but does allow method overriding
class A:
    def __init__(self) -> None:
        pass

    def poly_method(self):
        print("poly method without params")
    
    def poly_method(self, value):
        print("poly method with value", value)

obj = A()
# obj.poly_method() # not working function overloading
obj.poly_method('param_value')

