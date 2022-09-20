import pandas as pd

data = {"name":["Alvaro","Carmen","David","Cristina"],
"age":[24,24,23,29],
"Eye-Color":["green","brown","brown","honey"],
"home":["Malaga","Estepona","Almeria","Malaga"]}

df = pd.DataFrame(data)
print(df)

df_2 = pd.DataFrame([["Maria",20],["Luis",19],["Marcos",23]], columns=["Name","Age"])
print(df_2)