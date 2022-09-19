import pandas as pd

s = pd.Series({"Name" : "Alvaro","Surname": "Arrabal","Age":24,"Heigh":1.75,"Birthplace":"Spain"})

print(s)

print(s.size)                   # Returns the length
print(s.index)                  # Returns a list of the names of the rows in the DataFrame
print(s.dtype)                  # Returns the type of the elements

#----------------------------------------
# How to access an element of the series?
# Very similar to arrays
print(s[1])
# The diference is that we can access an element with the variable name as well
print(s["Name"])
# Another diference is that we can enter a list of multiple elements from the series
print(s[["Name","Surname"]])
#----------------------------------------

#----------------------------------------
# Important Functions:

print(s.count())                # Returns the number of non-nulls elements

numbers = pd.Series([1,1,1,2,3,4,4,5,6,4,7,8,9])

print(numbers.sum())            # Returns the sum of the series
print(numbers.cumsum())         # Returns the cumulative sum of the series
print(numbers.value_counts())   # Returns a series with the frequency of the elements
print(numbers.min())
print(numbers.max())
print(numbers.mean())
print(numbers.var())
print(numbers.std())
print(numbers.describe())

