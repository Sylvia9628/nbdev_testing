# nbdev_testing
> This is a project to test out nbdev



<h4 id="Preprocess.lemmatize" class="doc_header"><code>Preprocess.lemmatize</code><a href="https://github.com/Sylvia9628/nbdev_testing/tree/master/nbdev_testing/preprocess.py#L18" class="source_link" style="float:right">[source]</a></h4>

> <code>Preprocess.lemmatize</code>()

`Returns stemmed or lemmatized documents with punctuation and stopwords removed`



<h4 id="get_freq" class="doc_header"><code>get_freq</code><a href="https://github.com/Sylvia9628/nbdev_testing/tree/master/nbdev_testing/tfidf.py#L13" class="source_link" style="float:right">[source]</a></h4>

> <code>get_freq</code>(**`preprocessed_documents`**)

Returns list with vocabulary frequencies per document and a vocabalury list



<h4 id="form_matrix" class="doc_header"><code>form_matrix</code><a href="https://github.com/Sylvia9628/nbdev_testing/tree/master/nbdev_testing/tfidf.py#L30" class="source_link" style="float:right">[source]</a></h4>

> <code>form_matrix</code>(**`doc_freq`**, **`vocabulary`**)

Returns matrix with td-idf vectors.



<h4 id="get_query_vec" class="doc_header"><code>get_query_vec</code><a href="https://github.com/Sylvia9628/nbdev_testing/tree/master/nbdev_testing/tfidf.py#L58" class="source_link" style="float:right">[source]</a></h4>

> <code>get_query_vec</code>(**`preprocessed_query`**, **`vocab`**, **`doc_freq`**)

Retun tf-idf vector of input query



<h4 id="get_cos_sim" class="doc_header"><code>get_cos_sim</code><a href="https://github.com/Sylvia9628/nbdev_testing/tree/master/nbdev_testing/tfidf.py#L85" class="source_link" style="float:right">[source]</a></h4>

> <code>get_cos_sim</code>(**`matrix`**, **`vector`**)

Returns 10 most similar documents based on cosine similarity between documents and query vector


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




    ['NLP', 'world', 'fun', 'work', 'bank', 'hello', '-PRON-']



## More functions
