#!/usr/bin/env python
# coding: utf-8

# In[1]:


test_str = "datascience"
   
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1


# In[2]:


print ("Count of all characters in datascience is :\n "+  str(all_freq))


# In[ ]:




