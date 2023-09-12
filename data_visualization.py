import pandas as pd
import matplotlib.pyplot as plt
original_data = pd.read_csv("healthcare-dataset-stroke-data.csv")

original_data["gender"].value_counts().plot(kind = "bar")

print(original_data["gender"].value_counts())

#Gender "other" needs to be removed.
#Look at data, look for "other" and remove that row.

print(original_data["gender"].get(3116))


#Removing the row with "Other"
manipulated_data = original_data.drop(3116)

print(manipulated_data["gender"].value_counts())


