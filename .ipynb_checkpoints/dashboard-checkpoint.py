import pandas as pd
import streamlit as st

# Set the target date
TARGET_DATE = "30-Jan-2024"

# Define file names
top_10_ips_file = f"ips_{TARGET_DATE}.csv"
hourly_traffic_file = f"hourly_traffic_{TARGET_DATE}.csv"
top_85_ips_file = f"ips_85_percent_{TARGET_DATE}.csv"
top_70_hours_file = f"Traffic_70_percent_Overall_Traffic_{TARGET_DATE}.csv"

# Load CSVs into DataFrames
try:
    top_10_ips_data = pd.read_csv(top_10_ips_file)
    hourly_traffic_data = pd.read_csv(hourly_traffic_file)
    top_85_ips_data = pd.read_csv(top_85_ips_file)
    top_70_hours_data = pd.read_csv(top_70_hours_file)
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    st.stop()

# Streamlit Dashboard
st.title(f"Server Traffic Analysis for {TARGET_DATE}")

# 1. Top 10 IP Occurrences
st.subheader("Top 10 IPs by Occurrences")
st.dataframe(top_10_ips_data)

# 2. Hourly Traffic
st.subheader("Hourly Traffic on the Given Day")
st.line_chart(hourly_traffic_data.set_index("Hour"))

# 3. Top 85% Contributing IPs
st.subheader("Top IPs Contributing to 85% of Traffic")
st.dataframe(top_85_ips_data)

# 4. Top Hours Contributing to 70% Traffic
st.subheader("Top Hours Contributing to 70% of Traffic")
st.dataframe(top_70_hours_data)
