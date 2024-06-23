# Control Structure in Python

Loops are a fundamental concept in programming. You will hardly find any programming language without a way to loop over the code. We are going to talk about 'while' loops here but let's rewind a little bit. 

There are 3 different kinds of loops: 
* Count Controlled loops - A loop structure which have a structure for repeating a loop a certain number of times. Python doesn't have this kind of loop. I am talking about the 'for' loop kind of structure from C language. 

* Condition Controlled loop - A loop will be repeated until a given condition changes i.e. changes to True to False or vice-versa. 

* Collection Controlled loop - It allows looping through the elements of a collection which can be array, list or other ordered sequence. 

Python supplies two different kinds of loops - the 'while' loop and the 'for' loop. 
The body of the loop will be executed as long as the mentioned condition yields True. With the help of a break statement, a while loop can be left prematurely. 
'Break' should not be confused with 'continue' statment. 'continue' STOPS the current iteration of the loop and starts the next iteration by checking the condition. If a loop is left by a break, the else part is not executed. 

The above mentioned behaviour is discussed [here](https://github.com/robsingh/python-refresher/blob/8721858ccb2172332faac3025a4b5d5698e31646/control_structure/examples.py#L1-L27).


# For Loop

A 'for' loop is used for iterating over a sequence(list, tuple, string etc) or other iterable objects. It is a fundamental concept in programming which allows us to repeat a block of code a specific number of times or iterate through the elements of a sequence.

The items of the sequence object are assigned one after the other to the loop variable; to be precise the variable points to the items. For each item the loop body is executed. 

Different kinds of 'for' loop:
1. Count-controlled - This is primarily used by C. Python does not have a count controlled loop implementation. It has a initialisation part, a termination expression, and a counting expression. 

2. Numeric Ranges - This is a simplified version of count-controlled loops. Starting with a start value and counting up to an end value. Python doesn't use this either. 

3. Iterator based for loop - This is the type of 'for' loop used by Python. It iterates over an enumeration of a set of items. In each iteration step, a loop variable is set to a value in sequence or other data collection. 

In Python, an 'else' block that follows a 'for' or 'while' loop is executed only if the loop completes normally, without encountering a 'break' statement. 