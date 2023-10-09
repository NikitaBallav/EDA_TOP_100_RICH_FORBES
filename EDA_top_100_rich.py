#!/usr/bin/env python
# coding: utf-8

# # EDA with Python
# 

# ## Dataset: Top 100 richest people
# 
# ### Objective:
# - 1.To find the range of age for the people to get rich(very well stabled).
# - 2.Comparing Male and Female regarding age

# ## Step 1: Import libraries

# In[1]:


import pandas as pd #read the dataset
import numpy as np #work with arrays
import matplotlib.pyplot as plt #visualisation
import seaborn as sns #visualisation of data, statistical concept
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Step 2: Reading the file in pandas dataframe

# In[2]:


rich=pd.read_csv('top_100_richest_dataset.csv')
rich[:3] 


# ### inserting a required column

# In[3]:


x=list(range(1,101))
rich.insert(0,'rank',x)
rich


# In[4]:


rich.head() # printing 1st 5 datapoints


# In[5]:


rich.tail() # printing last 5 datapoints


# ## Step 3: knowing the dataset

# In[6]:


# getting all the datatypes
rich.dtypes


# In[7]:


rich.shape # dimension of dataset


# In[8]:


rich.nunique() # number of unique values in each datapoints


# In[9]:


a=rich['age'].unique()
a


# In[10]:


b=rich['nationality'].unique()
b


# In[11]:


c=rich["gender"].unique()
c


# In[12]:


d=rich["net_worth"].unique()
d


# ## Step 4: Cleaning the data

# In[13]:


# checking for null values
rich.isnull().sum()


# In[14]:


# checking the datapoints with NaN age values
rich[rich['age'].isnull()]


# ### filling the missing values available or updating it with 0

# In[15]:


rich.loc[10,'age']=72
rich.loc[20,'age']=67
rich.loc[56,'age']=0
rich.loc[80,'age']=0
rich.loc[87,'age']=79


# In[16]:


display(rich.iloc[10])
display(rich.iloc[20])
display(rich.iloc[56])
display(rich.iloc[80])
display(rich.iloc[87])


# In[17]:


rich[rich['age'].isnull()] # no null are left for age


# In[18]:


# checking the datapoints with NaN age values
rich[rich['bday'].isnull()]


# ### 1. since bday would not be helping in any conclusion
# ### 2. updating the data by droping bday

# In[19]:


R=rich.drop(["bday"],axis=1)


# In[20]:


R.head()


# In[21]:


R.isnull().sum()


# ## Step 5: EDA
# ### 1.Univariate non-graphical
# - variable: age

# In[22]:


# measures of central tendency
R.describe()


# In[23]:


# mode
import statistics
mod=statistics.multimode(R['age'])
print(mod)
# most frequently occured age is 65 and 86


# ### 1. skewness: to measure the symmetry of the distribution while
# ### 2. kurtosis: determines the volume of the outliers

# In[25]:


print(R["age"].astype(float).skew()) # asymmetric


# ### negatively skewed: tail of the distribution is longer towards the left hand side of the curve
# 

# In[26]:


print(R["age"].astype(float).kurt()) # leptokurtic
 # higher than normal distribution


# ### Observations:
# - The above measures gives an analysis about the age in the given dataset: Majority of people lies in the age group beyond the mean value

# ### 2. Multivariate non-graphical
# - cross tabulation: frequency distributions

# In[27]:


# variable: net_worth and gender
cross_table=pd.crosstab(R.net_worth,R.gender,margins=True)
cross_table


# In[28]:


# variable: age and gender
cross_table=pd.crosstab(R.age,R.gender,margins=True)
cross_table


# ### These above tabulations shows that :
# - In total there are 10 females and 90 males.
# - Most frequently occurred age is 65 and 86.

# ### 3.Unvariate Graphical
# - variable: age
# #### histograms
# 

# In[30]:


sns.displot(R["age"],height=5,aspect=1)


# #### boxplots

# In[31]:


sns.catplot(y="age",kind="box",data=R) # outlier with the value zero


# #### univariate scatter plot

# In[32]:


sns.scatterplot(x=R.index,y=R["age"],hue=R["gender"])


# #### univariate swarmplot

# In[33]:


sns.swarmplot(x=R["age"])


# ### Observations:
# 1. Histogram: People within the age group of 62 to 80 are the maximum.
# 2. Boxplot: Age=0 is the outlier in the given dataset.
# 3. Scatter plot and Swarmplot: Actual age is ranging from 36 to 97.
# 

# ### Multivariate Graphical

# #### scatter plots

# In[35]:


sns.relplot(x="rank",y="nationality",hue="gender",data=R,kind="scatter")


# In[36]:


sns.relplot(x="age",y="nationality",hue="gender",data=R)


# In[37]:


sns.swarmplot(x=R["age"],y=R["gender"])


# In[38]:


sns.pairplot(data=R,hue="gender")


# In[39]:


sns.displot(data=R,x="age",y="net_worth",hue="gender",height=10,aspect=1)


# ### Observations:
# 1. Scatterplot: USA has the most diversity of ages and rankings corresponding to net_worth.
# 2. Swarmplot and pairplot: Male varies from 36 to 97 age group whereas females are 58 to 82.
# 3. Multivariate histogram: Net_worth for male lies in the interval (16 to 240 billion dollar) whereas for female it lies in interval (18 to 70 billion dollars).

# In[ ]:




