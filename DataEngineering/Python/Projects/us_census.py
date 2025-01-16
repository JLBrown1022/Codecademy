import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

import glob

files = glob.glob('states*.csv')

states_list = []
for filename in files:
  data = pd.read_csv(filename)
  states_list.append(data) 

us_census = pd.concat(states_list)

print(us_census.columns, us_census.dtypes)

#4 Look at the .head()
print(us_census.head())

#5 Use regex to turn the Income column into a format that is ready
#  for conversion into a numerical type
#us_census.Income = us_census['Income'].replace('[\$,]', '', regex=True)
us_census['Income'] = us_census['Income'].replace('[\$,]', '', regex=True)
for x in range(0,len(us_census['Income'])):
  string = str(us_census['Income'].iat[x])
  replace_dollar = string.replace('$', '')
  replace_comma = replace_dollar.replace(',', '')
  replace_dollar_comma = str(us_census['Income'].iat[x]).replace('$', '').replace(',', '')
  us_census['Income'].iat[x] = replace_comma

us_census['Income'] = pd.to_numeric(us_census['Income'])

print(us_census.head())
print(replace_dollar_comma)

#6.6 Separate the 'GenderPop' column into two columns, Men and the Women
Men = []
Women = []
for x in range(0, len(us_census['GenderPop'])):
  string = str(us_census['GenderPop'].iat[x])
  replace = string.split('_')
  Men.append(replace[0])
  Women.append(replace[1])

us_census['Men'] = Men
us_census['Women'] = Women
print(us_census.head())

#7 Convert both of the columns into numerical datatypes
# Remove `M` and `F` then convert
for x in range(0, len(us_census['Men'])):
  string = str(us_census['Men'].iat[x])
  replace = string.replace('M','')
  us_census['Men'].iat[x] = replace
us_census['Men'] = pd.to_numeric(us_census['Men'])

for x in range(0, len(us_census['Women'])):
  string = str(us_census['Women'].iat[x])
  replace = string.replace('F','')
  us_census['Women'].iat[x] = replace
us_census['Women'] = pd.to_numeric(us_census['Women'])

print(us_census.head())

# 8 Use matplotlib to make a scatterplot using plt.show()
plt.scatter(us_census['Women'], us_census['Income'])
plt.xlabel('Number of Women')
plt.ylabel('Income')
plt.title('Scatterplot of Income vs Number of Women')
plt.show()

plt.scatter(us_census['Men'], us_census['Income'])
plt.xlabel('Number of Men')
plt.ylabel('Income')
plt.title('Scatterplot of Income vs Number of Men')
plt.show()

# 9 Print out your column with the number of women per state to see.

print(us_census['Women'])

us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop'] - us_census['Men'])
print(us_census['Women'])

# 10 Use .duplicated() on your census DataFrame to see if we have duplicate rows
print(us_census.duplicated())

# 11 print count of duplicates
us_census = us_census.drop_duplicates()

# 12 Make the scatterplot again
plt.scatter(us_census['Women'], us_census['Income'])
plt.xlabel('Number of Women')
plt.ylabel('Income')
plt.title('Scatterplot of Income vs Number of Women')
plt.show()

# 13 Use .columns to see what the race categories are
print(us_census.columns)

# Convert percentage columns to numerical format
us_census['Hispanic'] = us_census['Hispanic'].str.replace('%', '').astype(float)
us_census['White'] = us_census['White'].str.replace('%', '').astype(float)
us_census['Black'] = us_census['Black'].str.replace('%', '').astype(float)
us_census['Native'] = us_census['Native'].str.replace('%', '').astype(float)
us_census['Asian'] = us_census['Asian'].str.replace('%', '').astype(float)
us_census['Pacific'] = us_census['Pacific'].str.replace('%', '').astype(float)

# Fill NaN values with 0
us_census = us_census.fillna(0)

# Plot histograms
us_census[['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']].hist(bins=10, figsize=(15, 10))
plt.show()



