# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title = "Personal_Expense_Tracker",
    layout = "wide"
)

# Dashboard Title
st.title("💰 Personal Expense Tracker")

# Project Overview
st.divider()
st.subheader("Project Overview")
st.markdown("This dashboard helps analyze expenses through interactive visualizations.")


# Load Data
df = pd.read_csv("cleaned_expense.csv")
st.success("Data loaded successfully")

st.divider()

# Dashboard Summary
st.header("📊  Dashboard Summary")

# Calculate KPI values
total_expense = df["Amount"].sum()
average_expense = df["Amount"].mean()
highest_expense = df["Amount"].max()
lowest_expense = df["Amount"].min()
total_transactions = df.shape[0]  #len(df) can be used

# Create 4 columns
col1, col2, col3, col4, col5 = st.columns(5)

# Adding KPI card within respective column
with col1:
    st.metric(
        label = "💰 Total Expense",
        value = f" ₹{total_expense:,.2f}"
    )
    
    
with col2:
    st.metric(
        label = "📊 Average Expense",
        value = f" ₹{average_expense:,.2f}"
    )

with col3:
    st.metric(
        label = "💸 Highest Expense",
        value = f" ₹{highest_expense:,.2f}"
    )

with col4:
    st.metric(
        label = "📉 Lowest Expense",
        value = f" ₹{lowest_expense:,.2f}"
)
    
with col5:
    st.metric(
        label = "🧾 Total Transactions",
        value = total_transactions,
        delta = "Total records"
)
st.divider()

#Monthly Expense Section
st.header("📈 Monthly Expense Trend")
st.info(" Monthly expense trend chart will be displayed here.")

st.divider()

#Categort wise Expense
st.header("📂 Category-wise Expenses")
st.info(" This section will display category-wise spending analysis.")

st.divider()

# Pie Chart Section
st.header("🥧 Expense Distribution")
st.info(" Expense distribution by category will be displayed here.")

#Dataset Preview
st.divider()
st.header("📄 Dataset Preview")
st.dataframe(df.head())

# Footer
st.caption("Personal Expense Tracker | Built using Python, Pandas and Streamlit")
st.divider()


