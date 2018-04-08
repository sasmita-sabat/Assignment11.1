
# coding: utf-8

# In[1]:


#Consider a DataFrame df where there is an integer column 'X':
#For each value, count the difference back to the previous zero (or the start of the Series, whichever is closer).

import pandas as pd
#list for taking the values for X:
Z=[]
k=input("Number of values that can be in column X ")
for index in range (0,int(k)):
    x=input("Enter the list of values for Column X: ")
    Z.append(x)
#Adding the list in a dataframe
df=pd.DataFrame({'X':Z})
y=0
#Intializing other column for Y holding the result
Y=[]
for index,rows in df.iterrows():
    if(rows[0] == '0'):
        y=0        
    else:        
        y = y + 1
    Y.append(y)
df['Y']=Y
df

