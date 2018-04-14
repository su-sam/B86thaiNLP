
# coding: utf-8

# In[82]:


import pandas as pd


# In[83]:


from pandas import DataFrame, read_csv


# In[84]:


import csv


# In[91]:


with open(r'C:\Users\Sumonwan\Desktop\Project\newCol.csv',encoding='utf-8') as csvfile
    df = csv.reader(csvfile, delimiter=',')
    for j in df:
        print (j)


# In[90]:


df = pd.read_csv(r'C:\Users\Sumonwan\Desktop\Project\newCol.csv');df


# In[43]:


#Count_Row=df.shape[1]; Count_Row


# In[104]:


with open(r'C:\Users\Sumonwan\Desktop\Project\newCol.csv',encoding='utf-8') as csvfile:
    df = csv.reader(csvfile, delimiter=',')
    with open(r'C:\Users\Sumonwan\Desktop\Project\outp2.csv',encoding='utf-8') as csvfile2:#for compare
        reader = csv.reader(csvfile2, delimiter=',')
        for row in reader:
            a=row #word in example
            b=len(a)
            for i in range(b):
                for j in df:
                    for k in range(len(j)):
                        if j[k] is a[i] : 
                            print(a[i],j[k])
                            print(1)
                        else: 
                            print(a[i],j[k])
                            print(0)
                    k=0
                j=0
            i=0

