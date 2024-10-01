class Person:
    def __init__(self, name, age):  # Constructor method
        self.name = name            # Initialize instance variable 'name'
        self.age = age              # Initialize instance variable 'age'

# Creating an instance of Person
a = Person("Esha", 24)

# Accessing the instance variables
print(a.name, a.age)  # Output: Esha 24
