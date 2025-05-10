
import nltk
import numpy as np
#nltk.download('punkt_tab')

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentance):
    return nltk.word_tokenize(sentance)

def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
   
   tokenized_sentence = [stem(w) for w in tokenized_sentence]
    
   bag = np.zeros(len(all_words),dtype=np.float32)
   for idx,w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx]  = 1.0

   return bag  

'''
 
sentance =  ["hello","hai","are","you"]     
words = ["hi","hello","I", "hai","bye", "thank" ,"you"]
bag = bag_of_words(sentance,words)   
print(bag)
'''

'''
#***preprocessing***

#tokenization
a = "how are you ?"
print(a)
a = tokenize(a)
print(a)

#stemming
words = ["Organize","organizes","organizing"]
stemmed_words = [stem(w) for w in words]
print(stemmed_words)
'''
