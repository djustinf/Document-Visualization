import logging
import scrape_web
import data_viz
import word_vectors
import random
import gensim
from gensim.models import KeyedVectors
import math

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    text = scrape_web.scrape("http://reprints.longform.org/angels-demons")
    model = word_vectors.genVectors(text.lower())
    #model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

    word = input("What word would you like to see?\n")
    vocab = list(x[0] for x in model.similar_by_word(word))
    vocab.append(word)

    keys = list(model.wv.vocab.keys())
    for i in range(100):
        vocab.append(keys[math.floor(random.random() * len(keys))])

    vocab = list(set(vocab))

    x_values = model[vocab]
    data_viz.projectTo2D_TSNE(vocab, x_values)

if __name__ == '__main__':
    main()
