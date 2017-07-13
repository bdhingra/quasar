# Quasar

Datasets accompanying the paper [Quasar: Datasets for QA by Search and Reading].

## Download

Both Quasar-S and Quasar-T are available for download [here](http://curtis.ml.cmu.edu/datasets/quasar/). See the accompanying `readme.txt` for a description of the included files. The release includes:

1. Question sets for train / test / dev splits.
2. Short- and Long-pseudodocuments retrieved by the system described in the paper.
3. For Quasar-S, an overall list of candidates to which all answers belong.
4. For Quasar-T, separate lists of noun phrases extracted from the contexts of each question.
5. Annotations of subset of dev set questions, as described in the paper.

## Explore the Datasets

Below you can find links to the web interface used for evaluating human performance and collecting annotations. This includes an interactive quiz in which the questions are presented one by one, and a search engine for querying the background corpus which you can use in a separate window. Please note that any answers and annotations you enter will be recorded!

Quasar-S: [Quiz](http://murph.ml.cmu.edu/clozemble/so/welcome) | [Search Engine](http://murph.ml.cmu.edu/solr/clozemble-so/browse)

Quasar-T: [Quiz](http://murph.ml.cmu.edu/clozemble/trivia/welcome) | [Search Engine](http://murph.ml.cmu.edu/solr/clozemble-cw/browse)

The search engine used here is Solr, which uses a Lucene backend similar to the search phase described in the paper. The corpus in each case is the set of short pseudodocuments (sentences) pooled across all queries for that corpus, with no query identifiers or tag filtering. This is just a bare-bones search engine guaranteed *not* to yield the exact source sentence for the question (as you'd get by just using Google).

## Citation

If you use these datasets please cite the following:

(To add)
