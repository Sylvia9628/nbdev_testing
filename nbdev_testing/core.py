# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['preprocess', 'get_freq', 'form_matrix', 'get_query_vec', 'get_cos_sim', 'text', 'documents']

# Cell
import spacy
import nltk
import re
from nltk.corpus import stopwords
from collections import Counter
import numpy as np
import math

# Cell

def preprocess(text):

    """Returns stemmed or lemmatized text with removed punctuation and stopwords
    works on Dutch and English """

    preprocessed_text = []
    nlp = spacy.load('en_core_web_sm')

    text = re.sub(r'[^\w\d\s\']+', '', text)
    doc = nlp(text)

    for token in doc:
        if token.text not in stopwords.words('english'):
            preprocessed_text.append(token.lemma_)

    return preprocessed_text

# Cell
def get_freq(documents):

    "Returns list with vocabulary frequencies per document and a vocabalury list"

    document_frequency = []
    vocab = []

    for page in documents:
        pre = preprocess(page)
        document_frequency.append(Counter(pre))
        vocab = vocab + pre

    vocab = list(set(vocab))
    return document_frequency, vocab

# Cell
def form_matrix(doc_freq, vocabulary):

    """"Returns matrix with td-idf vectors.
    """

    M = []

    for doc in doc_freq:
        arr = np.zeros(len(vocabulary))

        for word in doc.keys():
            tf = doc[word] / (sum(doc.values()))
            freq = 0
            for doc1 in doc_freq:
                if word in doc1.keys():
                    freq+=1

            idf = math.log(len(doc_freq)/(freq+1))
            tfidf = tf * idf
            tfidf_arr = np.array([tfidf])
            index = vocabulary.index(word)
            np.put(arr, index, tfidf_arr)

        M.append(arr)
    return M

# Cell
def get_query_vec(preprocessed_query, vocab, doc_freq):

    "Retun tf-idf vector of input query"


    counter = Counter(preprocessed_query)
    vector = np.zeros(len(vocab))

    for word in preprocessed_query:

        tf = counter[word] * sum(counter.values())
        freq = 0
        for doc in doc_freq:
            if word in doc.keys():
                freq+=1
        idf = math.log(len(doc_freq)/ (freq+1))
        tfidf = tf * idf
        tfidf_arr = np.array([tfidf])
        if word in vocab:
            index = vocab.index(word)
            np.put(vector, index, tfidf_arr)

    return vector

# Cell
def get_cos_sim(matrix, vector):

    "Returns 10 most similar documents based on cosine similarity between documents and query vector"

    cos_sim = []
    for vec in matrix:
        cos = np.dot(vec, vector) / (np.linalg.norm(vec) * np.linalg.norm(vector))
        cos_sim.append(cos)

    array = np.array(cos_sim)
    sort_index = np.argsort(array)[::-1][:10]
    return sort_index

# Cell

text =  "Hello world!"
preprocess(text)

# Cell

assert preprocess("Anne lives in Spain") == ["Anne", "live","Spain"]

# Cell

documents = ["Hello world", "NLP is fun", "We work at the bank"]

document_frequency, vocabulary = get_freq(documents)
vocabulary