# Financial-Q-A-Assistant-

This project is a **Streamlit web application** and a **report generator script** that analyzes financial survey data (Excel format) and produces insights such as most common investment preferences, objectives, and reasons for investing.  

## Features
- Upload an **Excel file** (e.g., Finance_data.xlsx).
- Preview the dataset in a clean web interface.
- Ask **natural language questions** (e.g., "Which investment avenue is most common?" or "How many users prefer Mutual Funds?").
- Answers are provided using a combination of **pandas** (for quick numeric analysis) and **Ollama** local LLMs (for conversational Q&A).

## 🛠 Requirements
Install dependencies before running:
Requirements include:
- streamlit
- pandas
- openpyxl
- ollama (installed separately: https://ollama.ai)

## Running the Web App
1. Start Ollama and make sure a model is available (e.g., llama3:8b).
2. Run the Streamlit app:
3. Upload your Excel file (e.g., Finance_data.xlsx).
4. Ask questions in the input box and view answers.

## Ask Questions

## Type your financial question...

# What percentage of users prefer mutual funds?
# Answer:

Based on the provided financial data, it can be seen that:

User 1 (Female, 34) has invested in Mutual Funds with a factor of 2.
User 2 (Female, 23) has invested in Mutual Funds with a factor of 4.
User 3 (Male, 30) has invested in Equity Market with a factor of 6, which also includes Mutual Funds. However, to make it comparable, let's assume that the user has invested at least 50% of their portfolio in Mutual Funds.
User 4 (Male, 22) has invested in Equity Market with a factor of 3.
Considering these factors, it can be concluded that:

2 out of 4 users have invested in Mutual Funds (Users 1 and 2).
Assuming User 3 has invested at least 50% of their portfolio in Mutual Funds, the total number of users investing in Mutual Funds becomes 3 out of 4.
Therefore, approximately 75% of users prefer Mutual Funds.
