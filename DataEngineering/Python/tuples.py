# Tuples are one of the built-in data structures in Python. Just like lists, 
# Tuples can hold a sequence of items and have a few key advantages:
#   - Tuples are more memory efficient than lists
#   - Tuples have a slightly higher time efficiency than lists
#   - Tuples can be used as keys in dictionaries, while lists cannot
#   - Tuples can be used as elements of sets, while lists cannot
#   - Tuples can be used as named tuples, which are similar to dictionaries but
#     with a fixed set of keys
#   - Tuples can be used as data structures for holding data that should not be
#     changed, such as a list of constants
#   - Tuples can be used as return values for functions that return multiple
#     values
#   - Tuples can be used as a way to :
#       unpack values from a sequence, 
#       swap values in a single line of code, 
#       return multiple values from a function,  
#       pass multiple values to a function, 
#       create a sequence of values that should or should not be changed, 
#       create a sequence of values that should be immutable
#       create a sequence of values that should be hashable 
#       create a sequence of values that should be used as keys in a dictionary
#       create a sequence of values that should be used as elements in a set
#       create a sequence of values that should be used as elements in a list

# Tuples have a limited number of built-in functions as they are immutable
#   - count() - returns the number of times a specified value occurs in a tuple 
#   - index() - returns the index of the first occurrence of the specified value
#     in a tuple
#   - len() - returns the number of items in a tuple
#   - max() - returns the largest item in a tuple
#   - min() - returns the smallest item in a tuple
#   - sum() - returns the sum of all items in a tuple
#   - sorted() - returns a sorted list of the specified iterable object
#   - any() - returns True if any item in an iterable object is true
#   - all() - returns True if all items in an iterable object are true
#   - enumerate() - returns an enumerate object that contains the index and
#     value of all items in an iterable object
#   - filter() - returns an iterator where the items are filtered through a
#     function to test if the item is accepted or not
#   - map() - returns an iterator where the items are modified by a function
#   - zip() - returns an iterator that combines multiple iterables into one
#     sequence of tuples

# Creating a tuple
# Tuples are created by enclosing a sequence of items in parentheses
# The items in a tuple can be of any data type
# The items in a tuple can be of different data types
# The items in a tuple can be of the same data type, value, reference, object, 
#   function, class, instance, module, package, library, framework, 
#   application, service, database, table, column, row, cell, value, 
#   key, index, position, order, length, size, shape, dimension, structure, 
#   format, style, type, or pattern. 
# The items in a tuple can be nested tuples, lists,  dictionaries,  sets,  
#   frozensets,  namedtuples,  dataclasses


my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')

print(my_tuple[0])
print(my_tuple[3:5])

print(len(my_tuple)) 

print(my_tuple.index('abc'))
print(my_tuple.index(789)) 



