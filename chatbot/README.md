# 🤖 Domain: LLM Owner

## Responsibility: RAG Pipeline, Prompt Engineering, and Conversational AI

### Current State:
- `llm_data/enrich_text.py`: Generates basic vehicle summaries.
- `rag_pipeline/vector_store.py`: FAISS skeleton for retrieval.
- `chatbot/ai_engine.py`: Basic prompt handling logic.

### 📝 Your Tasks:
1. **Improve Prompt Template**:
   - Refine the explanation prompt to be more empathetic and domain-specific.
2. **Add Memory Handling**:
   - Integrate LangChain's `ConversationBufferMemory` into the `ai_engine.py`.
3. **Embedding Optimization**:
   - Implement recursive character chunking for vehicle manuals in the RAG pipeline.
4. **Evaluation Script**:
   - Create a `llm_eval.py` script to test faithfulness of AI explanations.

---
*Refer to the project-wide roadmap in the main README.md for the advanced vision.*
