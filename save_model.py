import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Load your dataset
df = pd.read_csv('car.csv')  # Replace with your actual dataset

# Features and target
X = df[['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner']]
y = df['selling_price']

# Define preprocessing
categorical_features = ['name', 'fuel', 'seller_type', 'transmission', 'owner']
numerical_features = ['year', 'km_driven']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
    ('num', StandardScaler(), numerical_features)
])

# Build pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor())
])

# Fit model
pipeline.fit(X, y)

# ✅ Save the entire trained pipeline
with open('model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)
