# nbdev_testing
> This is a project to test out nbdev


This document explains how to use nbdev_testing

## Install

`pip install nbdev_testing`

## How to use

### Preprocess

```python
documents =  ["Hello world", "NLP is fun", "We work at the bank"]
text = Preprocess(documents)
```

```python
text.lemmatize()
```




    [['hello', 'world'], ['NLP', 'fun'], ['-PRON-', 'work', 'bank']]



```python
document_frequency, vocabulary = get_freq(text.lemmatize())
vocabulary
```




    ['-PRON-', 'NLP', 'fun', 'bank', 'world', 'hello', 'work']



```python
document_frequency
```




    [Counter({'hello': 1, 'world': 1}),
     Counter({'NLP': 1, 'fun': 1}),
     Counter({'-PRON-': 1, 'work': 1, 'bank': 1})]



```python
matrix = form_matrix(document_frequency, vocabulary)
matrix
```




    [array([0.        , 0.        , 0.        , 0.        , 0.20273255,
            0.20273255, 0.        ]),
     array([0.        , 0.20273255, 0.20273255, 0.        , 0.        ,
            0.        , 0.        ]),
     array([0.13515504, 0.        , 0.        , 0.13515504, 0.        ,
            0.        , 0.13515504])]



```python
preprocessed_query = preprocess("They have an interest in finance")
vector = get_query_vec(preprocessed_query, vocabulary, document_frequency)
sorted_index = get_cos_sim(matrix, vector)
sorted_index
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-20-30efa07864b7> in <module>
    ----> 1 preprocessed_query = preprocess("They have an interest in finance")
          2 vector = get_query_vec(preprocessed_query, vocabulary, document_frequency)
          3 sorted_index = get_cos_sim(matrix, vector)
          4 sorted_index
    

    NameError: name 'preprocess' is not defined

