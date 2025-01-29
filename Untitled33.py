#!/usr/bin/env python
# coding: utf-8

# In[2]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt
def generate_wordcloud(text, image_filename):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  
    plt.show()
    wordcloud.to_file(image_filename)
    print(f"WordCloud image saved as {image_filename}")
text = 'data science machine learning artificial intelligence'
generate_wordcloud(text, 'wordcloud.png')


# In[ ]:




