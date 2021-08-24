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
preprocessed = text.lemmatize()
```

```python
preprocessed
```




    [['hello', 'world'], ['NLP', 'fun'], ['-PRON-', 'work', 'bank']]



### TfIDF

```python
get_freq(preprocessed)
```




    ([Counter({'hello': 1, 'world': 1}),
      Counter({'NLP': 1, 'fun': 1}),
      Counter({'-PRON-': 1, 'work': 1, 'bank': 1})],
     ['fun', 'work', 'bank', 'hello', 'NLP', 'world', '-PRON-'])


