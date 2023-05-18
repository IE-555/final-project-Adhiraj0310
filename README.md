# Write a Brief Descriptive Title Here

Authors:  **Name 1**, **Name 2**, etc.

YouTube Video:  [Link](http://your_link_goes_here)

---

**NOTE**:  The *italicized* content below is for your reference only.  Please remove these comments before submitting.


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
*The purpose of this section is to provide some background about your project.  For example, your introduction should discuss*
- *The purpose of your project;*
- *The type of data you're using;*
- *What you're doing with this data;*
- *What types of analysis you're conducting;*

*Your introduction should make the reader excited to read the rest of this document.*

---

## References
*In this section, provide links to your references and data sources.  For example:*
- Source code was adapted from [the magic source code farm](http://www.amagicalnonexistentplace.com)
- The code retrieves data from [the organization for hosting cool data](http://www.anothermagicalnonexistentplace.com)
- The forecasting models were modified from [some academic research paper](http://www.linktotheacademicpaperyouused.com)

---

## Requirements
*In this section, provide detailed instructions for installing any necessary pre-requisites.  This could include:*
- *Python packages/libraries;*
- *API keys;*
- *etc.*

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
