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
*In this section you should provide a more detailed explanation of what, exactly, your Python script(s) actually do.  Your classmates should be able to read your explanation and understand what is happening in the code.*

The code, `needs_a_good_name.py`, begins by importing necessary Python packages:
```
import matplotlib.pyplot as plt
```

- *NOTE:  If a package does not come pre-installed with Anaconda, you'll need to provide instructions for installing that package here.*

We then import data from [insert name of data source].  We print the data to allow us to verify what we've imported:
```
x = [1, 3, 4, 7]
y = [2, 5, 1, 6]

for i in range(0,len(x)):
	print "x[%d] = %f" % (i, x[i])		
```
- *NOTE 1:  This sample code doesn't actually import anything.  You'll need your code to grab live data from an online source.*  
- *NOTE 2:  You will probably also need to clean/filter/re-structure the raw data.  Be sure to include that step.*

Finally, we visualize the data.  We save our plot as a `.png` image:
```
plt.plot(x, y)
plt.savefig('samplefigure.png')	
plt.show()
```

The output from this code is shown below:

![Image of Plot](samplefigure.png)

---

## How to Run the Code
*Provide step-by-step instructions for running the code.  For example, I like to run code from the terminal:*
1. Ensure that you have registered for the [insert name of API] API key.  (You may reference the instructions for doing this.)

2. Ensure that you have installed necessary Python packages. (Again, you may include a reference here to a prior section in the README that provides the instructions.)


2. Open a terminal window.

2. Change directories to where `needs_a_good_name.py` is saved.

3. Type the following command:
	```
	python needs_a_good_name.py
	```

- *NOTE: You are welcome to provide instructions using Anaconda, IPython, or Jupyter notebooks.*

---

## Results from your Analysis
*Last, but not least, you need to demonstrate your results.  You should include figures and/or tables of results.  What worked well?  What could be improved?*



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