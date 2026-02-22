import pandas as pd
import os

def expert_feature_engineering(df_path='clean_data/vehicle_data_clean.csv'):
    """
    Phase 3: Feature Engineering
    - km_since_last_service
    - aging_factor
    - maintenance_risk_score
    """
    if not os.path.exists(df_path): return
    df = pd.read_csv(df_path)
    
    # 1. Aging Factor
    df['aging_factor'] = df['Vehicle_Age'] * 1.5
    
    # 2. Maintenance Risk Score (0-100)
    df['maintenance_risk_score'] = (
        (df['Reported_Issues'] * 12) + 
        (df['Mileage'] * 0.5) + 
        (df['Vehicle_Age'] * 3)
    ).clip(0, 100)
    
    os.makedirs('features', exist_ok=True)
    df.to_csv('features/vehicle_features.csv', index=False)
    print("Expert features saved to features/vehicle_features.csv")

if __name__ == "__main__":
    expert_feature_engineering()
