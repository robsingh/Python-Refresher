# Introduction - Dictionary

A dictionary is a data structure that stores key-value pairs. 

For example, 
```
person = {
    'name': 'Deve',
    'age': 28,
    'city': 'Poland',
    'email': 'deve@example.com'
}
```
* Keys in the above example are 'name', 'age', 'city', and 'email'. 
* Every key has a corresponding value.
* We call a key-value pair an item. 
* Dictionaries are useful for organizing data in a way that allows quick and easy access. 
* Dictionaries are mutable.  

# Dictionary and Lists

A list is a sequence of objects where the order matters. You can access the elements of the list through its index. Similarly dictionaries are also ordered but we can't access elements by their position. 

In a dictionary, you can directly retrieve an information using the key, which is much quicker compared to searching through a list.
Think of it like looking up a word in dictionary versus flipping through pages of a book to find it. The dictionary provides instant access, while the list requires more time to search through. 

# items() 
- The items view can be turned into a list by applying the list function. We have no information loss by turning a dictionary into an item view or an items list. Accessing dictionary items via a method like items() provides a more efficient approach compared to creating lists directly due to: 

1. Lazy Evaluation : The items() method does not create the entire list of key-value pairs upfront. Instead, it returns a view object that generates objects on-the-fly as needed. This saves memory and computation time, especially when dealing with large dictionaries where creating a complete list of items upfront may be resource incentive. 

2. Memory Efficiency : items() generate items dynamically without storing the entire list in memory at once, whereas generating a list requires storing all key-value pairs in memory simultaneously. 

3. Time Complexity : If only a subset of items is needed, items() allows for efficient iteration over only the required items without iterating over the entire dictionary. 

# keys() 
- keys() method returns a view object that returns list of all keys in the dictionary. This allows you to iterate over or access the keys directly without needing to create a separate list of keys. 

It is a less commonly used behavior because iterating over a dictionary directly implicitly iterates over its keys. 

# values() 
- used to iterate over the values of a dictionary. 
