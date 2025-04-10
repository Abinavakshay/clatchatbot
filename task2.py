import spacy
import random

# Load SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Sample knowledge base
knowledge_base = {
    "syllabus": "CLAT 2025 syllabus includes English Language, Current Affairs including General Knowledge, Legal Reasoning, Logical Reasoning, and Quantitative Techniques.",
    "english_questions": "The English section usually contains around 28-32 multiple-choice questions.",
    "cutoff_nlsiu": "Last year’s cut-off for NLSIU Bangalore was around 85-90 for general category.",
    "exam_pattern": "CLAT consists of 150 multiple-choice questions to be completed in 2 hours.",
    "application_deadline": "The CLAT 2025 application deadline is expected to be in November 2024.",
    "marking_scheme": "Each correct answer carries 1 mark and 0.25 marks are deducted for every wrong answer."
}

# Basic rule-based matcher
def chatbot_response(query):
    doc = nlp(query.lower())

    if "syllabus" in query:
        return knowledge_base["syllabus"]
    elif "english" in query and "question" in query:
        return knowledge_base["english_questions"]
    elif "cut off" in query or "cut-off" in query and "nlsiu" in query:
        return knowledge_base["cutoff_nlsiu"]
    elif "pattern" in query or "how many questions" in query:
        return knowledge_base["exam_pattern"]
    elif "deadline" in query or "last date" in query:
        return knowledge_base["application_deadline"]
    elif "marking" in query or "negative marking" in query:
        return knowledge_base["marking_scheme"]
    else:
        return "Sorry, I don't have information on that. Please rephrase or ask something else."

# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
