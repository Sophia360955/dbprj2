import pymysql
import pandas as pd
import streamlit as st

# Function to establish a connection to the MySQL database
def get_connection():
    return pymysql.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["username"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"],
        port=st.secrets["mysql"]["port"]
    )

# Function to execute a query
def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit App UI
st.title("MySQL Data Viewer")

if st.button("Load Data"):
    query = "SELECT * FROM bookings;"  # Change the query as per your table
    data = run_query(query)
    st.write(data)
