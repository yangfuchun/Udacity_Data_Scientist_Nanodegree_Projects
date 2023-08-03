import sys 

from sqlalchemy import create_engine
import nltk
nltk.download(['punkt', 'wordnet'])

import re
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.multioutput import MultiOutputClassifier
import pickle

def import_data(databaseFile):
    """
    Imports data from an SQLite database and splits it into features (X) and labels (y).

    Args:
        databaseFile (str): Path to the SQLite database file.

    Returns:
        tuple: A tuple containing the following:
            - X (pandas.Series): Input messages.
            - y (pandas.DataFrame): Binary labels for multiple categories.
    """
    engine = create_engine('sqlite:///'+databaseFile)
    df = pd.read_sql_table('DisasterResponse', engine)
    X = df.message
    y = df[df.columns[4:]]
    return X, y

def tokenize(text):
    """
    Tokenizes and preprocesses the input text.

    Args:
        text (str): Input text to be tokenized.

    Returns:
        list: List of clean tokens.
    """
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

def build_model():
    """
    Builds a machine learning pipeline using CountVectorizer, TfidfTransformer, and MultiOutputClassifier.

    Returns:
        sklearn.model_selection.GridSearchCV: Grid search model object.
    """
    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('moc', MultiOutputClassifier(RandomForestClassifier())),
    ])
    parameters = {
        'moc__estimator__n_estimators': [10, 50],
        'moc__estimator__min_samples_split': [2, 5]
    }
    model = GridSearchCV(pipeline, param_grid=parameters)
    return model

def model_eval(model, X_test, y_test):
    """
    Evaluates the model's performance by predicting labels for the test set and printing a classification report.

    Args:
        model: Trained model object.
        X_test (pandas.Series): Test set features.
        y_test (pandas.DataFrame): Test set labels.

    Returns:
        None
    """
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

def save_model(model, modelFile):
    """
    Saves the trained model to a file.

    Args:
        model: Trained model object.
        modelFile (str): Path to save the model file.

    Returns:
        None
    """
    with open(modelFile, 'wb') as file:
        pickle.dump(model, file)



def main():
    if len(sys.argv) == 3:
        databaseFile, modelFile = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(databaseFile))
        X, y = import_data(databaseFile)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, y_train)
        
        print('Evaluating model...')
        model_eval(model, X_test, y_test)

        print('Saving model...\n    MODEL: {}'.format(modelFile))
        save_model(model, modelFile)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')

if __name__ == '__main__':
    main()