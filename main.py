# print("Hello")

# variable
# first_name = 'Ranjan'
# last_name = "Khadka"
# fullname = first_name + " "+last_name
# print(fullname)
# print("Hello "+name)
# print(type(name))

# age = 23
# age += 1
# print("Your age is : " +str(age))

# height = 25.55
# print("Your height is : "+str(height)+"cm")
# print(type(height))

# human = True
# print("Are you a human :" +str(human))
# print(type(human))

# multiple assignment:
# name = "Ranjan"
# AGE = 22
# attractive = True
# name, AGE, attractive = "Ranjan", 22, True
# print(name)
# print(AGE)
# print(attractive)

# name = "ranjan Khadka"
# print(len(name))
# print(name.find("a"))
# print(name.capitalize())
# print(name.islower())
# print(name.replace("n", "a"))
# print(name.isalpha())
# print(name*3)

# Type casting

# x = 10  #int
# y = 2.11  #float
# z = "3"  #string
#
# x = str(x)
# y = str(y)
# z = str(z)
#
# print("The value of x is : " +str(x))
# print(y)
# print(z*3)

# user input in python
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height =float(input("Enter your height: "))
#
# print("Your name is "+name)
# print("You are is "+str(age)+ " years old")
# print("Your height is "+str(height)+ "cm")

# import math

# pi = -3.14
# x, y, z = 10, 20, 25
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(math.sqrt(20))
# print(pow(pi, 2))
# print(max(x, y, z))
# print(min(x, y, z))

# slicing = create a substring by extracting elements from another string
#   indexing[] or slice()
#   [start:stop:step]

# name = "Ranjan Khadka"
# first_name = name[:6]
# last_name = name[7:]
# funky_name = name[::2]
# reversed_name = name[::-1]
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
# slice = slice(7, -4)
# print(website1[slice])
# print(website2[slice])

# age = int(input("Enter your age: "))
# if age == 100:
#     print("You are a century old!")
# elif age >=18:
#     print("You are an adult!")
# elif age <0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")

# logical operator (and or not) = used to check if two or more conditional statement is true
# temp = int(input("Enter the temperature: "))
# if temp >=0 and temp <=25:
#     print("The temperatuer is good!")
# elif temp <0 or temp >25:
#     print("The temperature is bad!")

# name = None
# while not name:
#     name = input("Enter your name: ")
#
# print("Hello "+name)

# for i in range(10):
#     print(i)

# for i in range(50, 100, 2):
#     print(i)

# for i in "Ranjan Khadka":
#     print(i)

# import time
# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy new year!")
#
# rows = int(input("Enter the no. of rows: "))
# columns = int(input("Enter the no. of columns: "))
# symbol = input("Enter the symbol: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-789"
#
# for i in phone_number:
#     if i == '-':
#         continue
#     print(i, end="")

# for i in range(1, 20):
#     if i == 13:
#         pass
#     else:
#         print(i)

# list = used to store multiple items in a single variable
#
# name = ["Ranjan", "Sandesh", "Dhimal", "Bidur", "Gothey"]
# name[4] = "Roosan"
# # print(name[4])
# # name.append("Dallu")
# # name.sort()
# # name.pop()
# # name.insert(0, "Kalu")
#
# for i in name:
#     print(i)
# 2d list

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice-cream"]

# food = [drinks, dinner, dessert]
# print(food[1][2])
# for i in food:
#     print(i)

# tuple = collection which is ordered and unchangeable
#            used to group together related data

# student = ("Ranjan", "22", "male")
#
# print(student.count("Ranjan"))
# print(student.index("male"))
# for x in student:
#     print(x)
# if "Ranjan" in student:
#     print("Hi Ranjan")

# Set = collection of which is unordered, unindexed. No duplicate values

# utensils = {"fork", "spoon", "knief"}
# dishes = {"bowl", "plate", "cup", "knief"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_table = utensils.union(dishes)
# print(dishes)
# print(dishes.difference(utensils))
# for i in utensils:
# print(i)

# Dictionary = A unchangable, unordered collection of unique key:value pairs
#                Fast because they use hashing, allow us to access a value quickly

# captials = {'USA': 'Washington DC',
#             'Nepal': 'Kathmandu',
#             'China': 'Beijing',
#             'India': 'Moscow'}

# captials.update({'Germany': 'Berlin'})
# captials.pop('China')

# print(captials['Germany'])
# print(captials.get('Germany'))
# print(captials.keys())
# print(captials.values())
# print(captials.items())

# for key, value in captials.items():
#     print(key, value)

# index operator [] = gives access to a sequence's element (str,list,tuples)

# name = "ranjan Khadka!"

# if name[0].islower():
# name = name.capitalize()

# first_name = name[:6].upper()
# last_name = name[7:13].lower()
# last_character = name[-1]
#
# print(first_name)
# print(last_name)
# print(last_character)

# Function = a block of code which is executed only when it is called.
# def hello(first_name, last_name, age):
#     print("Hello " + first_name+" "+last_name)
#     print("You are "+str(age)+" years old")
#     print("Have a nice day..")


# name = "Ranjan Don"
# hello("Ranjan", "Khadka", 21)

# return statement = Function send Python values/objects back to the caller
#                    These values/objects are known as the function's return values

# def multiply(num1, num2):
# return num1*num2


# print(multiply(5, 19))

# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional
# def hello(first, middle, last):
# print("Hello "+first+" "+middle+" "+last)


# hello(first="Ranjan", last="Khadka", middle="Bahadur")

# Nasted function call
# num = input("Enter a number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a number: ")))))

# Scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped version of a variable can be created

# name = "Don"
#
#
# def display_name():
#     namee = "Ranjan"
#     print(namee)
#
#
# display_name()
# print(name)


# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

# def add(*agrs):
#     sum = 0
#     for i in agrs:
#         sum += i
#     return sum


# print(add(10, 20, 30))


# **kwargs = parameter that will pack all the arguments into a dictionary
#              useful so that a function can accept a varying amount of keyword arguments

# def hello(**kwargs):
#     # print("Hello "+kwargs['first']+" "+kwargs['last'])
#     print("Hello ", end=" ")
#     for key, value in kwargs.items():
#         print(value, end=" ")


# hello(tile="Mr.", first="Ranjan", middle="Bahadur", last="Khadka")

# str.format() = optional method that gives users
#               more control when displaying output

# animal = "cow"
# item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item))

# number = 1000

# print("The number pi is {:.3f}".format(number))
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number)) binary
# print("The number is {:o}".format(number))  octal
# print("The number is {:X}".format(number)) hexa
# print("The number is {:e}".format(number))

# import random
# x = random.randint(1, 12)
# y = random.random()
# print(y)

# myList = ['rock', 'paper', 'scissors']
# print(random.choice(myList))

# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
# random.shuffle(cards)
# print(cards)

# Exception
# try:
#     a = int(input("Enter a number to divide: "))
#     b = int(input("Enter a number to divide by: "))
#     result = a/b
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero")
# except ValueError as e:
#     print(e)
#     print("You can only divide by zero")
# except Exception as e:
#     print(e)
#     print("Something went wrong")
# else:
#     print(result)
# finally:
#     print("This will always execute")


# File Handling
# try:
#     with open('text.txt') as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)

# text = "Hi This is new file\n Practicing file handling"
# with open('test.txt', 'w') as file:
#     file.write(text)

# Copy a file
# import shutil
# shutil.copy('test.txt', 'text.txt')

# move a file
# import os
#
# source = "test.txt"
# destination = "C:\\Users\\Dell\\Desktop\\test.txt"
#
# try:
#     if os.path.exists(destination):
#         print("File already exists")
#     else:
#         os.replace(source, destination)
#         print(source+" was moved successfully")
# except FileNotFoundError as e:
#     print(e)

# Delete a file
# import os
# import shutil
#
# path = "folder"
# try:
    # os.remove(path) remove a file
    # os.rmdir(path) remove a empty folder
    # shutil.rmtree(path) remove a folder containing file
# except FileNotFoundError as e:
#     print(e)
# except PermissionError as e:
#     print(e)
# except OSError as e:
#     print(e)
# else:
#     print(path+" was deleted successfully")

# Module = a file containing python code. May conatin functions, classes, etc
# used with modular programming, which is to separate a program into parts

# import hello
#
# hello.hello()
# hello.bye()

# import hello as hey

# hey.hello()
# hey.bye()
#
# from hello import hello, bye
# hello()
# bye()

# help("modules")

# from car import Car
#
# car_1 = Car("Tesla", "Tesla", "2015", "black")
# car_1.drive()
# car_1.stop()