# 👨🔬 Domain: ML Owner

## Responsibility: Data Pipeline, Feature Engineering, and Predictive Models

### Current State:
- `data_pipeline/clean_data.py`: Handles basic cleaning and outlier removal.
- `features/engineer_features.py`: Implements basic `maintenance_risk_score`.
- `models/train_baseline.py`: Trains an XGBoost model.

### 📝 Your Tasks:
1. **Improve Feature Engineering**:
   - Add `km_since_last_service` (need to parse `Last_Service_Date`).
   - Implement `thermal_risk_index` based on engine size and usage intensity.
2. **Model Improvement**:
   - Add 2 more metrics to the evaluation (e.g., F1-Score, ROC-AUC).
   - Add confusion matrix plotting in the training script.
3. **Refactor**:
   - Implement a standardized `ModelSave` class to handle versioning.

---
*Refer to the project-wide roadmap in the main README.md for the advanced vision.*
