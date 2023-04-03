import pandas as pd

# create a dictionary of data
data = {'Name': ['John', 'Emma', 'James', 'Emily'],
        'Age': [24, 27, 22, 31],
        'Gender': ['Male', 'Female', 'Male', 'Female']}

data2 = {'Name': ['John', 'Emma', 'James', 'Emily'],
        'Gender': ['Male', 'Female', 'Male', 'Female']}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

# print(df)
# print(df2.to_csv(None,index=False))
print('Yehudah'.lower().startswith('y'))
