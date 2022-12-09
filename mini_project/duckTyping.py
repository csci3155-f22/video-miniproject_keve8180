# Duck typing = is the concept where the class of an object is less important than the methods
#               class type is not chekced if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck: 
    
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print('This duck is quacking')

class Chicken:
    
    def talk(self):
        print('This chicken is clucking')
        
    def walk(self):
        print('This chicken is walking')

class Person:
    
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('You caught the criter!')
        
duck = Duck()
chicken = Chicken()
person = Person()

print()
person.catch(duck)
print()
person.catch(chicken)
