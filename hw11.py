class Vehicle():
    def __init__(self, make, model, year, mileage, price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
    def setMake(self, newMake):
        self.make = newMake
    def getMake(self):
        return self.make
    def setModel(self, newModel):
        self.model = newModel
    def getModel(self):
        return self.model
    def setYear(self, newYear):
        self.year = newYear
    def getYear(self):
        return self.year
    def setMileage(self, newMileage):
        self.mileage = newMileage
    def getMileage(self):
        return self.mileage
    def setPrice(self, newPrice):
        self.price = newPrice
    def getPrice(self):
        return self.price
    def display(self):
        print('Make:', self.make)
        print('Year:', self.year)
        print('Model:', self.model)
        print('Miles:', self.mileage)
        print('Price:', self.price)

class Car(Vehicle):
    def __init__(self, make='', model='', year=0, mileage=0, price=0, doorNum=0):
        super().__init__(make, model, year, mileage, price)
        self.doorNum = doorNum
    def setDoorNum(self, newDoorNum):
        self.doorNum = newDoorNum
    def getDoorNum(self):
        return self.doorNum
    def display(self):
        super().display()
        print('Number of doors:',self.doorNum)

class Truck(Vehicle):
    def __init__(self, make='', model='', year=0, mileage=0, price=0, driveType=''):
        super().__init__(make, model, year, mileage, price)
        self.driveType = driveType
    def setDriveType(self, newDriveType):
        self.driveType = newDriveType
    def getDriveType(self):
        return self.driveType
    def display(self):
        super().display()
        print('Drive type:',self.driveType)

class SUV(Vehicle):
    def __init__(self, make='', model='', year=0, mileage=0, price=0, passengerCapacity=0):
        super().__init__(make, model, year, mileage, price)
        self.passengerCapacity = passengerCapacity
    def setPassengerCapacity(self, newPassengerCapacity):
        self.passengerCapacity = newPassengerCapacity
    def getPassengerCapacity(self):
        return self.passengerCapacity
    def display(self):
        super().display()
        print('Passenger capacity:',self.passengerCapacity)

class Inventory():
    def __init__(self, vList=[]):
        self.vList = vList
    def addVehicle(self, vehicle):
        self.vList.append(vehicle)
    def display(self):
        for i in self.vList:
            i.display()
            print('\n\n')

def main():
    done = False
    x = Inventory()
    while not done:
        vType = input('Enter vehicle type: ')
        vType = vType.upper()
        make = input('Enter vehicle make: ')
        model = input('Enter vehicle model: ')
        year = input('Enter vehicle year: ')
        mileage = input('Enter vehicle mileage: ')
        price = input('Enter vehicle price: ')
        if vType == 'CAR':
            doorNum = input('Enter number of doors: ')
            car = Car(make, model, year, mileage, price, doorNum)
            x.addVehicle(car)
        elif vType == 'TRUCK':
            driveType = input('Enter drive type: ')
            truck = Truck(make, model, year, mileage, price, driveType)
            x.addVehicle(truck)
        elif vType == 'SUV':
            passengerCapacity = input('Enter passenger capacity: ')
            suv = SUV(make, model, year, mileage, price, passengerCapacity)
            x.addVehicle(suv)
        goOn = input('Add another vehicle? (y/n): ')
        if goOn is 'y':
            done = False
        else:
            done = True
            print('\n\n')
    x.display()
