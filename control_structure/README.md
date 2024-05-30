# Control Structure in Python

Loops are a fundamental concept in programming. You will hardly find any programming language without a way to loop over the code. We are going to talk about 'while' loops here but let's rewind a little bit. 

There are 3 different kinds of loops: 
* Count Controlled loops - A loop structure which have a structure for repeating a loop a certain number of times. Python doesn't have this kind of loop. I am talking about the 'for' loop kind of structure from C language. 

* Condition Controlled loop - A loop will be repeated until a given condition changes i.e. changes to True to False or vice-versa. 

* Collection Controlled loop - It allows looping through the elements of a collection which can be array, list or other ordered sequence. 

Python supplies two different kinds of loops - the 'while' loop and the 'for' loop. 
The body of the loop will be executed as long as the mentioned condition yields True. With the help of a break statement, a while loop can be left prematurely. 
'Break' should not be confused with 'continue' statment. 'continue' STOPS the current iteration of the loop and starts the next iteration by checking the condition. If a loop is left by a break, the else part is not executed. 

The above mentioned behaviour is discussed [here](https://github.com/robsingh/python-refresher/blob/8721858ccb2172332faac3025a4b5d5698e31646/control_structure/examples.py#L1-L26).