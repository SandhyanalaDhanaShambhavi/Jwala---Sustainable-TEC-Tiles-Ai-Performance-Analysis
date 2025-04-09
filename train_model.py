import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Make sure you have your training data in 'data/sample_data.csv'
df = pd.read_csv("data/sample_data.csv")
X = df.drop("Output_Power", axis=1)
y = df["Output_Power"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "models/tec_model.pkl")
print("Model trained and saved to models/tec_model.pkl")

# Run this file once from the terminal: python train_model.py