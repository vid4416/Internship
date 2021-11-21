#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = 11
  
if num > 1:
  
    for i in range(2, int(num/2)+1):
  
        if (num % i) == 0:
            print(num, "is a composite number")
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is a composite number")


# In[ ]:




