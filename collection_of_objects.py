class customer:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'I am {self.name} and I am {self.age}')

c1 = customer('A',12)  # Creating object
c2 = customer('B',13)  # Creating object
c3 = customer('C',14)  # Creating object

L = [c1,c2,c3]

for i in L:
    i.intro()