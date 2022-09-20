import pandas as pd

data = {"Country":["Spain","Italy","England","France"],"Capital":["Madrid","Rome","London","Paris"],"Visited?":[True,False,True,True]}

df = pd.DataFrame(data)

print(df)

df.to_excel("C:\\Users\\arrab\\Desktop\\GitHub\\Python-Pandas\\example.xlsx",sheet_name="Hoja2",columns=True,index=False)