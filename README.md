# Udacity_Data_Scientist_Nanodegree_Projects

### Disaster_Response_Project

In this project, I will build a model to classify messages sent during disasters. There are 36 predefined categories, such as Aid Related, Medical Help, Search And Rescue, and more. By categorizing these messages, we can ensure they reach the appropriate disaster relief agency. To accomplish this, I will develop a basic ETL (Extract, Transform, Load) and Machine Learning pipeline. It's important to note that this is a multi-label classification task, as a message can belong to one or more categories. The dataset we'll be using is provided by Figure Eight and consists of real messages sent during disaster events.

This project will include a web app where people, as an emergency worker, can input a new message and get classification results in several categories. The web app will also display visualizations of the data. 

#### Repository Structure
        disaster_response_pipeline
          |-- app
                |-- templates
                        |-- go.html
                        |-- master.html
                |-- run.py
          |-- data
                |-- disaster_message.csv
                |-- disaster_categories.csv
                |-- DisasterResponse.db
                |-- process_data.py
          |-- models
                |-- classifier.pkl
                |-- train_classifier.py
          |-- Preparation
                |-- categories.csv
                |-- ETL Pipeline Preparation.ipynb
                |-- ETL_Preparation.db
                |-- messages.csv
                |-- ML Pipeline Preparation.ipynb
                |-- README
          |-- README
          
- categories.csv: contains full descriptions of categories 
- messages.csv: contains the messages of real world data 
notebooks: Includes Jupyter Notebooks with the code used for data exploration, visualization, and modeling.

#### List of python libraries used
`sqlalchemy` `pandas` `sklearn` `numpy` `pickle` `NLTK` 

#### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

2. To run ETL pipeline that cleans data and stores in database python data/process_data.py data/messages.csv data/categories.csv data/DisasterResponse.db
To run ML pipeline that trains classifier and saves python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
Run the following command in the app's directory to run your web app. python run.py

3. Go to http://0.0.0.0:3001/
