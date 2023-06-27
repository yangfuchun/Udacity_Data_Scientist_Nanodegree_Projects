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
    engine = create_engine('sqlite:///'+databaseFile)
    df = pd.read_sql_table('ETL_Preparation', engine)
    X = df.message
    y = df[df.columns[4:]]
    return X, y

def tokenize(text):
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
    pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('moc', MultiOutputClassifier(RandomForestClassifier())),
    ])
    parameters = {
        'clf__estimator__n_estimators': [5],
        'clf__estimator__min_samples_split': [2],
    }
    model = GridSearchCV(pipeline, param_grid=parameters, n_jobs=4, verbose=2, cv=3)
    return model

def model_eval(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

def save_model(model, modelFile):
    with open(modelFile, 'wb') as file:
        pickle.dump(model, file)


def main():
    if len(sys.argv) == 3:
        databaseFile, modelFile = sys.argv[1:]
        print('Importing data...\n    DATABASE: {}'.format(databaseFile))
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
        print('incorrect! please check again. ')


if __name__ == '__main__':
    main()