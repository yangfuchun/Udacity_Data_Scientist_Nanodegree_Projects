import sys
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

def import_data(messages, categories):

    """
    Imports and preprocesses data from two CSV files, merges them, and performs necessary transformations.

    Args:
        messages (str): Path to the CSV file containing messages data.
        categories (str): Path to the CSV file containing categories data.

    Returns:
        pandas.DataFrame: Merged and preprocessed DataFrame with the following columns:
            - id: Message ID
            - message: Message content
            - original: Original message content (if available)
            - genre: Genre of the message
            - category1: First category label (binary, 0 or 1)
            - category2: Second category label (binary, 0 or 1)
            ...
            - categoryN: Nth category label (binary, 0 or 1)

    """

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
    df.drop('categories', axis=1, inplace=True)
    df = pd.concat([df, categories], axis=1)
    return df



def clean_data(df):
    """
    Removes duplicate rows from the DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame.

    Returns:
        pandas.DataFrame: DataFrame with duplicate rows removed.
    """
    df = df.drop_duplicates()
    return df
    

def save_data(df, databaseName):
    """
    Saves the DataFrame to an SQLite database.

    Args:
        df (pandas.DataFrame): DataFrame to be saved.
        databaseName (str): Name of the SQLite database.

    Returns:
        None
    """
    engine = create_engine('sqlite:///'+databaseName)
    df.to_sql('DisasterResponse', engine, if_exists='replace', index=False)
 

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
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()    