###Inheritance
Inheritance is when one thing is based on another thing. It's like when you make a new drawing and use the same colors as your previous drawing. In Python, we can do the same thing with classes.
Let's say we have a class called Animal. This class has some attributes and methods, like what sound the animal makes or how fast it can run. Now, let's say we want to create a new class called Dog. A dog is an animal, so we want to use the attributes and methods from the Animal class in our new Dog class.
This is where inheritance comes in. We can make our Dog class "inherit" from the Animal class. That means our Dog class will have all the same attributes and methods as the Animal class, but we can also add new attributes and methods that only apply to dogs.
Here's an example:
class Animal:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self):
        super().__init__("woof")

    def wag_tail(self):
        print("wagging tail")
In this example, we have two classes: Animal and Dog. The Dog class inherits from the Animal class using the parentheses in the class definition. This means that the Dog class has all the attributes and methods of the Animal class.
But the Dog class also has a new method called wag_tail, which the Animal class doesn't have. This is a special method only for dogs.
So when we create a new Dog object, we can call the make_sound method from the Animal class, and also the wag_tail method from the Dog class:
my_dog = Dog()
my_dog.make_sound()  # prints "woof"
my_dog.wag_tail()    # prints "wagging tail"
And that's it! Inheritance is a way to reuse code from one class in another class, so you don't have to write the same code over and over again. It's a really powerful tool in Python (and in programming in general).

###Multiple inheritance
So, you already know that inheritance allows us to create a new class based on an existing class, right? But what if we want to create a new class that combines attributes and methods from multiple existing classes? That's where multiple inheritance comes in!
Multiple inheritance is when a new class is created by inheriting from two or more existing classes. This allows us to combine the attributes and methods of all the parent classes in the new child class.
Let's say we have two classes called Animal and Pet. The Animal class has some general attributes and methods that apply to all animals, and the Pet class has some additional attributes and methods that apply specifically to pets, like their name or their owner.
Here's an example of how we can create a new class called Dog that inherits from both the Animal and Pet classes using multiple inheritance:

class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def get_owner(self):
        print(f"My owner is {self.owner}")

class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, "dog", "woof")
        Pet.__init__(self, name, owner)

    def wag_tail(self):
        print("wagging tail")
In this example, we have three classes: Animal, Pet, and Dog. The Dog class inherits from both the Animal and Pet classes using commas in the class definition.
When we create a new Dog object, it will have all the attributes and methods from both the Animal and Pet classes, as well as any new attributes and methods we add to the Dog class.
For example, we can create a new Dog object and call the make_sound method from the Animal class, the get_owner method from the Pet class, and the wag_tail method from the Dog class:

my_dog = Dog("Fido", "John")
my_dog.make_sound()  # prints "woof"
my_dog.get_owner()   # prints "My owner is John"
my_dog.wag_tail()    # prints "wagging tail"
And that's it! Multiple inheritance allows us to create new classes that inherit from multiple existing classes, giving us more flexibility and power when designing our programs.
