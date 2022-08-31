# class Animal:
#     alive = True
#
#     def eat(self):
#         print("The animal is eating")
#
#     def sleep(self):
#         print("The animal is sleeping")
#
#
# class Rabbit(Animal):
#     def run(self):
#         print("Rabbit is running")
#
#
# class Fish(Animal):
#     def swim(self):
#         print("Fish is swimming")
#
#
# class Dog(Animal):
#     def bark(self):  # adding own method
#         print("Dog is barking")
#
#
# rabbit = Rabbit()
# fish = Fish()
# dog = Dog()
#
# # print(rabbit.alive)
# # fish.eat()
# # dog.sleep()
# rabbit.run()
# fish.swim()
# dog.bark()


# Multi_level inheritance
# class Organism:
#     alive = True
#
#
# class Animal(Organism):
#     def eat(self):
#         print("Animal is eating")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
#
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()

# Multiple Inheritance
# class Prey:
#     def flee(self):
#         print("This animal flees")
#
#
# class Predator:
#     def hunt(self):
#         print("This animal is hunting")
#
#
# class Rabbit(Prey):
#     pass
#
#
# class Hawk(Predator):
#     pass
#
#
# class Fish(Prey, Predator):
#     pass
#
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.hunt()
# fish.flee()


# Method overriding ->
# class Animal:
#     def eat(self):
#         print("Animal is eating")
#
#
# class Rabbit(Animal):
#     def eat(self):
#         print("Rabbit is eating carrot")
#
#
# rabbit = Rabbit()
# rabbit.eat()

# Method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self
#
# class Car:
#
#     def trun_on(self):
#         print("Trun on the engine first")
#         return self
#
#     def drive(self):
#         print("Drive the car")
#         return self
#
#     def brake(self):
#         print("Step on the brake")
#         return self
#
#     def trun_off(self):
#         print("Trun off the engine")
#         return self
#
# car = Car()
# car.trun_on().drive().brake().trun_off()

# Super() = Function used to give access ti the methods of a parent class.
#           Returns a temporary object of a parent class when used
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#
# class Square(Rectangle):
#     def __init__(self, length, width):
#         super().__init__(length, width)
#
#     def area(self):
#         return self.length * self.width
#
#
# class Cube(Rectangle):
#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height
#
#     def volume(self):
#         return self.length * self.width * self.height
#
#
# # rect = Rectangle()
# sqr = Square(5, 5)
# cube = Cube(5, 5, 5)
#
# print(sqr.area())
# print(cube.volume())

# Abstract class

# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
#
#
# class Motorcycle(Vehicle):
#     def go(self):
#         print("Let's Goo by motorcycle")
#
#     def stop(self):
#         pass
#
#
# class Car(Vehicle):
#     def go(self):
#         print("Let's go by Car")
#
#     def stop(self):
#         pass
#

# motorcycle = Motorcycle()
# car = Car()
#
# motorcycle.go()
# car.go()


# Pass object as argument
# class Car:
#     color = None
#
#
# def change_color(vehicle, color):
#     vehicle.color = color
#
#
# car_1 = Car()
# car_2 = Car()
#
# change_color(car_1, "Red")
#
# print(car_1.color)
# print(car_2.color)

# Duck Typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like duck, then it must be a duck"

# class Duck:
#
#     def walk(self):
#         print("This duck is walking")
#
#     def talk(self):
#         print("This duck is qwacking")
#
# class Chicken:
#
#     def walk(self):
#         print("This chicken is walking")
#
# class Person():
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(duck)


