# 🏗 Domain: Backend Owner

## Responsibility: API layer, Deployment, and Infrastructure

### Current State:
- `api/main.py`: Basic FastAPI routes for prediction and chat.
- `app/streamlit_app.py`: Simple UI for demonstration.
- `docker/Dockerfile`: Multi-service containerization skeleton.

### 📝 Your Tasks:
1. **Build Robust Routes**:
   - Add a `/health` endpoint and proper Pydantic validation for all inputs.
2. **Validation Layer**:
   - Ensure `VehicleData` model handles all edge cases (e.g., negative mileage).
3. **Dockerization**:
   - Split the Dockerfile into a multi-stage build for production.
4. **Logging Middleware**:
   - Add request/response logging for all API calls.

---
*Refer to the project-wide roadmap in the main README.md for the advanced vision.*
