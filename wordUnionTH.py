
# coding: utf-8

# In[13]:


import pandas as pd


# In[14]:


from pandas import DataFrame, read_csv


# In[15]:


import csv


# In[6]:


tmp = []


# In[16]:


with open(r'C:\Users\Sumonwan\Desktop\Project\outp.csv',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print (row)
        a=row
        tmp=set().union(tmp,a)


# In[8]:


tmp


# In[17]:


with open(r'C:\Users\Sumonwan\Desktop\Project\newCol.csv', 'w',encoding='utf-8') as f:
    for line in tmp:
            f.write(line+",")

