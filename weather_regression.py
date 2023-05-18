import matplotlib.pyplot as plt
import requests
import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle

latitude = 52.52
longitude = 13.41
start_date = "2000-04-01"
end_date = "2023-04-27"
filename = f"test_{latitude}_{longitude}.csv"
filename_forecast = f"test_{latitude}_{longitude}_forecast.csv"

response = requests.get(f"https://archive-api.open-meteo.com/v1/era5?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m")
response = json.loads(response.content)

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

data = fetch_data_from_api_response(response)
data.to_csv(filename,index=False)

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


# csv file to load data from the above experiment
df = pd.read_csv(filename)
df

# build model based on the y_label in the variables
y_label = input("target: ")
model,y_test,y_pred, labels = buildModel(df,y_label)

pickle.dump(model, open('regression_model.pkl', 'wb'))

labels

mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# date to predict
date_to_predict = "2023-05-06"

# print(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m&start_date={date_to_predict}&end_date={date_to_predict}')
response_forecast = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m&start_date={date_to_predict}&end_date={date_to_predict}')
response_forecast = json.loads(response_forecast.content)

data_forecast = fetch_data_from_api_response(response_forecast)
data_forecast

x_forecast = data_forecast.drop(y_label, axis=1)
y_forecast = data_forecast[y_label]

x_forecast
y_forecast

x_forecast = x_forecast.values
y_forecast = y_forecast.values

regression_model = pickle.load(open('regression_model.pkl', 'rb'))

y_forecast_pred = regression_model.predict(x_forecast)

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

y_predicted
y_forecast

mse = mean_squared_error(y_forecast, y_predicted)
print("Mean square error for forecast data : " + str(mse))