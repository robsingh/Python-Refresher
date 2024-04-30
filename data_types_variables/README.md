# My experience
I have programmed in low-level programming languages such as C, C++ and when I started with Python, I realized that I already know enough about **Data Types and Variables**, but I was **wrong**. 
There is a difference in how Python and C deal with variables. There are integers, floating point numbers, strings and many more, but things are not the same as in C or C++. 

For example, if you have to use lists or associative arrays in C, you will have to construct the data type list or associative arrays from scratch! i.e. design memory structure and the allocation management. You will have to implement necessary search and access methods as well. We are going to read about it next. 

# Variables and Keywords in Python
There is no declaration of variables required in Python, which makes it quite easy. If there is a need for a variable, you think of a descriptive name and start using it! 

Fun fact: Not only the value of a variable may change during program execution, but the type as well. You can assign an integer value to a variable, use it as a integer for a while and later assign a string to the same variable. 

Python variables are references to objects, but the actual data is contained in the objects. 

A valid variable name can consist of uppercase letters "A" through "Z", the lowercase letter "a" through "z", the underscore and except for the first character, the digits 0 through 9. Python is based on Unicode so variable names and identifier name can additionally contain Unicode characters as well. 

Use help() in the iteractive shell to get list of Python keywords. Feel free to learn more about them and use them in your day to day programming! When I started with Python, I basically used to do this a lot and this has helped me to strengthen my basics of the language, not the programming fundamentals :D 

# More Information
Strings show a special effect. If both 'a' and 'b' are strings, 'a is b' checks if they have the same identity i.e. share the same memory location. If 'a is b' is True, then it follows that 'a==b' has to be True as well. Yet 'a==b' True doesn't imply that 'a is b' is True as well! Python doesn't automatically intern the string because it contains special characters. Python's string interning mechanism is generally limited to simple strings without special strings or whitespace. 


