#THE FOR LOOP

fruits = ["mangoes", "oranges", "grapes"]
for fruit in fruits:
   print(fruit)

for letter in 'fruits':
   print(letter)

for letter in 'fruits':
   print(letter)


# USING ELSE WITH FOR LOOP
num = []
for num in range(10, 20):
    for i in range(2, num):
        if num%i == 0:
            x = num/i
            print(num, i, x)
            break
        else:
            print(num)
            break