# Indexing and Slicing
fruits = ('oranges', 'grapes', 'apples')
print(fruits[3])    #Slicing an item from its position
print(fruits[0])
print(fruits[-1])
print(fruits[-2])

# Indexing
print(fruits.index('mango'))    #Gets the position of an item in a list
print(fruits.index('grape'))
print(fruits.index('orange'))


# TUPLES
fruits = ('oranges', 'grapes', 'apples')
print(fruits)
list = ("chair", "table", 97, 25, 1995)
print(list)
items = "bank", "school", "bus"
print(items)

# Accessing values in tuples
print(list[3])
print(items[2])

# Assigning new tuples
items_total = fruits + list
print(items_total)

# Deleting a tuple
commodities = ('apples', 24, 32, 'mangoes')
del commodities


# DICTIONARIES
name ={"Name": "Anthony", "Age":27, "School":"JKUAT"}
print(name)
print("The age of Anthony is", name['Age'])

#Updating a dictionary
name['Age'] = 52
name['School'] = 'UON'
print(name)

#Deleting elements in a dictionary
del name['Age']
print(name)

for key, value in name.items():
    print("{} is {}".format(key, value))



