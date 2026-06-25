import streamlit as st
import pandas as pd

st.title("Student Expense Tracker")

category = st.text_input("Category")
amount = st.number_input("Amount", min_value=0.0)

if "expenses" not in st.session_state:
    st.session_state.expenses = []

if st.button("Add Expense"):
    st.session_state.expenses.append(
        {"Category": category, "Amount": amount}
    )

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)

    st.subheader("Expenses")
    st.dataframe(df)

    chart_data = df.groupby("Category")["Amount"].sum()

    st.subheader("Expense Distribution")
    st.bar_chart(chart_data)
