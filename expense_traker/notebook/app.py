import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title = "Personal_Expense_Tracker",
    layout = "wide"
)

# Title
st.title("Personal_Expense_Tracker")

#Project Overview
st.divider()
st.subheader("Project Overview")
st.write("This dashboard helps analyze expenses through interactive visualizations.")



df = pd.read_csv("cleaned_expense.csv")
st.write(df)