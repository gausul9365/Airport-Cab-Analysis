#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',',  skip_header = True)


# **Calculate the mean speed of the Cab rides**

# In[ ]:





# In[4]:


speed = taxi[:,7]/(taxi[:,8]/3600)


# In[5]:


mean_speed = speed.mean()


# In[18]:


print(mean_speed)


# **Calculate the number of rides taken in the month of february (feb is given by 2 month column)**

# In[7]:


rides_feb=taxi[taxi[:,1] == 2, 1]


# In[19]:


rides_feb.shape[0]


# **Calulate the number of rides with a tip greater than  50 doller** 

# In[11]:


print(taxi[taxi[:,-3]>50,-3].shape[0])


# **Calculate the number of rides where drop was JFK airport**

# In[13]:


print(taxi[taxi[:,6]==2,6].shape[0])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Calculate the mean speed of the Cab rides**

# **Calculate the number of rides taken in the month of february (feb is given by 2 month column)**

# **Calulate the number of rides with a tip greater than 50 doller**

# **Calculate the number of rides where drop was JFK airport**

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




