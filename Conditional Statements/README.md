# Conditional Statements

Conditions usually in the form of 'if' statements are a fundamental concept in a programming language. There is hardly a way to program without branches in the code flow. (this is debatable!)

A decision must be made when the script or the program comes to a point where there is a selection of actions i.e. different calculations from which to choose. The instructions for decision making are called Conditional Statements. 

In programming, blocks are used to treat sets of statements as if they were a single statement. A block consists of one or more statements. A program can be considered as a block consisting of statements and other nested blocks. 

Code in Python can be structured with indents. It is useful to use indentations in C or C++ to increase the readability of the program. The compiler relies exclusively on the structures determined by the brackets. Python forces the programmer to use indentation that should be used anyway to write readable code. Moving the indentation level the way it is done in C or C++ will change the program logic. So it is important to consider that each line of a block in Python must be indented with the same number of spaces or tabs. 

# Syntax:

if condition:
    statement
    statement
elif condition:  #only checked if previous if or elif is false
    statement 
else:
    statement 
