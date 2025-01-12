
## Formatting Methods ##

# The.lower() and .upper() and .title() methods are used
# to change the case of the string. 
# - .lower() method converts all letters to lowercase
# - .upper() method converts all letters to uppercase
# - .title() method converts the first letter of each 
#    word to uppercase

poem_title = "spring storm"
poem_author = "William Carlos Williams"

#1 Change poem_title to a title case and save it to 
#  poem_title_fixed
poem_title_fixed = poem_title.title()
#print(poem_title_fixed)
#print(poem_title)

#2 Change poem_author to a uppercase and save it to 
#  poem_author_fixed
poem_author_fixed = poem_author.upper()
#print(poem_author_fixed)
#print(poem_author)

## Splitting Strings ##

# The .split() method is used to split a string into a list
# of substrings. The .split() method takes one argument, the
# delimiter, and splits the string at each instance of that
# delimiter. The delimiter is not included in the substring.

# .split() is performed on a string, takes one argument, and 
# returns a list of substrings found between the given 
# argument (which in the case of .split() is known as the 
# delimiter).

# string_name.split(delimiter)
poem_title_words = poem_title.split()
print(poem_title_words)

# If no argument is provided for .split(), it will default 
# to splitting at space.
# For example:

man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())
# => ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

line_one = "The sky has given over"

line_one_words = line_one.split()
print(line_one_words)
line_one_words = line_one.split("a")
print(line_one_words)

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
#print(authors)

#1 Using .split() and the provided string, create a 
# list called author_names
author_names = authors.split(",")
#print("\n", author_names)

#2 Create another list called author_last_names that 
# only contains the last names
author_last_names = []

for name in author_names:
  author_last_names.append(name.split()[-1])
#print(author_last_names)


# We can also split strings using escape sequences. 
# Escape sequences are used to indicate that we want 
# to split by something in a string that is not 
# necessarily a character. Such as:
# - \n Newline 
# - \t Horizontal Tab

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

#1 Create a list called spring_storm_lines that 
#  contains a string for each line of Spring Storm
spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

for line in spring_storm_lines:
  print(len(line), len(line.split())-1)

## Joining Strings ##

# The .join() method is used to join a list of strings
# together. It is called on a string that will be used as
# the delimiter and the list of strings that we want to
# join together. The method returns a new string that is
# the concatenation of the strings in the list.

#1 Use .join() to combine these words into a sentence 
#  and save that sentence as the string 
#  reapers_line_one

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ', '.join(reapers_line_one_words)
print(reapers_line_one)

# join together the strings in the list together into 
# a single string that can be used to display the full 
# poem. Name this string winter_trees_full

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_lines)
print(winter_trees_full)

# The.strip() method removes all whitespace characters 
# from the beginning and end of a string.

# .strip() can used with a character argument, which will
# strip that character from either end of the string.
featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas       '
# By including the argument '!' we are able to 
# strip all of the !

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

#1 use .strip() on each line in the list to remove unnecessary
#  whitespace and save it as a new list love_maybe_lines_stripped
love_maybe_lines_stripped = []

for line in love_maybe_lines:
  #print(line)
  #print(line.strip())
  love_maybe_lines_stripped.append(line.strip())

#2 .join() the lines in love_maybe_lines_stripped 
#  together into one large multi-line string, 
#  love_maybe_full
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

#print(love_maybe_full)
  #love_maybe_lines_stripped = love_maybe_lines[lines].strip()
#print(love_maybe_lines)
#print(love_maybe_lines_stripped)

# The .replace() method is used to replace a substring. This
# method takes two arguments, the substring to be replaced
# and the string to replace it with to return a new string.

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

#1 Use .replace() to change all instances of Tomer in
#  the bio to Toomer. Save the updated bio to the 
#  string toomer_bio_fixed
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)


# The .count() method is used to count the number of
# occurrences of one string within another string.

#1 Use .count() to find and print how many times the word
#  'Dream' appears in the string dream_song
dream_song = \
"""
In the quiet of the night, I dreamt
Of a world where dreams could be free,
Where every star would be a moon,
And the moon would be a star.
"""
dream_count = dream_song.count('dream')
print(dream_count)

# The .index() method is used to find the index of the first
# occurrence of a substring in a string. The method takes
# one argument, the substring you are searching for, and
# returns the first index where that substring is found.

#1 Use .index() to find the index of the first instance of
#  the word 'but' in the string but
but = "But soft what light through yonder window breaks"
but_index = but.index('But')
print(but_index)

# .find() method is similar to .index() but it returns
# -1 if the substring is not found. 
# .find() takes a "argument string" and searches the string 
# it was run on for that argument string. It then returns 
# the first index location value of that argument string.

#1 Here is the first line of Gabriela Mistral’s poem 
#  God Wills It.
god_wills_it_line_one = "The very earth will disown you"

# At what index place does the word “disown” appear? 
disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)

# .format() method is used to concatenate strings and

# Write a function called poem_title_card that takes 
# two inputs: the first input should be title and the 
# second poet
def poem_title_card(title, poet):
  poem = "The poem \"{}\" is written by {}.".format(title, poet)
  print(poem)
  return (poem)

poem_title_card("I Hear America Singing", "Walt Whitman")
def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana"))

# .format() can be made even more legible for other people 
# reading your code by including keywords
# - {0} is the first argument
# - {1} is the second argument
# - {2} is the third argument
# - {n} is the nth argument


#1 The function poem_description is supposed to use 
#  .format() to print out some quick information about 
#  a poem, but it seems to be causing some errors currently.

# Fix the function by using keywords in the .format() method

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  print(poem_desc)
  return poem_desc

#2 Run poem_description with the following arguments and save 
# the results to the variable my_beard_description
my_beard_description = poem_description(author = "Shel Silverstein", title = "My Beard", original_work = "Where the Sidewalk Ends",publishing_date = "1974")
print(my_beard_description)

# The .format() method can be used to concatenate strings 
# in the .format() method to produce a string that is
# more legible. 

#*************************#
## String Methods Review ##
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(",")
#print(highlighted_poems_list)

highlighted_poems_stripped= []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
#print(highlighted_poems_stripped)

highlighted_poems_details = []

for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(":"))

#print(highlighted_poems_details)

titles = []
poets = []
dates = []

for x in highlighted_poems_details:
  titles.append(x[0])
  poets.append(x[1])
  dates.append(x[2])
  
for x in range(len(highlighted_poems_details)):
  print ("The poem {} was published by {} in {}.".format(titles[x], poets[x], dates[x]))

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#1 print highlighted_poems to the terminal to see how it displays
#print(highlighted_poems)

# 2 Split highlighted_poems at the commas. Saving it to 
# highlighted_poems_list then print that
highlighted_poems_list = highlighted_poems.split(",")
#print(highlighted_poems_list)

#4 Create a new empty list, highlighted_poems_stripped
highlighted_poems_stripped= []

# Then iterate through highlighted_poems_list using a for loop 
# For each poem strip away the whitespace and append it to 
# your new list, highlighted_poems_stripped
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
#print(highlighted_poems_stripped)

#6 break up all the information for each poem into it’s own list. 
# Create an empty list called highlighted_poems_details
highlighted_poems_details = []

#7 Iterate through highlighted_poems_stripped and split at 
# the : characters. Append the new lists into 
# highlighted_poems_details
for i in highlighted_poems_stripped:
  highlighted_poems_details.append(i.split(":"))

#print(highlighted_poems_details)

#8 Create three new empty lists, titles, poets, and dates
titles = [] ; poets = [] ; dates = []

#9 Iterate through highlighted_poems_details and for each list 
# in the list append the appropriate elements into the lists 
# titles, poets, and dates
for x in highlighted_poems_details:
  titles.append(x[0])
  poets.append(x[1])
  dates.append(x[2])

#10 write a for loop that uses .format() to print out the 
#    following string for each poem
for x in range(len(highlighted_poems_details)):
  print ("The poem {} was published by {} in {}.".format(titles[x], poets[x], dates[x]))

#Q1 Given the list greeting = ["Hello", "my", "name", "is", "Earl"] 
#   what line of code would produce a string that contains 
#   `”Hello_my_name_is_Earl”.
greeting = ["Hello", "my", "name", "is", "Earl"]
"_".join(greeting)

#Q2 Given the following block of code, what is stored in the 
#   string split_hairs?
dirty_harry = "Go ahead, make my day."
split_hairs = dirty_harry.split("a")
# => ['Go ', 'he', 'd, m', 'ke my d', 'y.']

#Q3 Which of the following is a benefit of using .format() 
#   to include variables in your strings
#A3 To make code more legible/readable.

#Q4 Given the string hello_jerry = "Hi, my name is Jerry", 
#   which of the following lines of code will produce the 
#   string "Hi, My Name Is Jerry"?
#A4 hello_jerry.title()

#Q5 Which of the following answer choices best describes 
#   the function of the string method .find()?
#A5 .find() searches a string for its argument and returns 
#   the index location of that argument

#Q6 Consider the string user_name = ":::::::: Eloise :::::::::::". 
#   What line of code would clean this string and produce 
#   the string user_name_fixed = "Eloise"?
#A6 user_name = user_name.replace(":::", "").strip() or 
#   user_name.translate(str.maketrans("", "", ":-:")) or
#   user_name_fixed = user_name.strip(":").strip()

#Q7 Given the poem (When You Are Old, by W. B. Yeats) saved 
#   as multiline string as shown in the code block, what code 
#   could we use to create a list that contains a string of 
#   each line in the poem?

when_you_are_old = \
"""When you are old and grey and full of sleep,
And nodding by the fire, take down this book,
And slowly read, and dream of the soft look
Your eyes had once, and of their shadows deep;

How many loved your moments of glad grace,
And loved your beauty with love false or true,
But one man loved the pilgrim soul in you,
And loved the sorrows of your changing face;

And bending down beside the glowing bars,
Murmur, a little sadly, how Love fled
And paced upon the mountains overhead
And hid his face amid a crowd of stars."""

#A7 list_of_lines = when_you_are_old.split("\n")

#BQ3 How would you write a Python function that takes a 
#    string and replaces all the vowels with the next 
#    vowel in the English alphabet?
def replace_vowels(input_string):
  vowels = "aeiouAEIOU"
  output_string = ""
  for char in input_string:
    if char in vowels:
      output_string += vowels[(vowels.index(char) + 1) % len(vowels)]
    else:
      output_string += char
  return output_string









