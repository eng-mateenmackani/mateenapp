import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Startup Idea Generator")

st.title("💡 Startup Idea Generator")

user_input = st.text_input("Ask anything for your new business idea or startup:")

if st.button("Generate Idea") and user_input:
    with st.spinner("Thinking of your next big idea..."):
        prompt = f"""
        You are an expert startup consultant. A user is exploring a startup idea based on the theme: "{user_input}".

        Please provide a detailed startup plan including:
        - Problem being solved
        - Proposed solution
        - Key features
        - Target audience
        - Monetization strategy
        - Potential technologies or platforms
        - Market potential (if possible)

        Make it comprehensive, innovative, and actionable.
        """

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        st.markdown(response.text)

st.divider()
st.markdown("🔧 Built by **Mateen Mackani Far**")
