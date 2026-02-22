# 🚀 Advanced Vehicle Maintenance Prediction System

Welcome to the production-grade Predictive Maintenance System. This project bridges structured ML predictors with LLM-powered natural language reasoning.

## 🧭 Roadmap Overview
This project follows a 12-stage advanced roadmap:
0. Problem Framing
1. Dataset Validation
2. Cleaning & Normalization
3. Feature Engineering
4. Classical ML Baseline
5. Neural Models (Experimental)
6. Natural Language Enrichment
7. Instruction Dataset Generation
8. LLM Strategy
9. RAG Pipeline
10. Conversational AI
11. Evaluation & Safety
12. Deployment

## 👥 Ownership Domains
The project is split into three logical domains. Follow the links below for domain-specific tasks and implementation details:

- **👨🔬 ML Owner** ([data_pipeline/README.md](data_pipeline/README.md)): Data, Features, and ML Models.
- **🤖 LLM Owner** ([chatbot/README.md](chatbot/README.md)): RAG, Prompting, and AI Chat.
- **🏗 Backend Owner** ([api/README.md](api/README.md)): FastAPI, Streamlit, and Docker.

## 🛠 Tech Stack
- **Languages**: Python (Pandas, Scikit-learn, XGBoost)
- **AI**: LangChain, FAISS, Sentence-Transformers
- **Backend/UI**: FastAPI, Streamlit, Docker

## 🚀 Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Run data pipeline: `python data_pipeline/clean_data.py`
3. Run features: `python features/engineer_features.py`
4. Start API: `uvicorn api.main:app --reload`
5. Start UI: `streamlit run app/streamlit_app.py`
