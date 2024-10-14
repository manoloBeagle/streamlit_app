import streamlit as st
import pandas as pd  # Corrected import
import numpy as np   # Corrected import

# Title for the app
st.title('Multi-page Data Dashboard')

page = st.sidebar.radio('Select a Page', ['Overview', 'Sales', 'Expenses', 'Profit'])

# Function to display overview page
def show_overview():
    st.header('Overview')
    return

# Function to display sales page
def show_sales():
    st.header('Sales Dashboard')
    return

def show_expenses():
    st.header('Expenses Dashboard')
    return

def show_profit():
    st.header('Profit Dashboard')  # Changed 'Expenses Profit' to 'Profit Dashboard'
    return

# Navigation logic
if page == 'Overview':
    show_overview()
elif page == 'Sales':
    show_sales()
elif page == 'Expenses':
    show_expenses()
elif page == 'Profit':
    show_profit()

@st.cache_data
def load_data():
    data = pd.DataFrame({
        'Date':pd.date_range(start='2023-01-01', periods=100),
        'Sales': np.random.randint(100, 500, size=100),
        'Expenses': np.random.randint(50, 300, size=100)
    })
    data['Profit'] = data['Sales'] - data['Expenses']
    return data
