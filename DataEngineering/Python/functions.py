## Functions
# Define a function my_function() with parameter x
def my_function(x):
  return x + 1

# Invoke the function
print(my_function(2))      # Output: 3
print(my_function(3 + 5))  # Output: 9

# Some tasks need to be performed multiple times within a program.
# Rather than rewrite the same code in multiple places, a function
# may be defined using the def keyword. Function definitions may 
# include parameters, providing data input to the function.

# Functions may return a value using the return keyword followed 
# by the value to return.

## Calling Functions
def doHomework():#+
    print("Doing homework")#+

doHomework()

# Python uses simple syntax to use, invoke, or call a preexisting
# function. A function can be called by writing the name of it, 
# followed by parentheses.

# For example, the code provided would call the doHomework()
# method.

## Parameters as Local Variables
def my_function(value):
  print(value)   
  
# Pass the value 7 into the function
my_function(7) 

# Causes an error as `value` no longer exists
#print(value) 

# Function parameters behave identically to a function’s local 
# variables. They are initialized with the values passed into 
# the function when it was called.

# Like local variables, parameters cannot be referenced from 
# outside the scope of the function.

# In the example, the parameter value is defined as part of the 
# definition of my_function, and therefore can only be accessed 
# within my_function. Attempting to print the contents of value 
# from outside the function causes an error.

## Function Indentation
# Indentation is used to identify code blocks

def test_function(number):
  # This code is part of test_function
  print("Inside the test_function")
  sum = 0
  for x in range(number):
    # More indentation because 'for' has a code block
    # but still part of he function
    sum += x
  return sum
print("This is not part of test_function")

# Python uses indentation to identify blocks of code. Code within 
# the same block should be indented at the same level. A Python 
# function is one type of code block. All code under a function 
# declaration should be indented to identify it as part of the 
# function. There can be additional indentation within a function 
# to handle other statements such as for and if so long as the 
# lines are not indented less than the first line of the function 
# code.


## Multiple Parameters
def ready_for_school(backpack, pencil_case):
  if (backpack == 'full' and pencil_case == 'full'):
    print ("I'm ready for school!")

# Python functions can have multiple parameters. Just as you 
# wouldn’t go to school without both a backpack and a pencil 
# case, functions may also need more than one input to carry 
# out their operations.

# To define a function with multiple parameters, parameter 
# names are placed one after another, separated by commas, 
# within the parentheses of the function definition


def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 ", name)

trip_planner_welcome("LLLLLLL")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(9.9)
print(estimate)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination )
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Home", "World", estimate, "Plane")
## Quiz Question 1
time = "3pm"
mood = "good"

def report():
  print("The current time is " + time)
  print("The mood is " + mood)

print("Beginning of report")

report()
## Quiz Question 2
# Write your tenth_power function here:
def tenth_power(num):
  return num ** 10
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

def sum_numbers(a, b, c):
  print(a + b + c)

sum_numbers(2, 6, 4)
