import pandas as pd
# create a dataframe with pokemondata

# Set max column display of dataframe
pd.set_option('display.max_columns',20)

#read source data
pdf = pd.read_csv('pokemon.csv')

#convert data to dataframe
df=pd.DataFrame(pdf)

#display source data
#print(df.head(10))

#read header
#print(df.columns)

#read each row in dataframe
#print(df.iloc[0:4])

#filter records in dataframe
df.loc[df['Type 1'] == "Grass"]

#sort dataframe on HP column
df.sort_values("HP",inplace=True)

#sort dataframe on two columns , where order is ascending
# for first and descending for second
df.sort_values(["Type 1","HP"],ascending=[1,0],inplace=True)

# add a new column Total to the dataframe ,
# which is sum of 4 columns integerLocation
df['Total']=df.iloc[:,5:11].sum(axis=1)


# drop a column from a dataframe
df.drop(columns='Total',inplace =True)
#print(df.head(5))

# Get subset of dataframe
sdf=df.loc[:,'HP':'Generation']
#print(sdf.head(5))
#apply function to dataframe
# apply function takes two argument first is fucntion
#why throw error if axis is not mentioned ????
#sdf["HP"]=sdf.apply(lambda x: x['HP']+100,axis=1)
#print(sdf)

#or ... apply function on a column of dataframe for every row

sdf['HP']=sdf['HP'].apply(lambda x: x+2)
#print(sdf.head(10))
#Filter records using lambda function where HP >80
# do operation on other column in the dataframe
sdf.loc[(sdf['HP'] > 85) & (sdf['HP'] < 90),'Speed']=sdf['Speed'] + 10000


def fun(x):
    if x['HP'] <= 87:
        x['Speed'] =0
    else:
        x['Speed'] =1
    return x
# Or


sdf=sdf[(sdf['HP'] > 85) & (sdf['HP'] < 90)]
#sdf.loc[sdf['HP'] > 87 , 'Speed']=sdf['Speed']+100000
#sdf.loc[sdf['HP'] > 87]


#print(sdf)

#what is the difference between apply and applymap ?
#applymap is a dataframe method. Apply fucntion to each element of dataframe


#apply a custom funtion to a records of columns

sdf.apply(lambda x: fun(x),axis=1)
#print(sdf)

#Rank the dataframe on Attack
sdf['Rank']=sdf['Attack'].rank(method='first')
sdf.sort_values('Attack',ascending=True,inplace=True)
print(sdf)

#Groupby and rank on the basis of groups

#concatinate two dataframes

#Merse two dataframes

#Pivot and Pivot tables
