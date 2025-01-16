# pip install pandas
# pip install numpy
# pip install matplotlib

import pandas as pd

try:
	df = pd.read_csv('DataEngineering/Data/developer_dataset.csv')
except FileNotFoundError:
	print("The file 'developer_dataset.csv' does not exist.")
	df = pd.DataFrame()

print(df.columns)

