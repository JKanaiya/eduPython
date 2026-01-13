# Python script to demonstrate OOP concepts of Data hiding, Overloading (simulation) and overriding

# Define an animal class
class Animal:
    def __init__(self, name, age):
        self._name = name # Protected by convention
        self.__age = age # Private (name mangled to _Animal__age)

    def get_private_age(self):
        return self.__age # Access the private variable __age via a getter

    def speak(self):
        return f"{self._name} makes a sound"

    def make_sound(self, *args): # Simulate overloading with *args
        base_sound = self.speak()
        if not args:
            return base_sound
        elif len(args) == 1 and isinstance(args[0], (int, float)):
            volume = args[0]
            return f"{self._name} says {base_sound} at volume {volume}"
        else:
            extras = ', '.join(str(arg) for arg in args)
            return f"{base_sound} with {extras}"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self): # Overrid the Animal's (parent class) speak method
        return f"{self._name} baks 'WOOF' loudly!"


# Instantiate a dog object and call the various methods
dog = Dog("jimmy", 20)
print(dog.speak()) # Overriding the animals speak sound
print(dog.make_sound(8)) # Overloading with volume argument
print(dog.make_sound(12, "with toy", "excited")) # with extras
print(f"{dog._name}'s age is {dog.get_private_age()} years") # Data hiding: access via a getter