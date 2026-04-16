import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# load data
print("Loading data...")
df = pd.read_csv('data/train.csv')

# feature engineering
print("Creating features...")
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['hour']    = df['Date/Time'].dt.hour
df['day']     = df['Date/Time'].dt.day
df['month']   = df['Date/Time'].dt.month
df['weekday'] = df['Date/Time'].dt.weekday

# create hourly demand
hourly_demand = df.groupby(['month', 'day', 'weekday', 'hour']).size().reset_index()
hourly_demand.columns = ['month', 'day', 'weekday', 'hour', 'ride_count']

# features and target
X = hourly_demand[['month', 'day', 'weekday', 'hour']]
y = hourly_demand['ride_count']

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train model
print("Training model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)
print(f"MAE: {mae:.2f} rides")
print(f"R2 Score: {r2:.2f}")

# save model
os.makedirs('models', exist_ok=True)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('models/features.pkl', 'wb') as f:
    pickle.dump(list(X.columns), f)

print("Model saved to models/model.pkl")