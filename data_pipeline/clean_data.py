import pandas as pd
import numpy as np
import os
import kagglehub

def load_and_clean_data():
    """
    Downloads, loads, and cleans the vehicle maintenance dataset.
    - Handles missing values
    - Removes outliers
    - Standardizes categories
    """
    # Download dataset
    path = kagglehub.dataset_download("chavindudulaj/vehicle-maintenance-data")
    csv_path = os.path.join(path, "vehicle_maintenance_data.csv")
    df = pd.read_csv(csv_path)
    
    # 1. Basic Cleaning
    # Remove duplicates
    df = df.drop_duplicates()
    
    # 2. Handle Outliers (Example for Mileage and Engine_Size)
    for col in ['Mileage', 'Engine_Size', 'Odometer_Reading']:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
            
    # 3. Standardization
    # Ensure categorical columns are stripped of whitespace and lowercase
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = df[col].str.strip().str.title() # Keep Title case for readability
        
    # 4. Save cleaned data
    os.makedirs('clean_data', exist_ok=True)
    clean_path = 'clean_data/vehicle_data_clean.csv'
    df.to_csv(clean_path, index=False)
    print(f"Cleaned data saved to {clean_path}")
    return df

if __name__ == "__main__":
    load_and_clean_data()
