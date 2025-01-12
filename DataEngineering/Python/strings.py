## Strings ##

#1 Create a function called username_generator take two
#  inputs, first_name and last_name and returns a
#  user_name, a slice of the first three letters of 
#  the first_name and the first four letters last_name
def username_generator(first_name, last_name):
  user_name =[]

  if len(first_name) < 3: 
    user_name = first_name
  else: 
    user_name = first_name[0:3]

  if len(last_name) < 4: 
    user_name += last_name
  else:
    user_name += last_name[0:4]
  return user_name

#2 For the temporary password, use the user_name, 
#  shift all of the letters by one to the right. The 
#  last letter of the user_name ends up as the 
#  first letter and so forth

#  defining a function called password_generator
def password_generator(user_name):
  # define an empty string
  password = ""

  #3 create a for loop that iterates through the 
  #  indices of user_name by going from 0 to len
  #  (user_name).
  for x in range(0, len(user_name)):
    password += user_name[x-1]
  return password

print(password_generator("AbeSimp"))
print(username_generator("Abe", "Simpson"))
username_generator("Abe", "Simpson")
print(password_generator(username_generator("Abe", "Simpson")))

#Q What will the following code print to terminal?
def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])

print_some_characters("watermelon")

#Q2 The following expressions evaluates to False
#A2 "s" in "watermelon"

#Q3 What code would select the letter “p” from 
#   the string good_fruit = "Raspberry"?
#A3 good_fruit[3]

#Q4 Given the string least_favorite_fruit = "cantaloupe", 
#  what piece of code would create a string that was equal 
#  to "lou"?
#A4 least_favorite_fruit[5:8]

#Q5 What character will be selected from the string 
#   cool_fruit = "watermelon" using the code 
#   cool_fruit[len(cool_fruit) - 2]?
#A5 "o"

#Q6 Consider the following function. What would it print to 
# the terminal?
def tell_me_about_icecream(favorite_icecream):
  response = "My favorite icecream is" + favorite_icecream + "."
  print(response)

tell_me_about_icecream("chocolate")

#A6 My favorite icecream ischocolate.










