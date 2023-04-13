class bike:
    name = ''
    color = ''
    max_speed = ''
    height = ''

bike1 = bike()
bike1.name = 'Black Mamba'
bike1.color = 'Yellow'
bike1.max_speed = '120kph'
print(bike1.max_speed)


class room:
    length = ''
    width = ''
    
    def calc_area(self):
        area = self.length * self.width
        print('Area of the room: ', area)

staffroom = room()
staffroom.length = 50
staffroom.width = 30
staffroom.calc_area()



class bike:
    def __init__(self, name):
        self.name = name
bike1 = bike("Redbull")
print(bike1.name)



class Dog:
    animal = 'dog'

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    
    def bark(self):
        print('WOOF! WOOF! WOOF!')
    
bosco = Dog('Eurasian', 'White')
print('This is a', bosco.animal, ". It's breed is", bosco.breed, ". Its also", bosco.color)


class Girl:
    def __init__(self, name, body, color, net_worth):
        self.name = name
        self.body = body
        self.color = color
        self.net_worth = net_worth

    def take_out(self):
        if self.body == 'Petite' and self.net_worth >= 100000:
            print('Get taken out, bwoy!')
        else:
            print('RUN FROM BROKE WOMEN!')
    
alice = Girl('Alice', 'Petite', 'Lightskin', 25000)
mary = Girl('Mary', 'Skinny', 'Lightskin', 60000)
atticas = Girl('IDK', 'Petite', 'Dark', 200000)
atticas.take_out()
alice.take_out()
mary.take_out()


phones = ['RedMi', 'Samsung', 'Google Pixel', 'Oppo', 'Nokia', 'OnePlus']
class phone:
    def __init__(self, RAM, chipset, battery, price):
        self.RAM = RAM
        self.chipset = chipset
        self.battery = battery
        self.price = price
    
    def buy(self):
        for phone in phones:
            if self.chipset == 'Snapdragon' and self.RAM >= 6 and self.battery >= 4500:
                print("It's a good phone. Buy it!")
            else:
                print('Not your cup of tea')
    
my_phone = phone(8, 'Snapdragon', 5000, 24000)
my_phone.buy()






