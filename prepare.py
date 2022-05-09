import re
import json
import nltk
import acquire
import unicodedata
import pandas as pd
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords


def basic_clean(text):
    '''
    This function accepts data (string) and lowers the all upper cases, normalize 
    unicode chars, and replace chars that aren't letters, numbers, whitespaces, or single character. 
    '''
    text = re.sub(r"[^a-z0-9'\s]", '', text.lower())

    clean_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return clean_text
    
def tokenize(string_data):
    '''
    Function 'breaks' words and or any punctuations into discrete units using natual language tool kit (optimize speed).
    '''
    tokenizer = nltk.tokenize.ToktokTokenizer()

    return tokenizer.tokenize(string_data, return_str = True)
        
def stem(string_data):
    '''
    Accepts string data and apply stemming (base form of words). Note stemmed words may 
    not be lexicographically correct (as in english dictionary).
    '''
    # Create the nltk stemmer object, then use it
    ps = nltk.porter.PorterStemmer()

    stems = [ps.stem(word) for word in string_data.split()]
    stemmed_data = ' '.join(stems)
    return stemmed_data

    
def lemmatize(string_data):
    '''
    Similar to stemm but returns lexicographically correct words. Function accepts string data.
    '''
    # Fit the object
    wnl = nltk.stem.WordNetLemmatizer()
    
    lemmas = [wnl.lemmatize(word) for word in string_data.split()]
    lemmatized_data = ' '.join(lemmas)

    return lemmatized_data
  
def remove_stopwords(string_data):
    '''
    This function removes stop words from a string data input. (Stop words are 
    words that have no meaninful singificance in our explorations).
    
    Function first segments words in linguistic units (other words- tokenization).
    '''
    words = string_data.split()
    stopword_list = stopwords.words('english')
    filtered_words = [w for w in words if w not in stopword_list]
    
    extra_words = ''
    exclude_words = ''
    data_with_stripped_stopwords = ' '.join(filtered_words)

    return data_with_stripped_stopwords

    
    
