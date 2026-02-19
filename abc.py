import streamlit as st
from google import genai

# Page configuration
st.set_page_config(page_title="Gemini AI Assistant", layout="wide")
st.title("🤖 Gemini AI Assistant")
st.caption("Enter your API key, ask a question, and get an instant response.")

# Sidebar for API key
with st.sidebar:
    st.header("🔑 API Key")
    api_key = st.text_input("Google AI Studio API key:", type="password")
    st.markdown("---")
    st.markdown("**Get your free API key:**\n1. Go to [Google AI Studio](https://aistudio.google.com/)\n2. Click 'Get API key'\n3. Create or select a project\n4. Copy the key")
    st.info("Your key is only used for this session and is never stored.")

# Main area
if not api_key:
    st.warning("👈 Please enter your API key in the sidebar to start.")
else:
    # Initialize the client with the user's key
    client = genai.Client(api_key=api_key)

    # Question input
    user_question = st.text_area("💬 Your question:", height=120, placeholder="e.g., How does machine learning differ from deep learning?")
    col1, col2 = st.columns([1, 5])
    with col1:
        generate = st.button("🚀 Generate", type="primary")

    if generate:
        if not user_question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Generating answer..."):
                try:
                    # Use a more common model name; adjust if needed
                    # Options: "gemini-2.0-flash-exp", "gemini-1.5-flash", "gemini-1.5-pro"
                    response = client.models.generate_content(
                        model="gemini-3-flash-preview",  # Updated model name
                        contents=user_question
                    )
                    st.subheader("📝 Response:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.info("If the model name is incorrect, try changing it in the code (e.g., to 'gemini-2.0-flash-exp').")