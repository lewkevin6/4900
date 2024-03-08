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

data_cleaning_1.ipynb was made to create graphs to help me visualize the data. I performed the data cleaning steps listed below, and saved the new data into a CSV file. 

What I did to the:
- Drop N/A values
- Drop "Other" in "Gender" column (only 1 instance)
- Drop "ID" column (Used to identify specific patients not needed for the prediction)
- Manually ordinally encoded categorical values (Wasen't familar with sklearn library at the time)
  
model_test_1.ipynb loaded the cleaned data from data_cleaning_1.ipynb and placed it into a DecisionTreeClassifier. The cleaned data was split into training and testing data sets to train the model. This model was tested using a bunch of metrics (Didn't know much about which metrics to use at the time). The recall score was about 0.07 and the basic model was saved into model_for_app_1.pkl.

# data_cleaning_2 file

Included the first addition of the pipeline, performed the data cleaning steps as listed in data_cleaning_1.ipynb. The difference that I learned to use the sklearn library to encode and scale my data. I pakcaged everything into a pipeline and included a DecisionTreeClassifier in there to predict value.

After packaging everything I trained the model and saved it into model_for_app_2.pkl for the app to use.

# data_cleaning_3 file

This file was created to modify the previous pipeline created to support imblearn. The previous files didnt deal with the imbalanced dataset, after discovering the imblearn library that specifically deals with imbalanced data learning I used one of their over samplers (SMOTENC) to help train my model. The final pipeline was saved into pipeline_for_app_3.pkl for the app to use.

data_cleaning_3_testing.ipynb was created because the imblearn library and the sklearn library didnt interact with eachother properly. This file was made to break down the pipeline to see what steps werent working and to test potential fixes for them. I experimented a lot in this file without the fear of messing up the original file that will ultimately produce the pipeline for the app.

# version_4 file

This is where I tried different models and hyper parameters. Long story short, the best resulting model from our 3 cross validated grid search using F1 score as its metric is the SVC. The file contains more information about its hyper parameters. The SMOTENC over sampling percentage was grid searched aswell.

# version_5 file

I experimented with creating a neural network for my app. I ended up keeping the model from version_4 because the SVN generalized better. Im sure I can fine tune this model even more to make it out perform the SVN, but for now, I will keep using the SVN from file 4.

# Most up to date app consists of "version_4" file + app.py


