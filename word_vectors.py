# Justin Foxhoven
# djustinf

import gensim
import nltk
import scrape_web
import re
import logging

def genVectors(corpus):
    # Remove any garbage characters from the corpus
    regex = re.compile('[^a-zA-Z\s]')
    cleaned_string = regex.sub('', corpus)

    # Cut up the string into nice little pieces
    tokenized = [nltk.word_tokenize(cleaned_string)]

    # Generate the model using word2vec
    model = gensim.models.Word2Vec(tokenized, window=5, min_count=1, size=64)
    return model

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    text = scrape_web.scrape("https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing")
    model = genVectors(text)
    print(model.most_similar(positive=['criminal'], negative=None))

if __name__ == '__main__':
    main()