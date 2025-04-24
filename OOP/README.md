# Introduction

OOP is one of the most powerful tools of Python, but nevertheless we don't have to use it.
We can write powerful and efficient programs without it as well.

# General Idea of OOP

Imagine a library in New York. It has an organized collection of books, periodicals, newspapers, audiobooks, and so on. The analogy can be seen like this: The books and other publications, are like the data in an object-oriented program. Access to the books is restricted like access to the data is restricted in OOP. So, the data, - often called attributes, in such a setting can be seen as being hidden and protected by a shell, and it can only be accessed by special functions, usually called Methods in this context. Putting the data behind a shell is called Encapsulation.

## OOP in Python

Everything is a class in Python. Functions and methods are just like lists, integers or floats. Each of these are instances of their corresponding classes.

A good example is list class, which we have used quite often. The list class provides several methods to build lists, to access lists, change elements, or to remove elements.

# Class in Python

A class consists of two parts: the header and the body. 

For example, 
```
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Person: ({self.first_name}, {self.last_name}, {self.age})'

person = Person('John', 'Snow', 29)
print(person)
```

Above is a basic example of Class.
__str__ : is a special method used to define the string representation of an object. It provides human readable string representation of an object.

Attributes are created inside a class definition. We do this by joining an arbitrary name to the instance name, separated by a dot.

* Proper to define a method inside a class:
    - We define a method inside of a class definiton.
    - The first parameter is used as a reference to the calling instance (it is called 'self').

'Self' is not a Python keyword, just a naming convention.
* Self parameter is a reference to the instance of a class. 
* It is used to access variables and methods associated with the current object. 
* It differentiates between instance attributes and local variables.

In the above example, self.name and self.age refer to the instance variables.

__init__ is a method which is immediately and automatically called after an instance has been created. It is one of the magic methods. Basically, it initializes an instance. There is no explicit constructor or destructor method in Python. 
__init__ could be placed anywhere in the class, but it is a good idea to be the first method of a class. Refer to the example above.

