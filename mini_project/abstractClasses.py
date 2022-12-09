#Prevents a user from creating an object of that class
# + compels a user to override methods in a child class

#Abstract class = a class which contains one or more abstract mtehtods
#Abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod #abc -> abstact base class

class vechile(ABC): #This is the abstract class
    @abstractmethod #this is now an abstract method in the abstract class
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class car(vechile):
    
    def go(self):
        print('You drive the car')
        
    def stop(self):
        print('stopped car')

class motor(vechile):
    def go(self):
        print('Your drive the motor') 
    
    def stop(self):
        print('stopped mot')

# v = vechile()
c = car()
m = motor()

# v.go()
c.go()
m.go()
        