Team Members:  
Adhiraj Garg, Adhirajg@buffalo.edu 

Prachi Ramesh Kamble, Prachira@buffalo.edu

Vivek Reddy Duvvuru, Vduvvuru@buffalo.edu

Prashant Bhumireddy , Pbhumire@buffalo.edu



Proposed Project Title:

Weather Forecasting using Python: Analyzing Historical Data for Future Predictions


Option 2 - Online Data Analysis


Data Sources

We are planning to use the data source from Weather API and open-meteo as they contain all the necessary information and parameters we will need for our project.

https://www.weatherapi.com/docs/

https://open-meteo.com/en/docs/historical-weather-api#latitude=42.89&longitude=-78.88&start_date=2023-03-30&end_date=2023-04-13&hourly=temperature_2m

https://archive-api.open-meteo.com/v1/archive?latitude=42.89&longitude=-78.88&start_date=2023-03-30&end_date=2023-04-13&hourly=temperature_2m

Analysis Plan

Analysis steps to be performed:

1.Data Acquisition : 
We will first gather historical weather data from a large number of relevant data sources accessible online, and then retrieve the data via an API.

2.Data cleaning : 
We will clean and preprocess the data once we have collected it to eliminate any missing or inaccurate information.  To prepare the data for use in a regression  model, we may need to normalize or scale it.

3.Variable engineering : 
Once the data has been cleaned and preprocessed, We must extract relevant features for use in our regression model. The purpose of Variable engineering is to identify the most essential variables for weather forecasting and to prepare the data for use in a regression model.

4.Model Selection : 
Once the required characteristics have been collected, we must choose an acceptable regression model to employ for weather forecasting.The model used will be determined by the unique use case and the type of the data.

5.Model Training and Evaluation : 
Using past weather data, we must train the regression model. This entails dividing the data into training and testing sets and training the model using the training set. We must assess the model's performance on the testing set once it has been trained. 

6.Data Interpretation: 
Once we've created a regression model for weather forecasting using historical data, we need to understand the findings. Understanding the patterns and trends in the data and applying the model to provide insights and forecasts is required.

The selected source data for weather forecasting requested through Python is obtained from ‘weather api’ & 'open-meteo', which is historical weather data, is a rich and relevant data source for doing the study. With such a vast dataset  Historical weather data comprises information on previous weather patterns such as temperature, humidity, wind speed, and precipitation, which may be used to determine patterns and trends that might improve future weather forecasts. Python libraries and tools, such as NumPy, Pandas, etc.. can be used to analyze datasets and train a model in python to predict the future weather forecast.

Motivation

Accurate weather forecasting is essential for businesses such as agriculture, transportation, and energy, as well as people who plan outside activities or travel. We can acquire insights into weather patterns and trends by analyzing historical weather data, which may influence future weather predictions and help users make better decisions. We'll also learn about how weather patterns have evolved through time and how they could alter in the future. By analyzing this data, we will be able to apply the programming skills we learned in class to real-world problems.

## Task List


| ID | Task Name |Task Description | Due Date | Status |
| --- | --- | --- | --- | --- |
| 1 |Project Proposal|Decide a topic for the project and submit the proposal on github as a README.md document. | 2023-04-18 | DONE |
| 2 |Data Acquisition |Gathered historical weather data and forecasted weather data from “open-meteo” and retracted it using an API link into our python code. | 2023-04-22| DONE
| 3 |Data Cleaning |Cleaned and preprocessed all the relevant data acquired from the API’s which we will use in our regression model and then displayed it in the form of dataframe(pandas). |2023-04-24 | DONE
| 4 |Variable Engineering |We identified most relevant variables from the API’s that we will need for weather prediction and which can give us more accurate predictions when we use them to train our ‘Regression Model’. |2023-04-26 | DONE
| 5 |Model Selection |We have chosen Regression model for our project |2023-04-28 | DONE
| 6 |Model Training and Evaluation |Training the model with different sets of data, to see which set gives us more accurate predictions and less error when comparing it to the forecasted data we got from our API. Then, we enhance our model by removing the unnecessary information and errors. |2023-04-30 | DONE
| 7 |Saving Model locally for reuse |After getting results from the first model, we need to save that model locally so that we won’t have to retrain that model for future use instead we can just import the saved model and use it.  |2023-05-02 | DONE
| 8 |Data Interpretation |Plot the findings of our model compared to the forecasts extracted by the API to calculate the error and check how close our model is to the actual forecasts. |2023-05-05 | DONE
| 9 |Deployment |Rechecking the code for errors and resolving any issues present and then finally deploying the model for use in the project. |2023-05-07 | DONE
| 10 |Youtube Video |Complete YouTube video and upload to YouTube | 2023-05-16 |  IN PROGRESS
| 11 |Final Report |Upload README.md document to Github | 2023-05-17 | IN PROGRESS

--- 
