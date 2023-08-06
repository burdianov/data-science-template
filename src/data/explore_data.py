import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

data = pd.read_csv("../../data/raw/chipotle.csv")

arr = {1, 2, 3, 4, 5}

print(data.head())
