import streamlit as st
import pandas as pd
import subprocess

# Load Excel
@st.cache_data
def load_excel(file):
    try:
        df = pd.read_excel(file)
        return df
    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
        return None

# Query Ollama
def query_ollama(prompt, model="llama3:8b"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            capture_output=True,
        )
        if result.returncode == 0:
            return result.stdout.decode("utf-8").strip()
        else:
            return f"Error: {result.stderr.decode('utf-8')}"
    except Exception as e:
        return f"Error running Ollama: {e}"

# Try direct pandas answers for simple questions
def quick_answer(df, query):
    q = query.lower()
    if "revenue" in q and "total" in q:
        if "Revenue" in df.columns:
            return f"Total Revenue = {df['Revenue'].sum()}"
    if "profit" in q and "total" in q:
        if "Profit" in df.columns:
            return f"Total Profit = {df['Profit'].sum()}"
    if "expenses" in q and "total" in q:
        if "Expenses" in df.columns:
            return f"Total Expenses = {df['Expenses'].sum()}"
    return None

# Streamlit App
st.set_page_config(page_title="Financial Q&A Assistant", layout="wide")
st.title("Financial Document Q&A Assistant (Excel)")

uploaded_file = st.file_uploader("Upload Financial Document (Excel)", type=["xlsx", "xls"])

if uploaded_file:
    df = load_excel(uploaded_file)
    if df is not None:
        st.write("Extracted Data Preview")
        st.dataframe(df.head())

        file_text = df.to_string(index=False)

        # Interactive Q&A
        st.write("Ask Questions")
        user_query = st.text_input("Type your financial question...")

        if user_query:
            # Try quick pandas calculation first
            answer = quick_answer(df, user_query)

            if not answer:
                # Fallback to Ollama for complex queries
                prompt = f"""
                You are a financial assistant. The following financial data is provided:

                {file_text[:2000]}  # limit to first 2000 chars to avoid overload

                Answer the following user question clearly and accurately:
                Q: {user_query}
                """
                with st.spinner("Analyzing with Ollama..."):
                    answer = query_ollama(prompt)

            st.success("Answer:")
            st.write(answer)
