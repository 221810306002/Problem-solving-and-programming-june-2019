#!/usr/bin/env python
# coding: utf-8

# In[5]:


import re
def phonenumbervalidate(phone):
    pattern ='^[6-9][0-9]{9}$'
    phone =str(phone)
    if re.match(pattern,phone):
        return True 
    return False
print(phonenumbervalidate(998855451))
print(phonenumbervalidate(9955441))


# In[10]:


import re
def phonenumbervalidate(phone):
    pattern ='^[0][6-9][0-9]{9}$'
    phone =str(phone)
    if re.match(pattern,phone):
        return True 
    return False
print(phonenumbervalidate("09988554510"))
print(phonenumbervalidate(99554410))


# In[11]:


import re
def validaterollnumber(number):
    
    number =str(number)
    pattern ="^[1][5][2][u][1][A][0][1-9][0-6][0-9]"    
    if re.match(pattern,number):
        return True 
    return False
print(phonenumbervalidate("152u1A0555"))
print(phonenumbervalidate("152u1A0485"))


# In[ ]:




