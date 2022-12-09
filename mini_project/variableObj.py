# ##### <OBJ as Variables> #####

# class car:
#     color = None
    
# def change_color(car=car(), color=None):
#     car.color = color
    
# car1 = car()
# car2 = car()
# print('\n BEFORE: ')
# print(f'Car1: {car1.color}   Car2: {car2.color}')

# change_color(car1,'red')
# # change_color(car2,'blue')
# # print('AFTER:')
# print(f'Car1: {car1.color}   Car2: {car2.color} \n')

##### <FUNC as Variables/Higher Order Functions> #####

# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(chosen_func): 
    # storing the function in a variable 
    greeting = chosen_func("print statment created by a function passed as an argument.") 
    print(greeting)
  
greet(shout) 
greet(whisper) 