import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import pandas as pd


# Create the dataset as a Python dictionary
d = {
    'X': [5.4,13.8,14.7,17.6,np.nan,1.1,12.9,3.4,np.nan,10.2],
    'Y': [18,27.4,np.nan,18.3,49.6,48.9,np.nan,13.6,16.1,42.7],
    'Z': [7.6,4.6,4.2,np.nan,4.7,8.5,3.5,np.nan,1.8,4.7]
}

dTest = {
    'X': [13.1, 10.8, np.nan, 9.7, 11.2],
    'Y': [18.3, np.nan, 14.1, 19.8, 17.5],
    'Z': [4.2, 3.1, 5.7,np.nan, 9.6]
}

# Create the pandas DataFrame from our dictionary
df = pd.DataFrame(data=d)
dfTest = pd.DataFrame(data=dTest)

# Create the IterativeImputer model to predict missing values
imp = IterativeImputer(max_iter=10, random_state=0)

# Fit the model to the test dataset
imp.fit(dfTest)

# Transform the model on the entire dataset
dfComplete = pd.DataFrame(np.round(imp.transform(df),1), columns=['X','Y','Z'])

print(dfComplete.head(10))
################################
d = {
    'D': [6.9,np.nan,5.4,4.7,4.5,5.1,4.1,4.5,np.nan,7.5],
    'E': [18.5,21.9,np.nan,21.2,12.4,16.7,11,11.5,21.6,np.nan],
    'F': [np.nan,36.3,50.6,48.7,51.9,np.nan,51.6,50.1,46.9,36.6],
    'G': [80,70.1,94.5,np.nan,76.3,84.6,np.nan,93.6,68.9,82]
}

dTest = {
    'D': [5.6,np.nan,4.5,3.2,5.9],
    'E': [16.1,20.7,np.nan,22.4,13.4],
    'F': [np.nan,31.2,53.2,47.8,50.8],
    'G': [79.9,71.3,92.4,np.nan,75.6]
}

# Define df and dfTest as pandas DataFrames 
df = pd.DataFrame(data=d)
dfTest = pd.DataFrame(data=dTest)

# Create the IterativeImputer model to predict missing values
imp = IterativeImputer(max_iter=10, random_state=0)

# Fit the model to the test dataset
imp.fit(dfTest)

# Transform the model on the entire dataset
dfComplete = pd.DataFrame(np.round(imp.transform(df),1), \
                          columns=['D','E','F','G'])

print(dfComplete.head(10))

# Uncomment the following statement to print the result
print(round(dfComplete.mean(),2))
