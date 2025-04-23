# Introduction

I am going to combine two topics in a single readme file.
First, I am going to talk about Packages in Python and later talk about Error Handling.

# Packages

Modules are files containing Pythong statements and definitions, like function and class definitions. The next goal is to learn how to bundle multiple modules together to form a package.

A package is basically a directory with Python files and a file with the name __init__.py
This means that every directory inside of a Python path, which contains a file named __init__.py, will be treated as a package by Python.

It is possible to put several modules into a Package.

When you import a package, the submodules are not automatically accessible. You can either import the submodules directly or add import statements to the __init__.py file.

If we import a package with the asterisk, we might expect to import this way all the submodules and subpackages, but this is not true (not 100%).

Python provides a mechanism to give an explicit index of the subpackages and modules of a packages, which shoud be imported. For this purpose, we can define a list named __all__. This list will be taken as the list of module and package names to be imported when from pakage import asterisk is encountered. This line must be added in the __init__.py file of the parent directory.


# Errors and Exception Handling

An exception is an error that happens during the execution of a program. Exception handling in Python is ~very~ similar to Java. While in Java exceptions are caught by catch clauses, in Python we have statements introduced by an "except" keyword.

```
while True:
    try:
        n = int(input("Please enter an integer))
        break
    except ValueError:
        print("Not a valid integer!")

```
In the above example, if no exception occurs during the execution, the execution will reach the break statement and the while loop will be left. 

You can also write exceptions on your own.

Meanwhile, there is another way to use it as well. The try statement can be followed by a finally clause. Finally clauses are called
clean-up or termination clauses, because they must be executed under all circumstances i.e. a "finally" clause is always executed regardless if an exception occurred in a try block or not.

The skeleton looks like:

```
try:
    pass
except:
    pass
finally:
    pass
```