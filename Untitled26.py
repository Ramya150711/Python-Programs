#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install gensim nltk


# In[4]:


from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import remove_stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
def preprocess_text(text):
    tokens = simple_preprocess(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in stemmed_tokens]
    return lemmatized_tokens
file_path = 'sample_text.txt'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text_data = file.read()
except FileNotFoundError:
    print(f"File '{file_path}' not found. Using inline text as a fallback.")
    text_data = """
    Gensim is a Python library for topic modeling, document indexing, and similarity retrieval. It is built on Numpy and Scipy.
    """
processed_text = preprocess_text(text_data)
print("Original Text:")
print(text_data)
print("\nProcessed Text Tokens:")
print(processed_text)


# In[ ]:




