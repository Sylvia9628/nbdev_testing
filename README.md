# nbdev_testing
> This is a project to test out nbdev


This file will become your README and also the index of your documentation.

## Install

`pip install nbdev_testing`

## How to use

Use the following models to get tdidf vector based on given documents and query

```python
document_frequency, vocabulary = get_freq(["Hello world", "NLP is fun", "We work at the bank"])
matrix = form_matrix(document_frequency, vocabulary)
```

```python
preprocessed_query = preprocess("I like finance")
vector = get_query_vec(preprocessed_query, vocabulary, document_frequency)
```

```python
sorted_index = get_cos_sim(matrix, vector)
```
