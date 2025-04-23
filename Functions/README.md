# Introduction

It is a fundamental concept in programming. In the most general sense, a function is a structuring element in programming languages to group a bunch of statements so they can be utilized in a program more than once.

Functions are known under various names in programming languages, for example, as subroutines, routines, procedures, methods, or subprograms.

# Functions in Python

A function in Python starts with a 'def' keyword. The general syntax looks like this:

```
def function_name(parameters):
    statements (the function body)
```

The parameters consists of none or more parameters. Parameters are called 'Arguments', if the function is called. The function body consists of indented statements. The function body gets executed every time the function is called.

# Default Arguments

When we define a Python function, we can set a default value to a parameter. If the function is called without the argument, this default value will be assigned to the parameter. Hence, they are optional.
Demonstration of this behavior is as follows:

```
def hello(name="everybody"):
    result = "Hello" + name

hello("Rob")
hello()
```
```
Output:
Hello Rob
Hello everybody
```

One interesting scenario arises from the way Python treats the default arguments if it is a mutable object.
Passing mutable lists or dictionaries as default arguments to a function can have unforseen effects. 
Programmers can expect the program to create a new list or dictionary every time the function is called after using lists or dictionaries as default arguments, but this is not what actually happens.
Default values are created exactly once, at the compile time.


# Return Values

Function bodies can contain one or more return statements. They can be situated anywhere in the function body. A return statement ends the execution of the function call and returns the results, 
i.e. the value of the expression following the return keyword, to the caller. If the return statement is without an expression, 'None' is returned. If there is no return statement in the function code, the function ends, when the control flow reaches the end of the function body and the value 'None' will be returned.

# Local and Global Variables

Variable names are by default local to the function.
Global keyword is used to make the variable global.

# Arbitrary Number of Parameters

What if we don't know the exact number of parameters we want in our function.
For that case, an asterisk is used in front of the last parameter name to denote it as a tuple reference. (Please do not mistake it for pointers in C)
Asterisk will unpack or singularize.

To pass an arbitrary number of keyword parameters to a function as a dictionary, we use double asterisk.

There is a clear difference between Parameter and Argument.
Parameters are inside functions or procedures, while arguments are used in procedure calls,
i.e. the values passed to the function at run-time.

# Call by Value and Call by Reference

Python's argument passing mechanism can be understood as call by object reference, where the behavior depends on the mutability of the objects being passed.

The *args and **kwargs are common idioms to allow an arbitrary number of arguments to functions. 
The *args will give positional arguments as a tuple.
The **kwargs will give all keyword arguments as a dictionary.
