#!/usr/bin/env python
# coding: utf-8

# In[2]:


import spacy
nlp = spacy.load('en_core_web_sm')

def pos_tagging(sentence):
    doc = nlp(sentence)
    for token in doc:
        print(f'{token.text}: {token.pos_}')
sentence = 'NLP is amazing and fun to learn.'
pos_tagging(sentence)


# In[ ]:




