import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Make sure the OPENAI_API_KEY is available
if not os.getenv("OPENAI_API_KEY"):
    st.error("API key not found. Please check your .env file.")
else:
    # Set the API key globally for OpenAI client
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Streamlit App UI
    st.set_page_config(page_title="Ezza Language Translator", page_icon="🌍")
    st.title("Ezza Language Translator")
    st.markdown("Translate from English to Ezza Language using AI.")

    # Input box
    english_text = st.text_area("Enter English text:", height=200)

    # Translate button
    if st.button("Translate"):
        if english_text.strip() == "":
            st.warning("Please enter some text to translate.")
        else:
            with st.spinner("Translating..."):
                try:
                    response = openai.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": "You are a helpful translator that translates English to Ezza language."},
                            {"role": "user", "content": f"Translate the following into Ezza:\n{english_text}"}
                        ],
                        temperature=0.5,
                        max_tokens=300
                    )
                    ezza_translation = response.choices[0].message.content
                    st.success("Translation Complete!")
                    st.markdown("Ezza Translation:")
                    st.text_area("Output:", ezza_translation, height=200)
                except Exception as e:
                    st.error(f"Translation failed: {e}")