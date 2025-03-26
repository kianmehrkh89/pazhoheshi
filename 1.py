import pandas as pd

# reading csv file 
df = pd.read_csv("1.csv")
df["name"][0] = "ali"
print(df)
df.to_csv('out.csv', index=False)