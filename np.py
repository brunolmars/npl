from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt



def tokenization(n):
    
    text_data = pd.read_csv("text.txt", delimiter=";", names=["text", "label"])
    token_list = []
    
    for text in text_data["text"]:
        tokens = word_tokenize(text)
        token_list.extend(tokens)
        
        assert n <= len(token_list) 
        tokens_lower = [token.lower() for token in token_list]
    
    stop_words = set(stopwords.words('english') + list(punctuation))
    
    filtered_tokens = [token for token in tokens_lower if token not in stop_words]

    plt.rcParams['figure.figsize'] = (20, 8)
        
    word_cloud = " ".join(filtered_tokens)
    wordcloud = WordCloud(width=1000, height=500, background_color='white', min_font_size=10).generate(word_cloud)
    
    plt.imshow(wordcloud)
  

tokenization(100)

