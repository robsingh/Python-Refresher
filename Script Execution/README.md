# Python Internals and Script Execution Basics

When I started my journey with Python, I somewhere read that Python language is an interpreted programming or a script language but I was wrong (partially)!
The truth is that Python is both an interpreted and a compiled language. But calling Python a compiled language would be slightly misleading. I will explain why. 

When you write a Python script and execute it, the Python interpreter does not directly execute the source code. Instead, it first parses the source code and then generate bytecode instructions from it. These bytecode instructions are then executed by the Python Virtual Machine (PVM), which is basically an interpreter for bytecode. So while Python is often referred as an interpreted language, the execution of Python code involves a compilation step where the source code is transformed into bytecode. We can use 'dis' module to disassemble the bytecode of any function. The bytecode will be produced but discarded when the program exits. If a Python script is imported as a module, the bytecode gets stored in the .pyc file. 

There is even a way of translating Python programs into Java byte code for the Java Virtual Machine (JVM) through JPython. 

Now the question arises, do we need to compile our Python scripts to make them faster or how can I compile them? 
The answer is - The compilation step is done at the runtime, meaning it happens when you run your Python script. Python is doing all the thinking for you automatically! How cool! 

What if someone wants to compile the script manually? 
Yes, it is possible with py_compile module. This module creates a compiled version of our byte code. 



