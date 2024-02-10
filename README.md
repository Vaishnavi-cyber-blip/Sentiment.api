# Sentiment Analysis Model, API, and Android Application

## Overview
This project includes a sentiment analysis model with 84% accuracy, an API for performing sentiment analysis using Flask, and an Android application that uses the API to analyze sentiment.
## Sentiment Analysis Model
The sentiment analysis model is a machine learning model trained to classify text as positive, negative, or neutral. The model has gained an accuracy of 84%.

### About Dataset
The model was trained using a large Twitter dataset (current X) of more than 160000 text reviews and corresponding sentiment labels ( Positive:1, Negative:-1, and Neutral:0).

### Data preprocessing
The dataset was preprocessed by cleaning the text which involved removing stop words(i.e. a, an, the, etc), removal of numeric values, and punctuation marks, and conversion of letters in their base forms using stemming and lemmatization techniques.
#### Libraries used - Natural Language toolkit(nltk) and Regular expression (re)

### Algorithms used
#### TF-IDF (Term Frequency-Inverse Document Frequency) 
The algorithm is used for feature extraction.
##### Parameters used
'ngram_range=(1,2)' means that both unigrams (single words) and bigrams (pairs of words) will be extracted.

'max_features=5000' means that only the top 5000 most important features will be used in the model. This parameter helps to reduce the dimensionality of the feature space and prevent overfitting.

#### The Logistic Regression CV (aka logit, MaxEnt) 
The classifier is used for classification in the sentiment analysis process.
It is the variation of Logistic Regression that includes cross-validation to select the best hyperparameters for the model. It uses a technique called "stratified k-fold cross-validation" to ensure that each fold of the dataset contains approximately the same proportion of positive and negative examples. This can help to improve the performance of the model by reducing the risk of overfitting.

## Conversion of Model into API using flask
In this step, we will convert our machine learning model into the application. Python's Flask framework is used to implement this conversion.
### REST API
Representational State Transfer Application Programming Interface helps to build communication between the client and the server, and then the server sends you back the response.

### Basic steps performed: 
#### Saving the machine learning model (Serialization and deserialization):
The 'pickle' module is used to perform this task. Serializing the trained model, we have saved it to a file using the 'pickle.dump()' function, and then later deserialized it using the 'pickle.load()' function to restore the original object.

#### Getting the request data (the input from the user):
As in web applications, user input is sent to the server in the form of an HTTP request. We have used POST request in this application.

#### Loading the pickled predictor:
Once we have preprocessed the user input, we can load the serialized sentiment analysis model from the file using the 'pickle.load()' function. This will restore the original object that allows us to make predictions using the model.

#### jsonify our predictions and send the response back:
The jsonify() function is used to convert the results into a JSON format that can be sent back to the user as an HTTP response.

## Testing and Deployment of API (Usage of tools)

### Testing using Postman
Postman is a popular tool for testing APIs. It allows you to send HTTP requests to a server and view the responses. You can use Postman to test your Flask application by sending requests to the application's endpoints and checking the responses.

### Deployment using Render
'Render' is a cloud platform for deploying web applications. It supports a variety of web frameworks, including Flask. Deploying a Flask application using Render is simple and free with basic services.
























