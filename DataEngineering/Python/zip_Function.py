# Combining Lists: The Zip Function called zip()
# The zip() function takes two or more lists and returns an iterator that 
# generates tuples of elements from the lists.
# The zip() function stops generating tuples when the shortest list is exhausted.

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e'] 
# The lists have different lengths
list3 = [10, 20, 30, 40, 50, 60]
owners = names = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]
heights = [61, 70, 67, 64]
names_and_heights = zip(names, heights)

# This zip object contains the location of this variable in our 
# computer’s memory.
print("computer memory location:", names_and_heights)

# It's simple to convert this object into a useable list with the built-in 
# function list()
converted_list = list(names_and_heights)
print("converted to a list:", converted_list)

# Use a list comprehension to create a new list with tuples of the elements
# from list1 and list2
# The zip() function stops generating tuples when the shortest list is exhausted.   
# Combine the lists using zip()
# Zip the lists together    

names_and_dogs_anmes = zip(names, dogs_names)
list_names_and_dogs_anmes = list(names_and_dogs_anmes)
# or
names_and_dogs_anmes = list(zip(names, dogs_names))

print("Names and Dogs' Names:", list_names_and_dogs_anmes)

# 1: Create a list called single_digits that consists of the numbers 0-9 (inclusive)
digits = single_digits = range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cubes = [] #6 create a list called cubes
squares = [] #3 create a list called squares

#2 Create a for loop that goes through single_digits and prints out each one
for digit in digits:
  print(digit)
  #4 .append() the squared value of each element of single_digits to the list squares
  squares.append(digit**2)

print(squares)

squares = [digit**2 for digit in digits]

print(squares)

cubes = [digit**3 for digit in digits]
print(cubes)
