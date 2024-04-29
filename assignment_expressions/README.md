# Assignment Expression Operator

Assignment Expression Operator, also known as Walrus Operator was introduced in Python 3.8.
Link to the official documentation is [here](https://docs.python.org/3/whatsnew/3.8.html).

The purpose of this feature is not a new way to assign objects to variables, but it is a convenient way to assign variables in the middle of the expressions. Walrus Operator is useful in situations where you want to both assign a value to a variable and use that value within the same expression, such as while looping through an iterator or when performing multiple checks on a value. 
It's main purpose is to improve readability and efficiency by allowing variable assignment within expressions. 
It is equally important to use it judiciously. It can make code less readable and potentially harder to maintain. 

Checkout this [file](./example.py) where I will write some use cases. 

There was a long discussion about the use of Walrus Operator for quite some time. One reason it was not introduced earlier was the
fact that it can also be used to write code which is less readable. Personally, I have not used it a lot but I will try to implement
in my personal projects and calculate the efficiency of the methods. 