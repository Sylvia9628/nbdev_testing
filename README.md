# nbdev_testing
> This is a project to test out nbdev


This document explains how to use nbdev_testing

## Install

`pip install nbdev_testing`

## How to use

## Preprocess

### Lemmatize

```python
documents =  ["Hello world", "NLP is fun", "We work at the bank"]
text = Preprocess(documents)
preprocessed = text.lemmatize()
```

```python
preprocessed
```

## TfIDF tool

### Vocabulary frequency

```python
get_freq(preprocessed)
```
