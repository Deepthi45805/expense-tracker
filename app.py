import streamlit as st
import pandas as pd

st.title("Student Expense Tracker")

# Store expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

category = st.selectbox(
    "Category",
    ["Food", "Travel", "Books", "Shopping", "Entertainment", "Other"]
)

amount = st.number_input("Amount", min_value=0.0)

if st.button("Add Expense"):
    st.session_state.expenses.append(
        {"Category": category, "Amount": amount}
    )

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)

    st.subheader("Expense List")
    st.dataframe(df)

    st.subheader("Expense Chart")
    chart_data = df.groupby("Category")["Amount"].sum()
    st.bar_chart(chart_data)
