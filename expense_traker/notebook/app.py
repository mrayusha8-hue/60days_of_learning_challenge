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
st.write("Key performance Indicators(KPIs) will be be displayed here")
st.divider()

st.caption("Personal Expense Tracker | Built using Python, Pandas and Streamlit")
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