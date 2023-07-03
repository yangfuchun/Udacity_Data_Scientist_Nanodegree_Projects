# Udacity_Data_Scientist_Nanodegree_Program_Projects

***This repository serves as a collection of the various projects I have completed as part of the Udacity Data Scientist Nanodegree program. Within this repository, you will find a diverse range of projects that showcase my skills and knowledge in the field of data science.***

## Table of Contents 
1. [Seattle_Airbnb_Project](https://github.com/yangfuchun/Udacity_Data_Scientist_Nanodegree_Projects/blob/main/README.md#seattle_airbnb_project)
2. [Disaster_Response_Project](https://github.com/yangfuchun/Udacity_Data_Scientist_Nanodegree_Projects/blob/main/README.md#disaster_response_project)
3. [Recommendations_with_IBM](https://github.com/yangfuchun/Udacity_Data_Scientist_Nanodegree_Projects/blob/main/README.md#recommendations_with_ibm)

## 1. Seattle_Airbnb_Project
![image](https://github.com/yangfuchun/Udacity_Data_Scientist_Nanodegree_Projects/assets/100629848/ad6e0d11-f3bb-4961-9fbf-1b404a66ca66)
Seattle’s Airbnb market offers a diverse range of accommodations, attracting travelers from around the world. In this analysis, we delve into the dynamic pricing trends across different months and uncover the factors that determine whether a host achieves super-host status. Combining insights from both aspects, we gain a comprehensive understanding of the Seattle Airbnb landscape. 

#### Price Trends
The analysis reveals that Airbnb prices in Seattle vary significantly based on the month, with a peak during the summer months, especially in June and July. Understanding these seasonal fluctuations can help hosts optimize pricing strategies and enable guests to plan their trips more effectively.

#### Factors Affecting Superhost Status
By applying a machine learning approach, we identified several key factors that determine whether a host achieves superhost status. These factors include host tenure, responsiveness (response time and rate), acceptance rate, hosting experience (total listings count), and effective communication skills (review scores communication). Hosts can leverage these insights to increase their chances of becoming recognized superhosts and enhancing their reputation on the platform.

#### Property Type and Neighborhood Analysis
My analysis highlights specific neighborhoods and property types that command higher prices in Seattle. Cascade's Boat, Beacon Hill's Camper, Magnolia's Condo, and West Seattle emerged as desirable locations, offering unique experiences and attractive surroundings. Hosts and guests can take these findings into account when selecting accommodations or deciding where to host their properties.

#### Description of files
| Data Files  | Description |
| ------------- | ------------- |
| [calendar.csv](https://www.kaggle.com/datasets/airbnb/seattle)  | Airbnb calendar information including `listing_id` - the unique identifier for the listing, `date` - the date for which the availability and price information is provided, `available` - the listing is available (t) or not (f) on the corresponding date, `price` - the price for the listing on the corresponding date, given that it is available.|
| [listings.csv](https://www.kaggle.com/datasets/airbnb/seattle)  | Airbnb listings in Seattle, including details such as `property` descriptions, `amenities`, `host` information, `location`, `availability`, `pricing`, `review` scores, etc. |
| [reviews.csv](https://www.kaggle.com/datasets/airbnb/seattle)  | Airbnb reviews for specific listing in Seattle, with corresponding information such as the `reviewer's ID`, `name`, `review date`, and their `comments` |

#### List of python libraries used
 `pandas` `sklearn` `numpy` `seaborn` `matplotlib`

## 2. Disaster_Response_Project

In this project, I will build a model to classify messages sent during disasters. There are 36 predefined categories, such as Aid Related, Medical Help, Search And Rescue, and more. By categorizing these messages, we can ensure they reach the appropriate disaster relief agency. To accomplish this, I will develop a basic ETL (Extract, Transform, Load) and Machine Learning pipeline. It's important to note that this is a multi-label classification task, as a message can belong to one or more categories. The dataset we'll be using is provided by Figure Eight and consists of real messages sent during disaster events.

This project will include a web app where people, as an emergency worker, can input a new message and get classification results in several categories. The web app will also display visualizations of the data. 
![image](https://github.com/yangfuchun/Udacity_Data_Scientist_Nanodegree_Projects/assets/100629848/4b1f263e-eb0b-4827-86af-489d1e7a510d)

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
          
#### Description of files
| Folders  | Description |
| ------------- | ------------- |
| App | Templates folder including HTML templates and "run.py" for the web application |
| Data | `disaster_categories.csv`, `disaster_messages.csv` contains full description of categories and messages from past disasters; `DisasterResponse.db` has data cleaned and loaded into an SQLite database; the cleaning code in the final ETL script is `process_data.py` |
| Models | `classifier.pkl` and `train_classifier.py` for the Machine Learning model |
| Preparation | Cleaning, data wrangling, data visualiztions in Jupyter notebooks |

#### List of python libraries used
`sqlalchemy` `pandas` `sklearn` `numpy` `pickle` `NLTK` 

#### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

2. To run ETL pipeline that cleans data and stores in database python data/process_data.py data/messages.csv data/categories.csv data/DisasterResponse.db
To run ML pipeline that trains classifier and saves python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
Run the following command in the app's directory to run your web app. python run.py

3. Go to http://0.0.0.0:3001/
   
## 3. Recommendations_with_IBM
For this project, my objective is to investigate user interactions with articles on the IBM Watson Studio platform. The dashboard above presents a sample layout depicting articles on the IBM Platform. It showcases the latest articles and proposes the inclusion of a personalized recommendation board to highlight articles most pertinent to individual users. To achieve this, I will analyze the available data on the IBM Watson Studio platform, enabling me to determine the most suitable articles to recommend to each user. This study aims to enhance the user experience by providing relevant and engaging content.
![image](https://github.com/yangfuchun/Udacity_Data_Scientist_Nanodegree_Projects/assets/100629848/9e0f4ee1-59f0-4728-b73a-8923e0f0dddf)

#### Description of files
- articles_community.csv: articles available on the IBM platform
- user-item-interactions.csv: list of articles that users interact with
- Recommendations_with_IBM.ipynb: notebook that includes Exploratory Data Analysis, rank-based recommendations, user-user based collaborative filtering, content-based recommendations, and matrix factorization

#### List of python libraries used
`pandas` `numpy` `pickle` `matplotlib` 

## 4. Sparkify_Project

In this project, I will be working with Sparkify, a music streaming service similar to Spotify and Pandora. The goal is to predict user churn, i.e., identify users who are likely to cancel their subscription. By detecting churn in advance, the company can take appropriate measures to retain those users.

#### Description of files
- mini_sparkify_event_data.json: json file that contains user behavior data 

#### List of python libraries used
`pandas` `numpy` `pyspark` `matplotlib` `seaborn` 

For a more detailed blog post please refer to this one: https://medium.com/@yangfchn/sparkify-project-predicting-user-churn-with-apache-spark-ae528e773af0

## Acknowledgements
- Udacity for providing an excellent Data Scientist training program
- Figure 8 for making the disaster messages available for training 
- IBM for providing user-interaction articles dataset 

