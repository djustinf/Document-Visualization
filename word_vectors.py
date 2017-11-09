# Justin Foxhoven
# djustinf

import gensim
import nltk
import re

def genVectors(corpus):
    # Remove any garbage characters from the corpus
    regex = re.compile('[^a-zA-Z\s]')
    cleaned_string = regex.sub('', corpus)

    # Cut up the string into nice little pieces
    tokenized = [nltk.word_tokenize(cleaned_string)]

    # Generate the model using word2vec
    model = gensim.models.Word2Vec(tokenized, window=5, min_count=1, size=64)
    return model