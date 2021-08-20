# nbdev_testing
> This is a project to test out nbdev


This document explains how to use nbdev_testing

## Install

`pip install nbdev_testing`

## How to use

Use the following models to get tdidf vector based on given documents and query

```
document_frequency, vocabulary = get_freq(["Hello world", "NLP is fun", "We work at the bank"])
vocabulary
```




    ['hello', 'NLP', 'world', '-PRON-', 'fun', 'work', 'bank']



```
matrix = form_matrix(document_frequency, vocabulary)
matrix
```




    [array([0.20273255, 0.        , 0.20273255, 0.        , 0.        ,
            0.        , 0.        ]),
     array([0.        , 0.20273255, 0.        , 0.        , 0.20273255,
            0.        , 0.        ]),
     array([0.        , 0.        , 0.        , 0.13515504, 0.        ,
            0.13515504, 0.13515504])]



```
preprocessed_query = preprocess("They like finance")
vector = get_query_vec(preprocessed_query, vocabulary, document_frequency)
sorted_index = get_cos_sim(matrix, vector)
sorted_index
```




    array([2, 1, 0], dtype=int64)


