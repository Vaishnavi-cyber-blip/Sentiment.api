# Sentiment Analysis Model, API, and Android Application

## Overview
This project includes a sentiment analysis model with 84% accuracy, an API for performing sentiment analysis using Flask, and an Android application that uses the API to analyze sentiment.
## Sentiment Analysis Model
The sentiment analysis model is a machine learning model that has been trained to classify text as positive, negative, or neutral. The model has gained an accuracy of 84%.

### About Dataset
The model was trained using a large Twitter dataset (current X) of text reviews and their corresponding sentiment labels ( Positive:1, Negative:-1, and Neutral:0)

### Data preprocessing
The dataset was preprocessed by cleaning the text that involved removing stop words, removal of numeric values, and punctuation marks, and conversion of letters in their base forms by using the techniques of stemming and lemmatization.

### Algorithms used
TF-IDF (Term Frequency-Inverse Document Frequency) algorithm is used for feature extraction.
 The Logistic Regression CV (aka logit, MaxEnt) classifier is used for classification in the sentiment analysis process.

## Conversion of Model into API using flask




