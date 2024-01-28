class Programmer:
    company = 'Microsoft'
    
    def __init__(self,name,product):
        self.name = name
        self.product = product
        '''
        Here, we define a class named Programmer. It has a class variable company set to 'Microsoft', indicating that all instances of this class will belong to Microsoft.

        The __init__ method is a special method called a constructor, which initializes the object with the provided values for name and product.
        '''
    
    def getInfo(self):
        print(f'In {self.company} Name {self.name} working on {self.product}')
        '''
        Methods are functions defined within a class and operate on the attributes of the class
        Here, getInfo is a method of the Programmer class. It prints information about the programmer, including the company, name, and the product they are working on. 
        The self parameter is a reference to the instance of the class calling the method.
        '''

'''
Objects are instances of a class. They are created using the class as a blueprint.
Here, harry, aymaan, and you are objects of the Programmer class.
'''

us = Programmer("Harry",'Skype')
aymaan = Programmer("aymaan",'Skype')
you = Programmer("you",'excel')

'''
Attributes:
Attributes are variables that store data. In OOP, attributes are associated with objects.
In the __init__ method, name and product are attributes of the Programmer class. 
They store information about the name of the programmer and the product they are working on.
'''

us.getInfo()
you.getInfo()
'''
Calling the function defined in the class
'''
