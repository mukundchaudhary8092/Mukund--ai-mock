import streamlit as st

st.set_page_config(
    page_title="Mukund Chaudhary | AI Mock Interview",
    page_icon="🎯",
    layout="centered",
)

st.markdown('''<meta name="author" content="Mukund Chaudhary">
<meta name="description" content="AI Mock Interview Practice System by Mukund Chaudhary">''', unsafe_allow_html=True)

st.title("🎯 AI Mock Interview System")
st.caption("Built by Mukund Chaudhary")
st.markdown("---")

st.subheader("👋 Welcome!")
st.write("Practice interview questions for different tech roles and improve your confidence.")

st.sidebar.header("Interview Setup")
st.sidebar.markdown("**Created by Mukund Chaudhary**")

role = st.sidebar.selectbox("Choose your role", ["Python Developer", "Web Developer", "Data Analyst"])
difficulty = st.sidebar.selectbox("Choose difficulty", ["Easy", "Medium", "Hard"])

questions = {
    "Python Developer": {
        "Easy": ["What is Python and why is it popular?", "What is the difference between a list and a tuple?"],
        "Medium": ["What are decorators in Python?", "Explain list comprehension with an example."],
        "Hard": ["Explain Python's GIL and its effect on multithreading.", "What are generators and when would you use them?"]
    },
    "Web Developer": {
        "Easy": ["What is HTML?", "What is the difference between CSS and JavaScript?"],
        "Medium": ["What is REST API?", "Explain the difference between frontend and backend."],
        "Hard": ["How would you improve web application performance?", "Explain authentication vs authorization."]
    },
    "Data Analyst": {
        "Easy": ["What is data analysis?", "What is the difference between mean and median?"],
        "Medium": ["What is a pivot table?", "Explain the difference between INNER JOIN and LEFT JOIN."],
        "Hard": ["How would you handle missing data in a dataset?", "Explain correlation vs causation."]
    }
}

st.subheader(f"{role} • {difficulty}")
for i, question in enumerate(questions[role][difficulty], start=1):
    st.markdown(f"### Question {i}")
    st.write(question)
    st.text_area("Your answer", key=f"answer_{role}_{difficulty}_{i}", height=120, placeholder="Type your answer here...")

if st.button("✅ Submit Practice", type="primary"):
    st.success("Practice submitted! Review your answers and improve them.")
    st.info("Keep practicing — consistency is the key to interview success.")

st.markdown("---")
st.markdown("<div style='text-align:center; color:gray;'>© 2026 Mukund Chaudhary • AI Mock Interview System</div>", unsafe_allow_html=True)
