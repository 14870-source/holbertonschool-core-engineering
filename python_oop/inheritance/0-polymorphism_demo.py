#!/usr/bin/env python3
"""Demonstrate inheritance and polymorphism."""


class Animal:
    """Represent a basic animal."""

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog."""

    def speak(self):
        """Return the sound made by a dog."""
        return "Woof"


class Cat(Animal):
    """Represent a cat."""

    def speak(self):
        """Return the sound made by a cat."""
        return "Meow"


dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
