import streamlit as st
import random

# Motivational Quotes
quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Stay focused and never give up.",
    "Do something today that your future self will thank you for."
]

# Streamlit UI
st.set_page_config(page_title="Mind Set App", page_icon="🧠", layout="centered")

# Title
st.title("🧠 Mind Set - Stay Motivated!")

# Display Random Quote
st.write("### " + random.choice(quotes))

# Button to Generate New Quote
if st.button("Get Another Quote ✨"):
    st.write("### " + random.choice(quotes))

# Sidebar for Extra Features
st.sidebar.header("More Inspiration")
st.sidebar.write("💡 Stay Positive, Stay Focused!")

# Background Style
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .stTitle {
            color: #2E86C1;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer
st.write("---")
st.write("Made with ❤️ by Madiha Zubair Shah")