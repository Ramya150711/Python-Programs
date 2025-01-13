#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install spacy


# In[4]:


get_ipython().system('python -m spacy download en_core_web_sm')


# In[6]:


import nltk
from nltk.corpus import stopwords
import spacy

# Download the NLTK stopwords list
nltk.download('stopwords')

# Load SpaCy's English model
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    # Convert text to lowercase
    text_lower = text.lower()
    
    # Tokenize the text using SpaCy
    doc = nlp(text_lower)
    
    # Get the list of NLTK stopwords
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords
    filtered_words = [token.text for token in doc if token.text not in stop_words]
    
    return filtered_words

# Input text
text = input("Enter the text: ")

# Process the text
result = process_text(text)

# Display the result
print("Processed text without stopwords:")
print(" ".join(result))


# In[ ]:




