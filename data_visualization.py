import pandas as pd
import matplotlib.pyplot as plt
original_data = pd.read_csv("healthcare-dataset-stroke-data.csv")

original_data["gender"].value_counts().plot(kind = "bar")

