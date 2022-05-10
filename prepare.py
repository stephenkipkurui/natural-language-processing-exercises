import re
import json
import nltk
import acquire
import unicodedata
import pandas as pd
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords


def basic_clean(string_data):
    '''
    This function accepts data (string) and lowers the all upper cases, normalize 
    unicode chars, and replace chars that aren't letters, numbers, whitespaces, or single character. 
    '''
    # Strip any data that not words, number or space replacing with space (reject)
    string_data = re.sub(r"[^\w0-9'\s]", '', string_data).lower()
    # Normalize encode data into standard NFKD unicode --> then ACSII code --> back to UTF-8
    string_data = unicodedata.normalize('NFKD', string_data).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return string_data
    
def tokenize(string_data):
    '''
    Function 'breaks' words and or any punctuations into discrete units using natual language tool kit (optimize speed).
    '''
    # Create tokenizer object
    tokenizer = nltk.tokenize.ToktokTokenizer()
    # Use object
    string_data = tokenizer.tokenize(string_data, return_str = True)
    return string_data
        
def stem(string_data):
    '''
    Accepts string data and apply stemming (base form of words). Note stemmed words may 
    not be lexicographically correct (as in english dictionary).
    '''
    # Create the nltk (natural language tool kit) stemmer object, then use it
    ps = nltk.porter.PorterStemmer()
    # Utelize object
    stems = [ps.stem(word) for word in string_data.split()]
    # Join stems
    string_data = ' '.join(stems)
    return string_data
    
def lemmatize(string_data):
    '''
    Similar to stemm but returns lexicographically correct words. Function accepts string data.
    '''
    # Create and fit created object
    wnl = nltk.stem.WordNetLemmatizer()
    # Apply the object (output = list of strings)
    lemmas = [wnl.lemmatize(word) for word in string_data.split()]
    # Joint lemmas
    string_data = ' '.join(lemmas)
    return string_data
  
def remove_stopwords(string_data, extra_words = [], exclude_words = []):
    '''
    This function removes stop words from a string data input. (Stop words are 
    words that have no meaninful singificance in our explorations).
    Function first segments words in linguistic units (other words- tokenization).
    '''
    stopword_list = stopwords.words('english')
    # Utilizing set casting to remove any excluded stopwords
    stopword_list = set(stopword_list) - set(exclude_words)
    # add in any extra words to my stopwords set using a union
    stopword_list = stopword_list.union(set(extra_words))
    
    words = string_data.split()
    filtered_words = [w for w in words if w not in stopword_list]  
    
    stripped_stopwords_data = ' '.join(filtered_words)

    return stripped_stopwords_data


# def remove_stopwords(string_data):
#     '''
#     This function removes stop words from a string data input. (Stop words are 
#     words that have no meaninful singificance in our explorations).
    
#     Function first segments words in linguistic units (other words- tokenization).
#     '''
#     extra_words = [] 
#     exclude_words = []
    
#     num_words = int(input('How many words you wish to add?'))
#     count = 0
#     while count < num_words:
#         extra_words = str(input('Enter etra stopwords to add:'))
#         exclude_words = str(input('Enter etra stopwords to add:'))
#         count += 1
    
#         # Assign stopwords from nltk onto stopwords
#         stopword_list = stopwords.words('english')
#         for word in stopword_list:
#             if (len(extra_words) > 0):
#                 for w in extra_words:
#                     if w not in stopword_list:
#                         stopword_list.append(w)
#             elif len(exclude_words) > 0:
#                 for w in exclude_words:
#                     if w in stopword_list:
#                         stopword_list.remove(w)
#     utilizing set casting, i will remove any excluded stopwords
#     stopword_list = set(stopword_list) - set(exclude_words)
    
#     # Split string data by space
#     words = string_data.split()
#     # Filtered words not in stopwords
#     filtered_words = [w for w in words if w not in stopword_list]  

#     data_with_stripped_stopwords = ' '.join(filtered_words)

#     return data_with_stripped_stopwords


# =======================COMBINED FUNCTION=========================
def prepare_dataframe(df, column, extra_words = [['ha','it']], exclude_words = ['no']):
    '''
    Function combines all prepare function above by performing:
    - Basic clean
    - tekenizing
    - stemming
    - lemmatize
    - removing english stop words
    '''
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords)
    
    df['stemmed'] = df['clean'].apply(stem)
    
    df['lemmatized'] = df['clean'].apply(lemmatize)
    
    return df[['title', column,'clean', 'stemmed', 'lemmatized']]
    

    
    
    
    
    
