import sys
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

def import_data(messages, categories):
    categories = pd.read_csv(categories)
    messages = pd.read_csv(messages)
    df = messages.merge(categories, on='id', how='inner')
    categories = df["categories"].str.split(';', expand=True)
    row = categories.iloc[0,:]
    category_colnames = row.apply(lambda x: x[:-2])
    categories.columns = category_colnames
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = categories[column].astype(int)
    categories.replace(2, 1, inplace=True)
    df.drop('categories', axis=1, inplace = True)
    df = pd.concat([df, categories], axis=1)
    return df


def clean_data(df):
    df = df.drop_duplicates()
    return df
    

def save_data(df, databaseName):
    engine = create_engine('sqlite:///'+databaseName)
    df.to_sql('DisasterResponse', engine,if_exists = 'replace', index=False)  

def main():
    if len(sys.argv) == 4:

        messagesFile, categoriesFile, databaseFile = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messagesFile, categoriesFile))
        df = import_data(messagesFile, categoriesFile)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(databaseFile))
        save_data(df, databaseFile)
        
        print('Cleaned data saved to database!')
    
    else:
        print('incorrect! please check again.')


if __name__ == '__main__':
    main()    