import os

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Hello Agent", page_icon="📄")
st.title("Hello Agent")
st.caption("Upload one or more CSV files and ask a grounded question.")

uploaded_files = st.file_uploader(
    "Upload CSV files",
    type=["csv"],
    accept_multiple_files=True,
)

if uploaded_files:
    st.subheader("Uploaded files")
    for uploaded_file in uploaded_files:
        st.write(f"- {uploaded_file.name}")
        data = pd.read_csv(uploaded_file)
        st.dataframe(data.head())
else:
    st.info("No CSV files uploaded yet. Add one or more files to begin.")

question = st.text_area(
    "Question",
    value="What is the return policy for electronics?",
    height=120,
)

if st.button("Ask Hello Agent"):
    st.info("Step 1 setup is complete. The CSV grounding and answer logic will be added in the next steps.")
    st.write(f"Question received: {question}")

if __name__ == "__main__":
    pass
