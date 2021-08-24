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


