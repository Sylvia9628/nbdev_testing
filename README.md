# nbdev_testing
> This is a project to test out nbdev


## Modules

This document explains how to use nbdev_testing

## Install

`pip install nbdev_testing`

## How to use

## Preprocess

### Lemmatize

```
documents =  ["Hello world", "NLP is fun", "We work at the bank"]
text = Preprocess(documents)
preprocessed = text.lemmatize()
```

```
preprocessed
```




    [['hello', 'world'], ['NLP', 'fun'], ['-PRON-', 'work', 'bank']]



## TfIDF tool

### Vocabulary frequency

```
document_frequency, vocabulary = get_freq(preprocessed)
```

```
document_frequency
```




    [Counter({'hello': 1, 'world': 1}),
     Counter({'NLP': 1, 'fun': 1}),
     Counter({'-PRON-': 1, 'work': 1, 'bank': 1})]



```
vocabulary
```




    ['world', 'fun', 'hello', '-PRON-', 'NLP', 'bank', 'work']



## More functions
