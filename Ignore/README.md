# This README.MD will help you understand the files in the "dev" branch and why they were created.

# app.py
This is the python file where the app is launched. It uses a python library called streamlit to create a simple web interface for me to use.

Originally, it took the saved model file model_for_app_1.pkl and loaded that into the app. I then had to convert the user input into something the model was trained on and pass it through.

Now, it takes a pipeline and that handles the conversion.

The app takes in the 10 user inputs that the model sees features and will display whether or not you are likely to have a stroke.
Below are pictures of what the app looks like (They are zoomed out to capture the entire app)

![image](https://github.com/lewkevin6/4900/assets/112120323/baa8b045-00d8-4a8a-b880-16edcb792a66)
![image](https://github.com/lewkevin6/4900/assets/112120323/49bd4a51-51b9-4f47-abd0-7c81b79e2eed)


The app wont change much as the core focus of the project is the machine learning portion.

Use this command in terminal after running app.py: streamlit run /workspaces/4900/app.py

# data_cleaning_1 file

This is the prototype of the project:

data_cleaning_1.pynb was made for the pre-processing steps using graphs to help me visualize the data. I dropped N/A values, manually ordinal encoding (I didn't know much about sk learn library to automate this at the time), and saved the new data into a CSV file. 

model_test_1.ipynb loaded the cleaned data from data_cleaning_1.pynb and placed it into a DecisionTreeClassifier. The cleaned data was split into training and testing data sets to train the model. This model was tested using a bunch of metrics (Didn't know much about which metrics to use at the time). The recall score was about 0.07 and the basic model was saved into model_for_app_1.pkl.

# data_cleaning_2 file
