#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_word_frequency(text):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts
text = input("Enter a text: ")
frequencies = calculate_word_frequency(text)
print("\nWord Frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")


# In[ ]:




