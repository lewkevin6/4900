import pandas as pd
original_data = pd.read_csv("healthcare-dataset-stroke-data.csv")

print(original_data.info())

#BMI contains 4909/5110 null values

new_data = original_data.dropna()

new_data.info()

