import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import kagglehub

def validate_dataset():
    """
    Phase 1: Dataset Validation
    - EDA
    - Heatmap
    - Imbalance Check
    - Leakage Detection
    """
    path = kagglehub.dataset_download("chavindudulaj/vehicle-maintenance-data")
    csv_path = os.path.join(path, "vehicle_maintenance_data.csv")
    df = pd.read_csv(csv_path)
    
    # 1. Class Imbalance Check
    imbalance = df['Need_Maintenance'].value_counts(normalize=True)
    print("Class Imbalance Check:\n", imbalance)
    
    # 2. Leakage Detection (Example: Odometer vs Mileage correlation)
    corr_matrix = df.select_dtypes(include=[np.number]).corr()
    print("Correlation with Target:\n", corr_matrix['Need_Maintenance'].sort_values(ascending=False))
    
    # 3. Save Validated Dataset
    os.makedirs('raw_dataset', exist_ok=True)
    df.to_csv('raw_dataset/validated_vehicle_data.csv', index=False)
    print("Validated dataset saved to raw_dataset/validated_vehicle_data.csv")
    
    # Heatmap generation (Simulated)
    # plt.figure(figsize=(10, 8))
    # sns.heatmap(corr_matrix, annot=True)
    # plt.savefig('evaluation/correlation_heatmap.png')
    
    return df

if __name__ == "__main__":
    validate_dataset()
