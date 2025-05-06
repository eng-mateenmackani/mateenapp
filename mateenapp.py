import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Mateen's Startup App", layout="centered")

def home_page():
    st.title("💡 Startup Idea Generator")
    st.subheader("Built by Mateen Mackani Far")
    st.markdown("""
    Welcome to **Mateen's Startup Idea Generator App**!

    This app helps you come up with creative and innovative business ideas using AI. 

    Just go to the idea generator page and tell us what you're thinking about!
    """)

def idea_generator_page():
    st.title("🚀 Generate Your Startup Idea")
    user_input = st.text_area("Ask anything for your new business idea or startup:", height=150)

    if st.button("Generate Idea"):
        if user_input.strip() == "":
            st.warning("Please enter a problem or idea to generate.")
        else:
            detailed_prompt = f"""
            You are a helpful assistant. I want you to generate a detailed and thorough response based on the following query:
            
            "{user_input}"
            
            Please provide more context, insights, and details, even if the query is very short. 
            Expand on the topic with explanations, examples, or anything that might help in understanding the subject. 
            Include potential subtopics, history, impact, or related areas if applicable.
            """
            with st.spinner("Generating your startup idea..."):
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(detailed_prompt)
                st.markdown("### 🌟 Your Startup Idea")
                st.markdown(response.text)

page = st.radio("Navigate", ["🏠 Home", "💼 Startup Idea Generator"], horizontal=True, label_visibility="collapsed")

if page == "🏠 Home":
    home_page()
else:
    idea_generator_page()

st.markdown("""---\nMade with ❤️ by **Mateen Mackani Far**""")

st.markdown("""
    [View Streamlit Hosted App](YOUR_STREAMLIT_APP_URL)
    [Visit the GitHub Repository](YOUR_GITHUB_REPO_URL)
""")
