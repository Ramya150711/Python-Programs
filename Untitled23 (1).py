#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_of_evens(n):
    if n < 1:
        print("Please enter a positive integer.")
    total = 0
    for i in range(2, n + 1, 2): 
        total += i
    return total
try:
    n = int(input("Enter a positive integer: "))
    result = sum_of_evens(n)
    print(f"The sum of all even numbers between 1 and {n} is: {result}")
except ValueError:
    print("Invalid input! Please enter a valid positive integer.")


# In[ ]:




