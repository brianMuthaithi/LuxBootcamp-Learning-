# Dictionaries

d1 = {'a': 'value1', 'b': 'value2', 'c': 'value3'}
print(d1)
d1['d'] = 'Integer'             # Adding elements
print(d1)
print(d1['c'])                  # Printing specific elements
print('d' in d1)                # Checking if an element exists
del d1['d']                     # Deleting elements
print(d1)
print(list(d1.keys()))          # Outputs the dict's keys
print(list(d1.values()))        # Outputs the dict's values
d1.update({'3': 'baby', 'd': 'kuku', '5':'kach'})       # Merging dicts
print(d1)

# Mapping
students = ['scott', 'max', 'janet', 'bosco']
grades = {}
for student in students:
    grade = student[0]
    grades.setdefault(grade, []).append(student)
print(grades)


