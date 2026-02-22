import pandas as pd
import numpy as np
import os
import pickle
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

def train_baseline(feature_path='features/vehicle_features.csv'):
    """
    Trains a baseline XGBoost model.
    """
    if not os.path.exists(feature_path):
        print("Featured data not found. Run engineer_features.py first.")
        return
        
    df = pd.read_csv(feature_path)
    
    # Prepare features
    # Drop target and non-numeric columns for the baseline
    X = df.drop(['Need_Maintenance', 'Last_Service_Date', 'Warranty_Expiry_Date', 'risk_level'], axis=1)
    y = df['Need_Maintenance']
    
    # Encode categorical features
    le = LabelEncoder()
    for col in X.select_dtypes(include=['object']).columns:
        X[col] = le.fit_transform(X[col])
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train XGBoost
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    print("Baseline Model Performance:")
    print(classification_report(y_test, y_pred))
    
    # Save model
    os.makedirs('models', exist_ok=True)
    with open('models/baseline_ml.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model saved to models/baseline_ml.pkl")

if __name__ == "__main__":
    train_baseline()
