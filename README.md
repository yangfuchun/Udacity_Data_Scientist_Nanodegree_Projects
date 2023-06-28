# Udacity_Data_Scientist_Nanodegree_Projects
![Udacity Data Scientist Nanodegree Program](![image](https://github.com/yangfuchun/Udacity_Data_Scientist_Nanodegree_Projects/assets/100629848/ffd73cdd-d0e5-4a87-9cce-75e2647b6188))

![Seattle, Washington](![image](https://github.com/yangfuchun/Udacity_Data_Scientist_Nanodegree_Projects/assets/100629848/ad6e0d11-f3bb-4961-9fbf-1b404a66ca66))

### Seattle_Airbnb_Project
Seattle’s Airbnb market offers a diverse range of accommodations, attracting travelers from around the world. In this analysis, we delve into the dynamic pricing trends across different months and uncover the factors that determine whether a host achieves super-host status. Combining insights from both aspects, we gain a comprehensive understanding of the Seattle Airbnb landscape. 

#### Price Trends
The analysis reveals that Airbnb prices in Seattle vary significantly based on the month, with a peak during the summer months, especially in June and July. Understanding these seasonal fluctuations can help hosts optimize pricing strategies and enable guests to plan their trips more effectively.

#### Factors Affecting Superhost Status
By applying a machine learning approach, we identified several key factors that determine whether a host achieves superhost status. These factors include host tenure, responsiveness (response time and rate), acceptance rate, hosting experience (total listings count), and effective communication skills (review scores communication). Hosts can leverage these insights to increase their chances of becoming recognized superhosts and enhancing their reputation on the platform.

#### Property Type and Neighborhood Analysis
My analysis highlights specific neighborhoods and property types that command higher prices in Seattle. Cascade's Boat, Beacon Hill's Camper, Magnolia's Condo, and West Seattle emerged as desirable locations, offering unique experiences and attractive surroundings. Hosts and guests can take these findings into account when selecting accommodations or deciding where to host their properties.

#### Description of files
- [calendar.csv](https://www.kaggle.com/datasets/airbnb/seattle): Contains date, price, and availabiltiy information 
- [listings.csv](https://www.kaggle.com/datasets/airbnb/seattle): Contains rich information such as host profile, neighborhood information, housing conditions 
- [reviews.csv](https://www.kaggle.com/datasets/airbnb/seattle): Contains comments and reviews from reviewers 

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
