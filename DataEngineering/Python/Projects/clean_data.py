## cleaning_data.py ##

# When we receive raw data, we have to do a number of things before we’re 
# ready to analyze it, possibly including:

# - diagnosing the “tidiness” of the data — how much data cleaning we will 
#   have to do
# - reshaping the data — getting right rows and columns for effective 
#   analysis
# - combining multiple files
# - changing the types of values — how we fix a column where numerical 
#   values are stored as strings, for example:
#   ▫︎ dropping or filling missing values - how we deal with data that is 
#     incomplete or missing
#   ▫︎ manipulating strings to represent the data better
#  
#  We will go through the techniques data scientists use to accomplish 
#  these goals by looking at some “unclean” datasets and trying to get 
#  them into a good, clean state

##2 Diagnose the Data ##

# DATA must have:
# ▪︎ Each variable as a separate column
# ▪︎ Each row as a separate observation

# For example, we could reshape a table like:
# ▪︎  Account	Checkings	Savings
# ▪︎ “12456543”	8500	    8900
# ▪︎ “12283942”	6410	    8020
# ▪︎ “12839485”	78000	    92000

# Into:
# ▪︎ Account	Account Type	Amount
# ▪︎ “12456543”	“Checking”	    8500
# ▪︎ “12456543”	“Savings”	    8900
# ▪︎ “12283942”	“Checking”	    6410
# ▪︎ “12283942”	“Savings”	    8020
# ▪︎ “12839485”	“Checking”	    78000
# ▪︎ “12839485”	“Savings”	    920000

# Use 'panda's functions to explore the dataset

# Some of the most useful ones are:
# ▪︎ .head() — display the first 5 rows of the table
# ▪︎ .info() — display a summary of the table
# ▪︎ .describe() — display the summary statistics of the table
# ▪︎ .columns — display the column names of the table
# ▪︎ .value_counts() — display the distinct values for a column

import codecademylib3_seaborn
import pandas as pd
from students import students as df

df1 = pd.read_csv("df1.csv")
df2 = pd.read_csv("df2.csv")

#2.1 Print the .head() of df1 and df2
print(df1.head())
print(df2.head())

# Create a variable named clean and set it equal to either 1 for df1 
# or 2 for df2
df1.clean = 1
df2.clean = 2
clean = 2
print(df2.clean)

##3 Multiple Files ##

# The same data is separated out into multiple files, filename structures: 
# 'file1.csv', 'file2.csv', 'file3.csv', and so on. Use 'glob', a Python 
# library for working with files. 'glob' can open multiple files using
# shell-style wildcard matching to get the filenames
import glob

#3.1 There are 10 different files containing 100 students each. The 
#    filename structure is: 'exams[0-9].csv'

#    Create a variable called 'student_files' and set it equal to the 
#    .glob() of all of the csv files we want to import
student_files = glob.glob("exams*.csv")

#3.2 Create an empty list called df_list that will store all of the 
#    DataFrames we make from the files exams0.csv through exams9.csv
df_list = []

#3.3 Loop through the filenames in student_files, and create a 
#    DataFrame from each file. Append this DataFrame to df_list
for file in student_files:
  df_list.append(pd.read_csv(file))

#3.4 Concatenate all of the DataFrames in df_list into one 
#    DataFrame called students
students = pd.concat(df_list)

#3.5 Print students and the length of students
print(students)
print(len(students))

##4  Reshaping your Data ##

# Use .melt() to take in a DataFrame, to unpack the columns

# df = pd.melt(
#   frame=df, 
#   id_vars=["Account"],
#   value_vars=["Checking","Savings"],
#   value_name="Amount",
#   var_name="Account Type"
# )

# ▪︎ frame: the DataFrame you want to melt
# ▪︎ id_vars: the column(s) of the old DataFrame to preserve
# ▪︎ value_vars: the column(s) of the old DataFrame that you 
#     want to turn into variables
# ▪︎ value_name: what to call the column of the new DataFrame 
#     that stores the values
# ▪︎ var_name: what to call the column of the new DataFrame
#     that stores the variables

# Use .columns() to rename the columns after melting:
# ▪︎ .columns(["Account", "Account Type", "Amount"])

# Print the .head() and the .columns of students
# Print the .value_counts() of the column exam

print(students.columns)

# Index(['full_name', 'gender_age', 'fractions', 'probability', 'grade'], 
# dtype='object')

students = pd.melt(
   frame=students, 
   id_vars=["full_name", "gender_age", "grade"],
   value_vars=["fractions","probability"],
   value_name="score",
   var_name="exam"
 )

print(students.head())
print(students.columns)
print(students.exam.value_counts())

##5 Duplicates ##

# Use .duplicated() to find duplicate rows in your DataFrame
# Use .drop_duplicates() function to remove all duplicate rows
# To remove every row with a duplicate value in the item 'item_column', 
#    we could specify a subset keeping only the first occurrence of each 
#    duplicate
#    ▪︎ df = df.drop_duplicates(subset=['item_column'])

#5.1 Use the .duplicated() function on the  DataFrame, df, to make 
#    a Series object called duplicates.
duplicates = df.duplicated()

#5.2 Print out the .value_counts() of the duplicates
print(duplicates.head())
print(duplicates.value_counts())

#5.3 Update the value of df to be the df table with the 
#    duplicates dropped
students = students.drop_duplicates()

#5.4 Use the .duplicated() function again to make a Series object 
#    called duplicates after dropping the duplicates
duplicates = students.duplicated()
print(duplicates.head())
print(duplicates.value_counts())

##6 Splitting by Index ##

# We can break the data by splitting with .str:

# Create the 'month' column, take the first two characters a value
# ▪︎ df['month'] = df.some_date.str[0:2]

# Create the 'day' column, take the next two characters a value
# ▪︎ df['day'] = df.some_date.str[2:4]

# Create the 'year' column, take the last four characters a value
# ▪︎ df['year'] = df.some_date.str[4:]

#6.1  Print out the columns of the students DataFrame
print(students.columns)

#6.2 The column gender_age sounds like it contains both gender and age!
#    Print out the .head() of the column to see what it contains
print(students.head())

#6.3 Separate the gender data into a new column called gender
students['gender'] = students.gender_age.str[0:1]

#6.4 separate out the age
students['age'] = students.gender_age.str[1:]

#6.5  Print the .head() of students
print(students.head())

#6.6 Set the students DataFrame to be the students DataFrame 
#    with all columns except gender_age
students = students[['full_name', 'exam', 'grade', 'score', 'gender', 'age']]

##7 Split by Character ##

# Split this column into two separate, cleaner columns

# Split the string and save it as `string_split`
# ▪︎ string_split = df['type'].str.split('_')
 
# Create the 'usertype' column
# ▪︎ df['usertype'] = string_split.str.get(0)
 
# Create the 'country' column
# ▪︎ df['country'] = string_split.str.get(1)

#7.1 Split the string and save it as `string_split`
name_split = students['full_name'].str.split(' ')
 
#7.2 Create the 'first_name' column
students['first_name'] = name_split.str.get(0)
 
#7.3 Create the 'last_name' column
students['last_name'] = name_split.str.get(1)

print(students.head()) #7.4

##8 Looking at Types ##

# Each column of a DataFrame can hold items of the same data 
# type or dtype. The dtypes that pandas uses are: float, int, 
# bool, datetime, timedelta, category and object

# To see the types of each column of a DataFrame, we can use:
# ▪︎ print(df.dtypes)

#8.1 Print out the .dtypes attribute.
print(df.dtypes)

  # full_name     object
  # exam          object
  # score         object
  # gender        object
  # age           object
  # first_name    object
  # last_name     object
  # dtype: object

#8.2 Print out the mean of the score column of df
print(df.score.mean()) 
# ▪︎ Will  error for non-numeric data as it's an object

##9 String Parsing ##

# Use string parsing to modify data to a  more meaningful metrics
#   as when a column is actually composed of strings representing numeral. 
# Use regex to get rid of all of the dollar signs
df.price = df['price'].replace('[\$,]', '', regex=True)

# Then use the pandas function '.to_numeric()' to convert strings 
#   containing numerical values to integers or floats:

df.price = pd.to_numeric(df.price)

#9.1 Use regex to take out the % signs in the score column
df.score = \
df['score'].replace('[\%,]', '', regex=True)

#9.2 Convert the score column to a numerical type using the pd.to_numeric()
df.score = pd.to_numeric(df.score)

##10 More String Parsing ##

# Use regex to do analysis on numbers that are imbedded in strings
#
#   date.       exerciseDescription
#   10/18/2018	“lunges - 30 reps”

# Separate out data "30 lunges" into 2 columns with the number of reps,
# "30", and the exercise, "lunges" using the '.str.split()' function
split_df = df['exerciseDescription'].str.split('(\d+)', expand=True)

# Then assign the columns from this DataFrame to the original df:
df.reps = pd.to_numeric(split_df[1])
df.exercise = split_df[0].replace('[\- ]', '', regex=True)

#10.1 Print the first five rows of the grade column

print(students.grade.head())

#10.2 Use regex to extract the number from each string in grade and store 
#     those values back into the grade column
students.grade = students.grade.str.split('(\d+)', expand=True)[1]

#10.3 Print the dtypes of the students table
print(students.dtypes)

#10.4 Convert the grade column to be numerical 
students.grade = pd.to_numeric(students.grade)
print(students.dtypes)

#10.5 Calculate the mean of grade, store it in  'avg_grade'
avg_grade=students.grade.mean()
print(avg_grade)





# Use .pivot_table() to create a new DataFrame that groups your data
# Use .pivot_table() to rearrange your data into a more useful format


# Use .shape to find the number of rows and columns in your DataFrame














