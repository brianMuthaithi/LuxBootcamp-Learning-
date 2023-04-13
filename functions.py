import math
import re

from numpy import average
# Defining a function
def items(list):
    list.append([2, 4, 7, 8])
    print('Values are inside the function', list)
    return
laini = [63, 51, 890]
items(laini)

# Default arguments
def locall(name):
    print(name)
    return
locall("Brayo")

# Importing a library
a = 5
b = 20
print(a + b)

llid = [54, 54,54]
print("the sum is:", sum(llid))
a = average(llid)
print(a)


def simple_math(x, y, z):
    total = (x + y) * z
    print(total)
    return total
simple_math(x=4, y=6, z=4)

def f():
    a = 5
    b = 6
    c = 7
    return a, b, c                      # Return a tuple
    return {'a': a, 'b': b, 'c': c}     # Return a dict

# Basic data cleaning
states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south carolina##', 'West virginia?']
def cleaning_data(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)

        return print(result)
cleaning_data(states)

def apply_to_list(some_list):
    for x in some_list:
        f = x ** 2
        print(f)
    return f
apply_to_list(some_list=[2,4,6,8]) 


names = ['foo', 'card', 'bar', 'aaaa', 'abab']
names.sort()   
print(names)    

def sum(x, y):
    return x + y
add_five = lambda y: sum(5, y)
print(add_five)

