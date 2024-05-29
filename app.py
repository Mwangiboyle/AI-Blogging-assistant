import streamlit as st
import google.generativeai as genai
from api_key import google_gemini_api_key, openai_api_key
from openai import OpenAI

client = OpenAI(api_key=openai_api_key)
genai.configure(api_key=google_gemini_api_key)

generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  safety_settings=safety_settings,
  generation_config=generation_config
)

# Title of the app
st.title("✍🤖BlogCraft: Your writing companion")
st.subheader("Now you can craft perfect blogs with the help of AI")

# sidebar for our inputs

with st.sidebar:
    st.title("Input Your blog Details")
    st.subheader("Enter details you want to generate")

    # blog title
    blog_title = st.text_input("Blog Title")
    # keywords input
    keywords = st.text_area("Keywords (Comma separated)")

    # number of words
    num_words = st.slider("Number of Words", min_value=250, max_value=1200,step=250)

    # number of images
    num_images = st.number_input("Number of Images", min_value=1, max_value=5)

    # submit button
    submit_button = st.button("Generate Blog")

    prompt_parts = [f"Generate a comprehensive blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\" make sure to incorporate this keywords in the blog post. The blog post should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is informative and educative and also maintain a consistent tone throughout"]


if submit_button:
    response = model.generate_content(prompt_parts)

    st.write(response.text)
