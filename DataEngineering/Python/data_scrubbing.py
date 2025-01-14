## Wrangling Data ##

# Use the read_csv() function in pandas to load our dataset as a 
# pandas 'dataframe' and take a look at the first 10 of 27 rows

import pandas as pd
restaurants = pd.read_csv("DOHMH_restaurant_inspections.csv")

#  the .head(10) function will show us the first 10 rows in our dataset
print(restaurants.head(10))

# The .info() function provides us with a concise summary of our dataframe,
# including the number of non-null values and the data types of each column
print(restaurants.info())

# .shape method in pandas identifies the number of rows and columns in our 
# dataset as (rows, columns):

restaurants.shape # (27, 7)

# To remove any duplicate rows, we can use the drop_duplicates() function

# the .drop_duplicates() function removes duplicate rows
restaurants = restaurants.drop_duplicates() 
# .shape method again:

restaurants.shape # (25, 7)

# To have some consistency across column names, we will iterate over the 
# column names of our dataset and convert them all to lowercase using the 
# map() and lower() functions. We also need to make sure to include the 
# str function to identify that we are working with strings.

# map() applies the str.lower() function to each of the columns in our 
# dataset to convert the column names to all lowercase
restaurants.columns = map(str.lower, restaurants.columns)

# the .head(10) function will show us the first 10 rows in our dataset
print(restaurants.head(10))  

# The first column of the dataset is  DBA. We know thea column is restaurant 
# names. Use the .rename() function and a dictionary to relabel our columns. 
# While we are renaming our columns, we might also want to shorten the 
# cuisine description column to just cuisine

# 'axis=1' refers to columns, 
# 'axis=0' refers to rows
# In the dictionary, 'key' refers to the original column name and 'value' 
# refers to the new column name {'key': 'value', 'oldname2': 'newname2'}
restaurants = restaurants.rename({'dba': 'name', 'cuisine description': 'cuisine'}, axis=1)
print(restaurants.head(10))

## Data Types

# Let’s take a look at each column’s data types by appending .dtypes 
# to our pandas dataframe.
restaurants.dtypes

# Outputs:
# name         object
# boro         object
# cuisine      object
# grade        object
# latitude    float64
# longitude   float64
# url          object

# There are two types of variables: object and float64. 
# object can consist of both strings or mixed types (both numeric and 
# non-numeric), 
# float64 are numbers with a floating point (ie. numbers with decimals)
# Other data types: 
#  * int64 (integer numbers), 
#  * bool (True/False values), 
#  * datetime64 (date and/or time values)

# Look at the number of unique values in each column using the .nunique() 
# function to count the number of unique values in each column 
restaurants.nunique() 

# Output:
# name         25
# boro          4
# cuisine      15
# grade         1
# latitude     24
# longitude    24
# url          16

# The data consists of 4 boroughs in New York and 15 cuisine types

## Missing Data

# From our initial inspection of the data, we know we have missing data 
# Use .isna() to identify if the value is missing. .isna() returns a boolean 
# to indicate if the observation in that column is missing (True) or 
# present (False). 
# .sum() will count the number of missing values, where .isna() returns True.

# counts the number of missing values in each column 
restaurants.isna().sum() 

# Output:
# name          0
# boro          0
# cuisine       0
# grade        15
# latitude      0
# longitude     0
# url           9

# We see that there are missing values in the grade and url columns, but 
# no missing values in latitude and longitude. However, coordinates at 
# (0.000, 0.000) are not valid for any of the restaurants in our dataset, 
# and we saw that these exist in our initial analysis. To handle this,
#  we will replace the (0.000, 0.000) coordinates with NaN values.

# Use the .where() method to replace the invalid coordinates. 
# .where() method keeps the values specified in its first argument, 
# and replaces all other values with NaN

# .where() function replaces latitude values less than 40 with NaN values
restaurants['latitude'] = \
      restaurants['latitude'].where(restaurants['latitude'] > 40) 

# here our .where() function replaces longitude values greater than -70 
# with NaN values
restaurants['longitude'] = \
      restaurants['longitude'].where(restaurants['longitude'] < -70) 

# .sum() counts the number of missing values in each column
restaurants.isna().sum() 

# Output:
#     name          0
#     boro          0
#     cuisine       0
#     grade        15
#     latitude      2
#     longitude     2
#     url           9

# We see that latitude and longitude each have two missing data points 
# thanks to replacing the (0.000, 0.000) values with NaN values.

## Characterizing missingness with crosstab ##

# Let’s try to clarify the missingness in the url column by counting the 
# missing values across each borough using the .crosstab() function 
# .crosstab() computes the frequency of two or more variables 
# We can add isna() to identify then NaN in that column by boolean
# .crosstab() will look at all the boroughs in our data to find 
# whether or not the url link is missing

pd.crosstab(
        # tabulates the boroughs as the index
        restaurants['boro'],  

        # tabulates the number of missing values in the url column as columns
        restaurants['url'].isna(), 

        # names the rows
        rownames = ['boro'],

        # names the columns 
        colnames = ['url is na']) 


# Output:
#     url is na   False   True
#     boro
#     Bronx         1      1
#     Brooklyn      2      4
#     Manhattan    11      2
#     Queens        2      2

# We see that most of the restaurants in Manhattan in our dataset have 
# restaurant links, while most restaurants in Brooklyn do not have url links

## Removing prefixes ##

# It might be easier to read what url links are (something) by removing some
# prefix(es), such as “https://www.”
# Use str.lstrip() to remove the prefix(es)

# Similar to when we were working with our column names, we need to make 
# Include the .str function to identify that we are working with strings
# Include the .lstrip to remove parts of the string from the left side

# .str.lstrip('https://') removes the “https://” from the left side of 
# the string
restaurants['url'] = restaurants['url'].str.lstrip('https://') 

# .str.lstrip('www.') removes the “www.” from the left side of 
# the string
restaurants['url'] = restaurants['url'].str.lstrip('www.') 

# the .head(10) function will show us the first 10 rows in our dataset
print(restaurants.head(10))

# Output: data_wrangling_restaurants_url_cleaned

# Amazing! Our dataset is now much easier to read and use. We have identifiable 
# columns and variables that are easy to work with thanks to our data wrangling 
# process. We also corrected illogical data values and made the strings a 
# little easier to read.

# In this example, we worked with data that was rather tidy, in the sense that 
# each row was an observation (a restaurant) and each column was a variable. 
# However, what if our dataset was not tidy? What if our columns and rows 
# needed reorganization?

## Tidy Data ##

# Looking at data from the New York State Department of Labor, Quarterly 
# Census of Employment and Wages of the average annual wage for restaurant 
# workers across New York City boroughs and New York City as a whole from 
# the years 2000 and 2007.
annual_wage = pd.read_csv("annual_wage_restaurant_boro.csv")
print(annual_wage)
 
# There are three variables in this dataset: borough, year, and average  
# annual income. However, we have values (2000 and 2007) in the column  
# headers rather than variable names (year and average annual income).  
# This is not ideal to work with, so let’s fix it using .melt() function
# in pandas to turn the current values (2000 and 2007) in the column headers
# to row values and add year and avg_annual_wage as our column labels.

annual_wage=annual_wage.melt(

      # which column to use as identifier variables
      id_vars=["boro"], 
      
      # column name to use for “variable” names/column headers (ie. 2000 and 2007) 
      var_name=["year"], 

      # column name for the values originally in the columns 2000 and 2007
      value_name="avg_annual_wage") 

print(annual_wage)

# Now we have a tidy dataset where each column is a variable (borough, year,  
# or average annual wage), and each row is an observation
