# Lambda Functions are small, inline functions that can have any 
# number of arguments but only one expression. They are defined 
# using the lambda keyword and are typically used for short, 
# simple operations

# Regular function 
def square(x): 
    return x ** 2 

# Lambda function 
square_lambda = lambda x: x ** 2 

## Syntax of Lambda Functions

# The basic syntax of a lambda function is:
#lambda [arguments]: [expression] 

# Here are a couple of simple examples:
# Lambda function adding two numbers 

add = lambda a, b: a + b 
print(add(3, 5))  # Output: 8 

# Lambda function to print a name 
greeting = lambda name: f"Hello, {name}!" 
print(greeting("Alice"))  # Output: Hello, Alice! 

## Using Lambda Functions

# Lambda functions are most commonly used as arguments to 
# higher-order functions such as map(), filter(), and sorted().
# Higher-order functions are functions that can accept other 
# functions, such as lambda functions, as arguments.

## Using Lambda with map()

# The map() function applies the given lambda function to each 
# item in a list:

numbers = [1, 2, 3, 4, 5] 
squared = list(map(lambda x: x ** 2, numbers)) 
print(squared)  # Output: [1, 4, 9, 16, 25] 

# In this example, the lambda function lambda x: x ** 2 squares 
# each number in the numbers list. The map() function applies 
# this lambda to each element, resulting in a new list where 
# every number is squared.

## Using Lambda with filter()

# The filter() function creates a new list of elements for which 
# the given lambda function returns True:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 
print(even_numbers)  # Output: [2, 4, 6, 8, 10] 

# Here, the lambda function lambda x: x % 2 == 0 checks if a 
# number is even. The filter() function uses this lambda to 
# keep only the even numbers from the original list, creating 
# a new list containing only even numbers.

## Using Lambda with sorted()

# The sorted() function can use a lambda function as a key for 
# custom sorting:

students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 
sorted_students = sorted(students, key=lambda x: x[2]) 
print(sorted_students) 

# Output: [('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)] 

# In this case, the lambda function lambda x: x[2] is used as 
# the key for sorting. It tells the sorted() function to use 
# the third element (index 2) of each tuple for comparison. 
# As a result, the list of students is sorted based on their 
# age (the third element in each tuple).












