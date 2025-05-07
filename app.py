import streamlit as st
import pdfplumber
import json

st.title("PDF Text Extractor")

uploaded_files = st.file_uploader("Upload one or more PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    pdf_texts = {}

    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        with pdfplumber.open(uploaded_file) as pdf:
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
        pdf_texts[file_name] = full_text

    st.subheader("Extracted Text (Preview)")
    for name, text in pdf_texts.items():
        st.write(f"**{name}**")
        st.text_area("", text[:1000] + "..." if len(text) > 1000 else text, height=200)

    # Optional: Show raw JSON
    if st.checkbox("Show raw JSON output"):
        st.json(pdf_texts)
