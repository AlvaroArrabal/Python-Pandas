import pandas as pd
from math import log

# Series.apply(function)

# Applying operations to series
s = pd.Series([1,2,3,4])

s = s*2
print(s)

s = s/2
print(s)

letters = pd.Series(["a","b","c"])

letters = letters*3
print(letters)

# Applying functions to series

s = s.apply(log)
print(s)

letters = letters.apply(str.upper)
print(letters)

# Apply filters, conditions

s = pd.Series([1,2,3,4,5,6,7,8,9])
print(s[s>2])

# Sort series

s = pd.Series({"Maths":8.5,"Science":5,"Economy":6})

print(s.sort_values(ascending=True))        # Sort the values
print(s.sort_index(ascending=True))         # Sort the index

# Delete null data

s = pd.Series(["a",3,"b","c",None,"d",None,1])
print(s.dropna())