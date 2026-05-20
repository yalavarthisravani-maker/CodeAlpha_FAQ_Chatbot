import streamlit as st

st.title("🤖 FAQ Chatbot")

st.write("Ask me questions about AI, Python, Machine Learning, and Internship.")

faqs = {
    "what is ai": "AI means Artificial Intelligence. It helps machines think and work like humans.",
    "what is python": "Python is a simple and popular programming language used for AI, web development, and automation.",
    "what is machine learning": "Machine Learning is a part of AI where computers learn from data.",
    "what is chatbot": "A chatbot is a program that can answer user questions automatically.",
    "what is internship": "An internship gives students practical experience by working on real-world tasks.",
    "what is codealpha": "CodeAlpha provides internship tasks and projects for students.",
    "how are you": "I am fine! How can I help you?",
    "hello": "Hello! Ask me any FAQ question."
}

question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    user_question = question.lower().strip()

    if user_question in faqs:
        st.success(faqs[user_question])
    else:
        st.warning("Sorry, I don't know the answer. Please ask another FAQ question.")