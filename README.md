# Sentiment Analysis Model, API, and Android Application

## Overview
This project includes a sentiment analysis model with 84% accuracy, an API for performing sentiment analysis using Flask, and an Android application that uses the API to analyze sentiment.
## Sentiment Analysis Model
The sentiment analysis model is a machine learning model trained to classify text as positive, negative, or neutral. The model has gained an accuracy of 84%.

### About Dataset
The model was trained using a large Twitter dataset (current X) of more than 160000 text reviews and corresponding sentiment labels ( Positive:1, Negative:-1, and Neutral:0).

### Data preprocessing
The dataset was preprocessed by cleaning the text that involved removing stop words, removal of numeric values, and punctuation marks, and conversion of letters in their base forms using stemming and lemmatization techniques.

### Algorithms used
#### TF-IDF (Term Frequency-Inverse Document Frequency) 
The algorithm is used for feature extraction.
##### Parameters used
###### 'ngram_range=(1,2)' means that both unigrams (single words) and bigrams (pairs of words) will be extracted.
'max_features=5000' means that only the top 5000 most important features will be used in the model. This parameter helps to reduce the dimensionality of the feature space and prevent overfitting.

The Logistic Regression CV (aka logit, MaxEnt) classifier is used for classification in the sentiment analysis process.

## Conversion of Model into API using flask







