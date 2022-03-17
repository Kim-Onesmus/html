# print(set('My name is mori and mori is my name'.split()))
# a = set(["Mori", "Keli", "Mbithi"])
# b = set(["Ann", "John", "Mbithi", "Mary"])
# print(a.intersection(b))    # attended both events a & b.
# print(b.symmetric_difference(a))    # attended only one event.
# print(a.difference(b))  # attended only one event.
# print(a.union(b))

# # list comprehension.
# foodList = ["mango", 'banana', 'avocado']
# mylist = [x for x in foodList if 'a' in x]
# print(mylist)

# # another example of list comprehension.
# students = ['Mori', 'Kim', 'Peninah', 'Trizah', 'Steve']
# scores = [75, 56, 74, 53]
# for name, scores in zip(students, scores):  # I learnt a new list comprehension today!! WOW!!
     # print('{} has scored {}.'.format(name, scores))

# dictionaries
# squares = {num: num**2 for num in range(10)}    # dictionary comprehension. Awesome!!
# print(squares)

# # lambda function
# x = lambda a, b: a*b
# print(x(2, 4))

# # Inheritance
# class Vehicle:
#     def __init__(self,  make, model, fuel="gas"):
#         self.make = make
#         self.model = model
#         self.fuel = fuel
#
#     def fuel_needs(self):
#         print(self.make, 'needs fuel.')
#
#
# class Car(Vehicle):
#     def __init__(self, make, model, fuel="gas"):
#         super().__init__(make, model, fuel)
#
#
# Car(make="Toyota", model="Thunderbird").fuel_needs()

# creating your own module and import the module
# import name
# print('His name was', name.name)

# import os module
# import os
# print(os.name)
# print(os.getlogin())    #print the user of this machine.

# from math import sqrt
# print(sqrt(100))
# from math import *
# print(sqrt(100))

# JSON
# import json
# d = {
#     'name': 'Mori Keli',
#     'age': 21,
#     'city': 'Nairobi',
#     'marital status(married)': True,
#     'children': ('ann', 'dan'),
#     'pets': None,
#     'cars': [{
#         "model": 'Ford Mustang'},
#         {"model": 'Porsche 911 Turbo S'
#     }]
# }
# y = json.dumps(d, indent=4, sort_keys=True)
# print(y)

# try and exceptions(Error handling)
# a = 6
# print(a)
# try:
#     print(b)    # NameError! if the error was not caught, the program would not run since b is undefined.
# except:
#     print('an error occurred!!')
#     # print(f"An error occurred")

# file handling
import os
print(os.getcwd())  # get current working directory(cwd)
