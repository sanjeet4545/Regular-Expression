#!/usr/bin/env python
# coding: utf-8

# # Regular Expression Practice Questions and Solutions

# In[1]:


import re


# Question 1- Write a RegEx pattern in python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# In[ ]:


pattern = re.compile('[^a-zA-Z0-9]')


# Question 2- Write a RegEx pattern that matches a string that has an a followed by zero or more b's

# In[ ]:


pattern = '^a(b*)$'


# Question 3-  Write a RegEx pattern that matches a string that has an a followed by one or more b's

# In[ ]:


pattern = 'ab+?'


# Question 4- Write a RegEx pattern that matches a string that has an a followed by zero or one 'b'.

# In[ ]:


patterns = 'ab?'


# Question 5- Write a RegEx pattern in python program that matches a string that has an a followed by three 'b'.

# In[ ]:


pattern = 'ab{3}?'


# Question 6- Write a RegEx pattern in python program that matches a string that has an a followed by two to three 'b'.

# In[ ]:


pattern = 'ab{2,3}'


# Question 7- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# In[ ]:


pattern = 'a.*?b$'


# Question 8- Write a RegEx pattern in python program that matches a word at the beginning of a string.

# In[ ]:


pattern = '^\w+'


# Question 9- Write a RegEx pattern in python program that matches a word at the end of a string.

# In[ ]:


pattern = '\w+\S*$'


# In[ ]:


Write a RegEx pattern in python program to find all words that are 4 digits long in a string.


# In[ ]:


pattern = "\b\w{4,}\b"

