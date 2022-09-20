import pandas as pd

data = {"Country":["Spain","Italy","England","France"],"Capital":["Madrid","Rome","London","Paris"],"Visited?":[True,False,True,True]}

df = pd.DataFrame(data)

print(df.info())                # Returns info of the DataFrame
print("----")
print(df.shape)                 # Returns in a tupple the dimension of the DataFrame
print("----")
print(df.size)                  # Returns how many elements are in the DataFrame
print("----")
print(df.columns)               # Returns a list of all column names
print("----")
print(df.index)                 # Returns a list of all row names
print("----")
print(df.dtypes)                # Returns a series with the types
print("----")
print(df.head(2))               # Returns the first "n" rows of DataFrame
print("----")
print(df.tail(2))               # Returns the last "n" rows of DataFrame
print("----")
# Modifying DataFrame

# We can change the name of the columns and index
df_2 = df.rename(columns={"Capital":"Cities"} , index={0:1000}) 
print(df_2)
print("----")

# We can set a particular index
print(df.set_index("Country").head())
print("----")

# Access to DataFrame
print(df.iloc[2,2])             # Returns a specific element
print(df.iloc[0])               # Returns a specific row

print(df.loc[2,"Capital"])      # 
print(df["Capital"])            # Returns all the column


# Adding new columns
df["Population"] = [100,5555,24,1]  
# You can also enter a series instead of a list
print(df)
