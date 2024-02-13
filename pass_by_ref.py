# Aliasing --> Point to the same location in memory, so they edit the same list

# In python object of a class are also mutuable
# E.g : list dict and sets

#when you pass arguments to a function, there are two main ways in which these arguments can be handled:


'''
Call/Pass_by_reference:
-> In call by reference, a reference (or address) to the original argument is passed to the function
-> Changes made to the parameter inside the function affect the original value outside the function
'''
'''
def change(l):
    print(id(l))
    l.append(5)
    print(id(l))

L1 = [1,2,3,4]
print(id(L1))
print(L1)

change(L1)
print(L1)
'''

'''
Call/Pass_by_value:
-> In call by value, a copy of the argument's value is passed to the function.
-> Changes made to the parameter inside the function do not affect the original value outside the function.
'''
'''
def change(l):
    print(id(l))
    l.append(5)
    print(id(l))

L1 = [1,2,3,4]
print(id(L1))
print(L1)

change(L1[:]) # Cloning to make it immutable
print(L1)
'''