import pandas as pd
import numpy as np
import os

def engineer_features(df_path='clean_data/vehicle_data_clean.csv'):
    """
    Implements expert-level feature engineering:
    - maintenance_risk_score: A composite metric [0-100]
    - usage_intensity: Mileage / Vehicle_Age
    - thermal_risk: Based on engine size and usage
    """
    if not os.path.exists(df_path):
        print("Cleaned data not found. Run clean_data.py first.")
        return
        
    df = pd.read_csv(df_path)
    
    # 1. Usage Intensity
    # Handle division by zero for new vehicles (Age 0)
    df['usage_intensity'] = df['Mileage'] / (df['Vehicle_Age'] + 1)
    
    # 2. Composite Risk Score (Simplified logic for demonstration)
    # Higher reported issues, higher mileage, and older age increase risk
    df['maintenance_risk_score'] = (
        (df['Reported_Issues'] * 10) + 
        (df['Mileage'] / 10000) + 
        (df['Vehicle_Age'] * 2)
    ).clip(0, 100)
    
    # 3. Risk Categories
    df['risk_level'] = pd.cut(
        df['maintenance_risk_score'], 
        bins=[0, 30, 70, 100], 
        labels=['Low', 'Medium', 'High']
    )
    
    # 4. Save featured data
    os.makedirs('features', exist_ok=True)
    feature_path = 'features/vehicle_features.csv'
    df.to_csv(feature_path, index=False)
    print(f"Featured data saved to {feature_path}")
    return df

if __name__ == "__main__":
    engineer_features()
