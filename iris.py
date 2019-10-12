# importing pandas package
import pandas as pd
from sklearn import datasets
import re

iris=datasets.load_iris()
#print(iris.keys())

df=pd.DataFrame(iris.data)
colnames = iris.feature_names
colnames =list(map(lambda x: re.sub(r"[\s()]", "", x), colnames))
df.columns = colnames
print(df.head(10))

df.drop(columns="")
print(df.sepallengthcm.head(10))



#df.sort_values()
# sorting dataframe
#data.sort_values("Team", inplace=True)

# making boolean series for a team name
#filter = data["Team"] == "Atlanta Hawks"

# filtering data
#data.where(filter, inplace=True)

# display
