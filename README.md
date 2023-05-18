# Weather Forecasting Using Python

Authors:  **Adhiraj Garg**, **Prashant Bhumireddy**,**Vivek Reddy Duvvuru**,**Prachi Kamble** 

YouTube Video:  [Link](http://your_link_goes_here)

---
## Task List


| ID | Task Name |Task Description | Due Date | Status |
| --- | --- | --- | --- | --- |
| 1 |Project Proposal|Decide a topic for the project and submit the proposal on github as a README.md document. | 2023-04-18 | DONE |
| 2 |Data Acquisition |Gathered historical weather data and forecasted weather data from “open-meteo” and retracted it using an API link into our python code. | 2023-04-22| DONE
| 3 |Data Cleaning |Cleaned and preprocessed all the relevant data acquired from the API’s which we will use in our regression model and then displayed it in the form of dataframe(pandas). |2023-04-24 | DONE
| 4 |Variable Engineering sourcing |We identified most relevant parameters from the API’s that are needed for weather prediction and which can give us accurate predictions when trained on a Regression model. |2023-04-26 | DONE
| 5 |Model Selection |We have chosen a variant of regression model for our project |2023-04-28 | DONE
| 6 |Model Training and Evaluation |Training the model with different datasets to identify the suitable dataset with the highest prediction score evaluated against the data from the API. After sufficient exploratory dataset analysis we preprocessed the dataset for redundant features. |2023-04-30 | DONE
| 7 |Saving Model locally for reuse |After observing results from the initial model, we need to save that model as a pre-trained model to use it on test data. The model is saved on a local machine as a pre-trained model to run evaluations on test dataset.  |2023-05-02 | DONE
| 8 |Data Interpretation |Visualizing the predictions from the model and the forecasts extracted from the API to compare and analyze computed error to assess the model close to the API forecast. |2023-05-05 | DONE
| 9 |Deployment |After reviewing the code for any bugs and errors through thorough manual quality assurance, we deploy the model to be used in the project. |2023-05-07 | DONE
| 10 |Youtube Video |Complete YouTube video and upload to YouTube | 2023-05-16 |  IN PROGRESS
| 11 |Final Report |Upload README.md document to Github | 2023-05-17 | IN PROGRESS

--- 

## Introduction
Welcome to this project on weather forecasting using Python!

The purpose of this project is to demonstrate the use of historical weather data to create accurate predictions for future weather conditions.

We will be using a dataset of historical weather data spanning several years, including information on temperature, precipitation, wind speed, and other relevant factors.

Using this data, we will be conducting various types of analysis, such as data cleaning and preprocessing, exploratory data analysis, and building predictive models using machine learning algorithms.

Our aim is to create a robust and accurate forecasting model that can be used to predict future weather conditions with a high degree of certainty.

This project will showcase how Python can be used to handle and analyze large amounts of data, as well as how machine learning can be applied to solve real-world problems such as weather forecasting.

We hope that this project will leave you excited to explore the fascinating world of data analysis and machine learning, and how they can be applied to solve important problems in our daily lives.


---

## References
-HISTORICAL WEATHER DATA was extracted using an API link which is taken from “https://open-meteo.com/en/docs/historical-weather-api#latitude=42.89&longitude=-78.88&start_date=2023-04-13&end_date=2023-04-27&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m”

-FORECASTED WEATHER DATA was extracted using an API link which is taken from “https://open-meteo.com/en/docs#latitude=42.89&longitude=-78.88&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m&start_date=2023-05-01&end_date=2023-05-07”

-The code for the regression model was taken from “OpenAI. (2021). ChatGPT [Computer software]. Retrieved Month Day, Year, from https://openai.com/blog/chatgpt/”

-Code modifications were taken from “https://www.geeksforgeeks.org/”

---

## Requirements
1.To build this model and extract the data from the API’s, we will need to use a few python libraries, some of which might already be pre installed and if they are not you will have to install them in your ipython notebook as follows:

Enter the following commands in your notebook and they will install all the required libraries which we are using. 
! pip install matplotlib

! pip install request

! pip install json

! pip install pandas

! pip install sklearn

! pip install http

! pip install pickle

2. To use the API from the website for data extraction we will first need to check the website for its API link if one is given or sometimes some websites have their API keys and Host link which we can use in our code in the following ways:

response = requests.get(f"https://archive-api.open-meteo.com/v1/era5?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m")
response = json.loads(response.content)
  
                                                                       OR
import requests


url = "https://weatherapi-com.p.rapidapi.com/forecast.json"


querystring = {"q":"<REQUIRED>","days":"3","dt":"2023-05-05"}


headers = {
   "X-RapidAPI-Key": "2df736d9f2msh8a87273ab18ac1ap1d938djsn0a83e34b3d77",
   "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}


response = requests.get(url, headers=headers, params=querystring)


print(response.json()
	
3. We should know the latitude and longitude of the place whose weather we are trying to predict and also the start and end dates for which we need to predict.


---

## Explanation of the Code

1.Importing all the libraries we installed using the above commands: 

import matplotlib.pyplot as plt
	
import requests
	
import json
	
import pandas as pd
	
from sklearn.linear_model import LinearRegression
	
from sklearn.model_selection import train_test_split
	
from sklearn.metrics import mean_squared_error
	
import pickle

2.Now we initialize our code with some variables like :
	
Latitude and longitude of the place whose weather we want to predict
	
Start and end date to retract History Weather data from the API which we will use to train our model.
	
Creating two different file names to save the History Weather Data( for training) and Forecasted weather data(for testing i.e predicting) which will automatically change based on the coordinates of the location given by us.(we can print the filename just to check if it's in the correct format using the commands ‘filename’ , ’filename_forecast’)
	
Date to predict
	
Target value which we need to predict.(example-> ‘temperature’,’wind speed’ etc.)
	
3.Importing Data from the Website using the API links:
	
response = requests.get(f"https://archive-api.open-meteo.com/v1/era5?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m")
response = json.loads(response.content)

4.Adaptor code used to convert api response to dataframe used to train the model
def fetch_data_from_api_response(response):
   temp_col = response["hourly"]["temperature_2m"]
   humidity_col= response["hourly"] ["relativehumidity_2m"]
   ppt_col=response["hourly"] ["precipitation"]
   wind_col= response["hourly"] ["windspeed_10m"]
   data_dict = {
       # "time":time_col,
       "temperature":temp_col,
       "humidity":humidity_col,
       "precipitation":ppt_col,
       "windspeed":wind_col
   }
   weather_data = pd.DataFrame(data_dict)
   return weather_data

5.Used the method mentioned above and stored the data in csv format
	
data = fetch_data_from_api_response(response)
data.to_csv(filename,index=False)


6.Function used to clean the None values from the dataframe and split the data in train test with 20% for test data and trained the model using LinearRegression() for the column specified in the parameter of the function. This function will return 4 values (trained model, target test values, target predicted values and columns used to train the model).

def buildModel(df, y_column):
   # dropping all the rows with None values
   df = df.dropna(how='all')
   # drop column with name temperature from X ( i.e seperating input data and target)
   X = df.drop(y_column, axis=1)
   X_values = X.values


   # target in this case is temperature
   y = df[y_column]


   X_train, X_test, y_train, y_test = train_test_split(X_values, y, test_size=0.2, random_state=42)


   model = LinearRegression()
   model.fit(X_train, y_train)
  
   y_pred = model.predict(X_test)


   return model,y_test,y_pred,X.columns.values

7.Target label is taken as user input. Need to give a label as any one of the column names from the output of step 5.
	
y_label = input("target")
model,y_test,y_pred, labels = buildModel(df,y_label)
	
8.Saved model in local to reuse again
	
pickle.dump(model, open('regression_model.pkl', 'wb'))
	
9.Code used to calculate the mean square error between predicted(generated from the model created above) and actual target values for test data.
	
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)


10.Load the model saved in pickle format in step 8.
	
regression_model = pickle.load(open('regression_model.pkl', 'rb'))
	
11.Part-II is to fetch forecast data from open-meteo api based on the same latitude and longitude used to fetch historical data to train the model.
	
# print(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m&start_date={date_to_predict}&end_date={date_to_predict}')
response_forecast = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m&start_date={date_to_predict}&end_date={date_to_predict}')
response_forecast = json.loads(response_forecast.content)

12.We reuse the same function used to build dataframe from the api response mentioned in step 4.
	
data_forecast = fetch_data_from_api_response(response_forecast)
data_forecast

13.Splitting the forecast data into input and target data
	
x_forecast = data_forecast.drop(y_label, axis=1)
y_forecast = data_forecast[y_label]


14.Predict forecast values of y_label ( taken as input from user ) based on the model loaded from local in step 8.
	
y_forecast_pred = regression_model.predict(x_forecast)

15.Function used to plot comparison graph between predicted and actual target forecast values.


def plot_predicted(y_forecast, y_predicted):
   x = [i for i in range(1,25)]
   plt.plot(x,y_forecast)
   plt.plot(x,y_predicted)
   plt.ylabel(y_label)
   plt.xlabel("Hour in a day")
   plt.title("Predicted " + y_label + " VS " + "Forecasted " + y_label)
   plt.legend(['Forecast', 'Predicted'])
   plt.show()
   return y_forecast, y_predicted
y_forecast, y_predicted  = plot_predicted(y_forecast, y_forecast_pred)
	
	


---
## How to Run the Code

### Environment

Install the required dependencies

```python
pip install -r requirements.txt
```

**Note:** Use pip or pip3 in the above command as per your pip env variable name.

### Execution

**Running python file**

There is one python file i.e., `weather_regression.py` which requires one of the following enumeration for standard IO input as target for modeling. Use one of the following strings as input for execution.

```
temperature
humidity
precipitation
windspeed
```

Ensure the input is one of these names as it is an enuremation.

To run the file, from the project root directory

```
python3 weather_regression.py
```

**Note:** Use python or python3 in the above command as per your Python env variable name of the version you are using.

You will be prompted to provide input when the program starts running, then provide one of the target names mentioned above.

**Notebook**

If you are using Anaconda or Jupyter setup or VS Code python notebook setup, then you can execute the `weather_regresion.ipynb` notebook file by running all cells of the notebook. 

In VSCode, you will find this Run All button to execute this code. Follow the top floating prompt to input the target when asked in the code(from 10th cell) and hit 'Enter' to pass the input enumeration string. 

![VSCodeRunAll](image/README/VSCodeRunAll.png)

##Results
	
1.Temperature:

We got the forecasted values of temperature from the API, and we got the predicted values of temperature for the given coordinates of latitude and longitude using our python model.After comparing them we plotted the comparison graph as follows:


We also got the values of Temperature for the date/dates for which we predicted the Temperature using our model and after comparing them we find that the predicted values are close to the forecasted values which we obtained and we also found the mean squared error which is 26.481181490915063. To reduce the error even further we can train our model for a much longer period but as we know that weather prediction is not always accurate and even the forecasted values from the API can be wrong.

2. Humidity:

We got the forecasted values of Humidity from the API, and we got the predicted values of Humidity for the given coordinates of latitude and longitude using our python model.After comparing them we plotted the comparison graph as follows:


We also got the values of Humidity for the date/dates for which we predicted the temperature using our model and after comparing them we find that the predicted values are getting closer to the forecasted values which we obtained and we also found the mean squared error which is 209.18585374612323. To reduce the error even further we can train our model for a much longer period but as we know that weather prediction is not always accurate and even the forecasted values from the API can be wrong.

3. Precipitation


We also got the values of Precipitation for the date/dates for which we predicted the Precipitation using our model and after comparing them we find that the predicted values are getting closer to the forecasted values which we obtained and we also found the mean squared error which is 1.2360902458370944.In this case we don’t have to do much as the error is very small. 
	
4. Windspeed


We also got the values of Wind speed for the date/dates for which we predicted the Wind speed using our model and after comparing them we find that the predicted values are getting closer to the forecasted values which we obtained and we also found the mean squared error which is 17.8038854228414.We can reduce the model buy further training the model but there is no guarantee that the error will become 0 as weather prediction is a difficult task and the forecasted values can be wrong.
	
# **Prospective Development Directions**

The current model of linear regression for forecasting climatic conditions showcases remarkable predictive proficiency. Nevertheless, there exist several opportunities to augment and refine the model further. Here's a roadmap for potential enhancements and directions for future developments:

1. **Inclusion of broader variables** : The complexity of weather patterns is informed by numerous factors. Enriching our model with a greater variety of variables like relative humidity, wind velocity, barometric pressure, and others could substantially upgrade the precision of our predictions. Additionally, analyzing the influence of unconventional variables such as the indices of El Niño Southern Oscillation (ENSO) could provide compelling insights.
2. **Extension of data coverage** : Broadening the range of our data, both temporally (integrating data from further in the past) and spatially (incorporating data from more geographical locations), can reinforce the reliability of our model and enhance its capacity to adapt to diverse conditions.
3. **Exploration of advanced models** : Despite linear regression serving as an excellent foundational tool, more intricate models might better encapsulate the intricacies of climatic forecasting. Techniques including polynomial regression, support vector regression, or artificial neural networks could be investigated.
4. **Integration of interaction variables** : The interplay between different weather variables can often be complex and non-linear. By including interaction variables in our regression model, we can better capture these interdependencies.
5. **Employment of time-series methodologies** : Given the temporal nature of climatic data, deploying models specifically designed for time-series analysis, such as ARIMA or LSTM models, might enhance the fidelity of our predictions.
6. **Focus on outlier detection** : In addition to improving overall predictive accuracy, future research could also prioritize the forecast of severe climatic phenomena. Considering their propensity to inflict substantial damage, devising a model capable of predicting such occurrences reliably is of paramount importance.
7. **Optimization of computational efficiency** : With the escalation in data volume and model complexity, the aspect of computational efficiency gains significance. Future endeavors could concentrate on refining our coding practices and deploying more efficient algorithms to process large data sets.

By exploring these approaches, we hope to continually refine and enhance our weather prediction model, driving the frontiers of accurate, reliable weather forecasting.
	

