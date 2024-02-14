# Method overriding
'''
-> Allows you to redefine a method in a subclass or the derived class previously defined in its parent or the superclass

-> When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, 
   then the method in the subclass is said to override the method in the super-class.
'''

'''
class phone:

    def __init__(self,price,brand):
        self.price = price
        self.brand = brand

    def buy(self):
        print("Buying a phone")

class SmartPhone(phone):  # Inheriting properties of parent class

    def buy(self):
        print("Buying smartphone")

s = SmartPhone(2000,'Apple')

s.buy()
'''

# Method Overloading 

'''
-> Method overloading in simple terms refers to the ability to define multiple methods in a class with the same name but with different parameter lists

-> Unlike some other programming languages like Java and C++, Python doesn't natively support method overloading. 
   In Python, the latest defined method with a particular name overrides any previously defined method with the same name.

-> We can achieve similar behavior in Python using default parameter values or variable-length argument lists (e.g., *args and **kwargs)
   to handle different parameter scenarios within a single method.
'''

'''
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Create an instance of the class
math = MathOperations()

# Calling overloaded methods
#print(math.add(2, 3))       # Output: TypeError: add() missing 1 required positional argument: 'c'
print(math.add(2, 3, 4))    # Output: 9
'''

# Operator Overloading

'''
-> Example '+' sign used to add numbers as well as concatinatio of strings 

-> Ability to redefine the behavior of standard operators

-> Customize the behavior of operators for your objects, done using magic methods in python
'''

'''
a,b = 4,5
c = 'hello'
d = 'world'

add = a+b
print(add)

concat = c + d
print(concat)

'''