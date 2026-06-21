import pandas as pd

#Series
a = [1, 7, 2]
s = pd.Series(a)
print(s)

#label
a = [1, 7, 2, 5]
s = pd.Series(a, index = ['p','q', 'r','s'])
print(s)
print(s['p'])

#series as dictionary
sub = {"S1": "eng", "S2": "nep"}
s = pd.Series(sub)
print(s)

#Dataframe
data = {
  "SetA" : [1,2,3],
  "SetB" : [4,5,6]
}

df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[[0]])


