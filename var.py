name = "Virginia"
nickname = "cookie girl"
height = 1.9
bmi = 1.5
school = "JKUAT"
home = "Gate C"
phone_number = "0748662456"
business = "chef"
friends = ["Brian", "Keisha", "C.Rep", "Max", "hubby"]
units = ["Stats", "Complex", "Real"]
print(name, "whose an accomplice of ", friends[0], ", is in the same class as ", friends[2], ". She takes the units: ",
      units, ". Besides, she's a ", business, "and ", friends[0], "calls her ", nickname)


#---------------dictionaries--------------
dept = {"HR": "gaidi", "Finance" : "Linda", "Compliance": "Kevo", "Law": "Proctor"}
print(dept)
print(dept["Finance"])
print(dept.keys())
print(dept.values())
dept["Compliance"] = "Brian"
print(dept)
dept.update({"Sales": "Harper"})
print(dept)
dept["Finance"] = "Kenny"
print(dept)
dept.pop("Law")
print(dept)

#----------------lists------------------
subjects = ["Stats", "Complex Analysis", "T.O.H", "Systems", "Networks"]
local = ["Database", "O.R", "Matlab", "Web"]
all_units = subjects + local
print(all_units)
print(len(all_units))
all_units.append("Graphics")
print(all_units)
all_units[4] = "Stats 3"
print(all_units)
all_units.remove(all_units[5])
print(all_units)


#-------------tuples-----------------
tup_1 = (46, 90, 26, 21, 43, 12, 39)
tup_2 = (17, 38, 24, 18, 39, 87, 20)
print(tup_1 + tup_2)
print(tup_1[4] + tup_2[3])


#----------------------sets----------------------
set_a = {"Alexis", "Blake", "Fallon", "Axelrod"}
set_a.add("Hamilton")
print(set_a)



f1_cars = {
    "Redbull": "Max Verstappen",
    "Ferrari": "Charles Leclerc",
    "Mercedes": "Lewis Hamilton",
    "McLarren": "Lando Norris",
    "AlphaTauri": "Yuki Tsunoda",
    "Haas": "Kevin Magnussen",
    "Aston Martin": "Fernando Alonso",
    "Alfa Romeo": "Sebastian Vettel",
    "Williams": "Nicholas Latifi"
}
print(len(f1_cars))
print(f1_cars.keys())
f1_cars.update({"Honda": "Zhou Ganyu"})
print(f1_cars)








