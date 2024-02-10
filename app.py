from flask import Flask, request, jsonify
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pickle
import re
import nltk
import string

nltk.download('stopwords')
nltk.download('wordnet')


app = Flask(__name__)

with open('clf.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('tfidf.pkl', 'rb') as f:
    tfidf = pickle.load(f)

stopwords_set = set(stopwords.words('english'))

english_punctuations = string.punctuation
punctuations_list = english_punctuations


def cleaning_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stopwords_set])


def cleaning_punctuations(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def cleaning_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)


def cleaning_URLs(data):
    return re.sub('((www.[^s]+)|(https?://[^s]+))', ' ', data)


def stemming_on_text(data):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in data.split()]


def lemmatizer_on_text(data):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in data.split()]


def preprocessing(text):
    cleaned_text = cleaning_stopwords(text)
    cleaned_text = cleaning_punctuations(cleaned_text)
    cleaned_text = cleaning_repeating_char(cleaned_text)
    cleaned_text = cleaning_URLs(cleaned_text)
    cleaned_text = " ".join(stemming_on_text(cleaned_text))
    cleaned_text = " ".join(lemmatizer_on_text(cleaned_text))

    return cleaned_text


@app.route('/predict', methods=['POST'])
def analyze_sentiment():
    comment = request.form.get('comment')

    preprocessed_comment = preprocessing(comment)

    comment_vector = tfidf.transform([preprocessed_comment])

    sentiment = clf.predict(comment_vector)[0]

    return jsonify({'emotion': sentiment})


if __name__ == '__main__':
    app.run(debug=True)
