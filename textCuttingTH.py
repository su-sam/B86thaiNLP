
# coding: utf-8

# In[2]:


from pythainlp.tokenize import word_tokenize


# In[3]:


from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 
 
file = r'C:\Users\Sumonwan\Desktop\Project\B86.csv'
df = pd.read_csv(file)
print(df['CC'])


# In[4]:


Count_Row=df.shape[0] #gives number of row count


# In[7]:


a=df['CC'].values[0];a


# In[48]:


Count_Row


# In[12]:


with open(r'C:\Users\Sumonwan\Desktop\Project\outp.csv', 'w',encoding='utf-8') as f:
    for x in range(0, Count_Row):
        data=df['CC'].values[x]
        print(word_tokenize(data,engine="icu"))
        s = word_tokenize(data,engine="icu")
        for line in s:
            f.write(line+",")
        f.write("\n")

