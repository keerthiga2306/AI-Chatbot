import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="AI Question Answering",
    page_icon="🤖"
)

st.title("AI Question Answering")
st.write("Ask a question and get an answer from an LLM.")

client = InferenceClient(
  api_key=st.secrets["HF_TOKEN"]
)

question = st.text_area(
    "Enter your question:",
    placeholder="What is artificial intelligence?"
)

if st.button("Ask AI"):
    if question.strip():
        with st.spinner("Generating answer..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

        st.subheader("AI Response")
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please enter a question.")
