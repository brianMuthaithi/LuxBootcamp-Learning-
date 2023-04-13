#-------------If-else---------------
james = 40
if james != 30:
    print("James isn't 30yrs old")
else:
    print("James is 30yrs old")

#------------if-elif----------------
marks = 57
if marks >= 80:
    print("A")
elif marks >= 75:
    print("A-")
elif marks >= 70:
    print("B+")
elif marks >= 65:
    print("B")
elif marks >= 60:
    print("B-")
elif marks >= 55:
    print("C+")
elif marks >= 50:
    print("C")
elif marks >= 45:
    print("C-")
elif marks >= 40:
    print("D+")
else:
    print("FAIL!")

#----------------Get external input----------
# salary = int(input("Enter your Gross Salary(USD): "))
# if salary >= 1000000:
#     print("Upper Class")
# elif salary >= 500000:
#     print("Middle Class")
# elif salary >= 250000:
#     print("Lower Class")
# else:
#     print("The Poors")

# name = str(input("What is your name: "))
# if len(name) >= 6:
#     print("Peleka uluhya mbali")
# else:
#     print("Welcome home my child")

#---------------------------------------LOOPS-----------------------------------------------------
#---------------------while loop-------------------------
x = 0
while x < 5:
    print(x, "is less than 5")
    x += 1

age = 13
while age <= 19:
    print(age, "is a teenager")
    age += 1
 
#--------------------for loop-----------------------------
shoes = ["Addidas", "Jordans", "Nike", "Reebok", "Yeezy", "Balenciaga", "And1", "Puma"]
for shoe in shoes:
    print(shoe, " has ", len(shoe), " letters.")


grades = [50, 65, 77, 48, 63]
for grade in grades:
    if grade >= 70:
        print(grade, "= A")
    elif grade >= 60:
        print(grade, "= B")
    elif grade >= 50:
        print(grade, "= C")
    elif grade >= 40:
        print(grade, "= D")
    else:
        print("FAIL!")

for x in range(10):
    if x % 2 == 0:
        print(x)
    else:
        x += 1


# stadiums = {
#     "Arsenal": "Emirates",
#     "ManUnited": "Old Trafford",
#     "ManCity": "Etihad",
#     "Chelsea": "Stamford Bridge"
# }
# for stadium in stadiums:
#     if len(stadiums) <= 6:
#         new_stadiums = stadiums.update({"Tottenham": "White Hart Lane", "Liverpool": "Anfield"})
#         print(new_stadiums)
#     else:
#         print("No stadiums")


