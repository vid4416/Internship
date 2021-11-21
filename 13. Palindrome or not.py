#!/usr/bin/env python
# coding: utf-8

# In[3]:


def isPalindrome(s):
    return s == s[::-1]
 
s = "LEVEL"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")


# In[ ]:




