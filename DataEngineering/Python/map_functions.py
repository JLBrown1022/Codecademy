## Map Functions

# Python provides several built-in functions that help with 
# functional programming. One of the most versatile and commonly 
# used is the map() function. 

## What is the map() Function?

# The map() function is a built-in function in Python that 
# applies a given function to each item in an iterable (like a 
# list, tuple, or string) and returns a new iterable as a result.

# The basic syntax of map() is:
#map(function, iterable, [iterable2, iterable3, ...]) 

# - "function" is the function to apply to each item in the 
#   iterable(s)
# - "iterable" is the iterable or optionally multiple iterables 
#   to process

## How map() Works
def double(x): 

    return x * 2 

numbers = [1, 2, 3, 4, 5] 
doubled_numbers = map(double, numbers) 

print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10] 

# map() applies the double function to each number in the 
# numbers list, creating a new iterator with the results.

## Using map() with Built-in Functions

# We can use map() with Python’s built-in functions. For example,
# we can quickly convert a list of strings to integers:


# Converting strings to integers 
str_nums = ['1', '2', '3', '4', '5'] 
int_nums = list(map(int, str_nums)) 
print(int_nums)  # Output: [1, 2, 3, 4, 5] 

# Or find the length of another list of strings:

# Finding the length of strings 

words = ['apple', 'banana', 'cherry'] 
word_lengths = list(map(len, words)) 
print(word_lengths)  # Output: [5, 6, 6] 

#Using map() with Lambda Functions

# map() is most often used in conjunction with lambda functions 
# for quick, one-off operations. For example, here we easily 
# double each number in a list:

numbers = [1, 2, 3, 4, 5] 
doubled = list(map(lambda x: x * 2, numbers)) 
print(doubled)  # Output: [2, 4, 6, 8, 10] 

## Multiple Iterables with map()

# map() can also work with multiple iterables, assuming the 
# function can take multiple inputs:

list1 = [1, 2, 3] 
list2 = [10, 20, 30] 
result = list(map(lambda x, y: x + y, list1, list2)) 
print(result)  # Output: [11, 22, 33] 

## Advantages of Using map()

# 1 - Readability: map() can make our code more concise and 
#     easier to read, especially for simple operations on 
#     iterables.
# 2 - Memory Efficiency: map() returns an iterator, which means 
#     it doesn’t create the entire result list in memory at once.
#     This can be beneficial when working with large datasets.
# 3 - Functional Programming: map() encourages a functional 
#     programming style, which can lead to more maintainable and 
#     testable code.

## When to Use map()

# Use map() when:

# 1 - We need to apply a function to every item in an iterable.
# 2 - We want to transform data without explicitly writing a 
#     for loop.
# 3 - We’re working with large datasets and want to avoid 
#     creating intermediate lists.

## Alternatives to map()

#While map() is powerful, there also are alternatives:

# 1 - List Comprehensions: Often more readable for simple 
#     operations.
doubled = [x * 2 for x in numbers] 

# 2 - Generator Expressions: Similar to list comprehensions 
#     but return an iterator.
doubled = (x * 2 for x in numbers) 

# 3 - For Loops: More verbose but sometimes clearer for complex 
#     operations.
doubled = [] 
for x in numbers: 
   doubled.append(x * 2) 

## Best Practices

# 1 - Use map() when it makes your code more readable and concise.
# 2 - For complex operations, consider using a regular function 
#     instead of a lambda.
# 3 - Remember that map() returns an iterator. If you need a list,
#     wrap it with list().
# 4 - When working with multiple iterables, ensure they have the
#     same length to avoid unexpected results.



