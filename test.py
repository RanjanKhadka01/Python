# warlus operator -> :=

# happy = True
# print(happy)

# print(happy:=True)

# foods = list()
# while True:
#     food = input("What food do you like?")
#     if food == "quit":
#         break
#     foods.append(food)

# foods = list()
# while food := input("What food do you like?") != "quit":
#     foods.append(food)
#
# def hello():
#     print("Hello")
#
#
# hi = hello
# hello()
# hi()

# say = print
# say("Hi all")

# Higher order function = a function that either:
#                         1. accepts a function as an argument
#                           or
#                         2. returns a function
#                         (In Python, functions are also treated as objects)

# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
# hello(loud)
# hello(quiet)
#
# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend
#
#
# divide = divisor(2)
# print(divide(10))


# lambda Function

# lambda parameters:expression
#
# x = lambda a: a + 10
# print(x(5))
#
# multiply = lambda x,y,z:x*y*z
# print(multiply(2,2,2))
#
# full_name = lambda first_name, last_name:first_name+" "+last_name
# print(full_name("Ranjan", "Khadka"))

# sort() method = used with lists
# sort() function = used with iterables

# name = ['Ranjan', "Bidur", "Dhimal", "Anish", "Biplap"]
# name.sort(reverse=True)
# for i in name:
#     print(i)

# Tuple
# name=("Ranjan", "Gothey", "Vanjo")
# sorted_name = sorted(name, reverse=True)
# for i in sorted_name:
#     print(i)

# students = (("Ram", "F", 32),
#             ("Shyam", "A", 25),
#             ("Hari", "D", 23),
#             ("Mr.Krabs", "C", 30))
# grade = lambda grades: grades[1]
# shorted_students = sorted(students, key=grade, reverse=True)
# # students.sort(key=grade, reverse=True)
# for i in shorted_students:
#     print(i)

# map() = applies a function to each item in an iterable (list, tuple,etc)

# map(function, iterable)
#
# store = [("shirt", 20.00),
#          ("pant", 25.000),
#          ("jacket", 50.000),
#          ("socks", 10.000)]
#
# to_euros = lambda data: (data[0], data[1]*0.82)
#
# store_euros = list(map(to_euros, store))
# for i in store_euros:
#     print(i)

# Filter() = creates a collection of elements from an iterable for which a function returns true
# filter(function, iterable)

# friends = [("Ranjan", 22),
#            ("Dhimal", 23),
#            ("Gothey", 18),
#            ("Bidur", 17)]
#
# age = lambda data: data[1] >= 18
# drinking_age = list(filter(age, friends))
# for i in drinking_age:
#     print(i)


# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#           performs function on first two elements and repeats process until 1 value remains
# reduce(function, iterable)
# import functools
# letters = ["H", 'E', "L", 'L', "O"]
# word = functools.reduce(lambda x, y:x+y,letters)
# print(word)
#
# factorials = [5,4,3,2,1]
# results = functools.reduce(lambda x,y:x*y,factorials)
# print(results)

# list comprehension = a way to create a new list with less syntax
#                       can mimic certain lambda function, easier to read
#               list = [expression for items in iterable]
#               list = [expression for item in iterable if conditional]
#               list = [expression if/else for item in iterable]

# squares = [i*i for i in range(1,11)]
# print(squares)

# students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
# passed_student = list(filter(lambda x: x>=60, students))
# passed_student = [i for i in students if i >= 60]
# passed_student = [i if i >=60 else "Failed" for i in students]
# print(passed_student)

# dictionary comprehension = create dictionaries using expression
#                           can replace for loops and certain lambda function

# dictionary = {key: expression for (key, values) in iterable}

# cities_in_F = {'Kathmandu': 40, 'Bhaktapur': 50, 'Lalitpur':75, 'Biratnagar':100}
# cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
# print(cities_in_C)
#
# weather = {'Kathmandu': "Sunny", 'Bhaktapur': "Snowing", 'Lalitpur':"cloudy", 'Morang':"Sunny"}
# sunny_weather = {key: value for (key,value) in weather.items() if value =="Sunny"}
# print(sunny_weather)

# zip(*iterables) = aggregate elements from two or more iterables (lists, tuples, sets, etc)
#                   creates a zip object with paired elements stored in tuples for each element)

# user_name = ['Ranjan', "Khadka", "admin"]
# password = ("password1", 'abc123', "admin")
# last_login = ["1/1/2022", "1/2/2022", "2/2/2021"]
#
# user = zip(user_name, password, last_login)
# print(type(user))
#
# for i in user:
#     print(i)


