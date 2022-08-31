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
