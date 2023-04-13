# Sets  -----   They support mathematical set operations

a = {3, 4, 5, 6, 7}
b = {9, 5, 3, 2}
print(a | b)                            # Union of sets
print(a.union(b))
print(a & b)                            # Intersection of sets
print(a.intersection(b))
print(a.issubset(b))                    # Check for subsets
a.remove(3)                             # Remove an elemen from a set
print(a)


name_caps = []
strgs = ['car', 'bat', 'door', 'pillar', 'puta']
for word in strgs:
    if len(word) >= 4:
        word =  word.upper()
        name_caps.append(word)
        print(name_caps)
    
    

all_data = [['john', 'emily', 'michael', 'mary', 'steven'],
            ['marta', 'juan', 'xavier', 'Natalie', 'pilar']]
niggaz = []
for names in all_data:
    for name in names:
        if name.count('a') >= 2:
            niggaz.append(name)
            print(niggaz)



flattened = []
some_tuples = [(2,3), (2,5,8), (7,1,6,0)]
for tup in some_tuples:
    for x in tup:
        flattened.append(x)
        print(flattened)            
