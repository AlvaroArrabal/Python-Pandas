import pandas as pd

data = {"Country":["Spain","Italy","England","France"],"Capital":["Madrid","Rome","London","Paris"],"Visited?":[True,False,True,True]}

df = pd.DataFrame(data)

print(df)

df.to_excel("example2.xlsx",index=False)