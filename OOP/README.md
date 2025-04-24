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

Attributes are created inside a class definition. We do this by joining an arbitrary name to the instance name, separated by a dot.

* Proper to define a method inside a class:
    - We define a method inside of a class definiton.
    - The first parameter is used as a reference to the calling instance (it is called 'self').

'Self' is not a Python keyword, just a naming convention.
* Self parameter is a reference to the instance of a class. 
* It is used to access variables and methods associated with the current object. 
* It differentiates between instance attributes and local variables.

In the above example, self.name and self.age refer to the instance variables.

* __init__ is a method which is immediately and automatically called after an instance has been created.
* It is one of the magic methods. It initializes an instance. There is no explicit constructor or destructor method in Python. 
* __init__ could be placed anywhere in the class, but it is a good idea to be the first method of a class. Refer to the example above.

# Data Abstraction, Data Encapsulation, and Informating Hiding

*Encapsulation* is seen as the bundling of the data with the methods that operate on that data.
Information Hiding is the principle that some internal information or data is hidden, so that it cannot be automatically changed.
Data Encapsulation via methods doesn't necessarily mean that the data is hidden. We might be capable of accessing and seeing the data, but using the methods is recommended.

Data Abstraction = Data Encapsulation + Information Hiding

*Encapsulation* is often accomplished by providing two kinds of methods for attributes : Getter and Setter Methods.

The methods for retrieving or accessing the values of attributes are called *getter* methods.
Getter methods do not change the values of attributes, they just return the values.

The methods used for *changing* the values of attributes are called *setter* methods.
Example:

```
class Robot:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am: ", self.name)
        else:
            print("Hi, I am a robot without a name.")

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name
    
x = Robot()
x.set_name("John")
x.say_hi()

y = Robot()
y.set_name(x.get_name())
print(y.get_name())
```

# __str__ and __repr__ - Methods

__str__ : is a special method used to define the string representation of an object. It provides human readable string representation of an object.
__repr__ is also quite similar, as it also produces a string representation.

If you apply str or repr to an object, Python is looking for a corresponding method __str__ or __repr__ in the class definition.
If the method does exist, it will be called (common sense!)

* When to use __repr__ and when __str__:
    - __str__ is always the right choice, if the output should be for the end user, or if it should be nicely printed.
    - __repr__ is used for internal representation of the object. If possible, the output of __repr__ should be a string which can be parsed by the python interpreter.

# Public, Protected, and Private Attributes

* Private Attributes should only be used inside of the class definition itself.
* Protected (restricted) Attributes may be used, but only under certain conditions.
* Public Attributes can and should be freely used.

* If we prefix an attribute name with a leading underscore, it marks the attribute as protected.
* If we prefix an attribute name with two leading underscores, the attribute is now inaccessible and invisible from outside.

```
class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
```
