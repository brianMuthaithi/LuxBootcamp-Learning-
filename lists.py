# Lists

gen = range(10)
print(gen)
a = list(gen)
print(a)
a.append(11)            #Inserting an element
a.insert(4, 30)         #Inserting an element
print(a)
a.pop(4)
a.pop(10)               #Inverse of insert
print(a)
a.remove(5)             #Removing an element
print(a)
print(len(a))           #Prints length of the list
print(8 in a)           #Does a value exist in the list
print('add' in a)

# Concatenating
list1 = ['Bosco', 'Tusker', 'Rutawira', 'Shepherd', 'Chiwawa']
b = range(4)
list2 = list(b)
list3 = list1 + list2
print(list3)

list1.extend([1, 2, 3, 4])  # Faster method of concatenation
print(list1)

list1.sort()                # Sorting 
list1.sort(key=len)         # Sorting based on length of elements
print(list1)

# Binary search
import bisect               #bisect performs a binary search 

c = [1, 2, 2, 2, 3, 4, 7]
print(bisect.bisect(c, 5))  #bisect.bisect searches identifies where to insert a value in the sorted list 
bisect.insort(c, 5)         #Inserts the value in the list
print(c)

# Slicing
seq = [7,3,4,5,6,2,5,7,9]
slice1 = seq[3:6]              # Slices the sequence from pos. 3 to 5
print(slice1)
slice2 = seq[2:]               # Slice starts from element 2 to end
slice3 = seq[:4]               # Slice ends at element 4 fro the start
slice4 = seq[-3:]              # Slice starts at 3rd element from the end
print('slice2: ', slice2)
print('slice3: ', slice3)
print('slice4: ', slice4)
