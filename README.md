A simple chatbot that answers frequently asked questions related to the CLAT exam using keyword matching or NLP-based intent detection (optional: spaCy).

** Features**
- Answers queries like:
  - "What is the CLAT 2025 syllabus?"
  - "How many questions in English?"
  - "What was the cut-off for NLSIU Bangalore?"

## ⚙️ Architecture Summary

- The chatbot receives a question and checks for keywords like `syllabus`, `cut-off`, `marking`, etc.
- It responds from a small hardcoded knowledge base using rule-based logic.
- NLP (spaCy) is optionally used to improve understanding and matching of user input.

## 🚀 Bonus: How to Scale

- Use **fine-tuning on GPT** with NLTI’s FAQ datasets.
- Introduce **retrieval-augmented generation (RAG)** using tools like LangChain or Haystack.
- Add a vector database (like FAISS) for intelligent semantic search.
