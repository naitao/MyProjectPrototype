import pandas as pd

df = pd.read_csv("out.csv")
df.Last_update = df.Last_update.str.replace('\'', '')
#for i in df.index:
    #df.loc[i, ['Last_update']] = df['Last_update'].loc[i].strip('\'')
df.to_csv("new.csv")
