import pandas as pd
import streamlit as st


df = pd.read_csv('ticket.csv')
print(df.to_string(index=False))

st.title("Customer support Analytics Dashboard")

uploaded_file = st.file_uploader(
    "Upload Ticket CSV",
    type=["csv"]
)
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    
total_tickets = len(df)


open_tickets = len(
    df[df["Status"] == "Open"]
)

closed_tickets = len(
    df[df["Status"] == "Closed"]
)

st.metric(
    "Total Tickets",
    total_tickets
)

category_count = (
    df["Category"]
    .value_counts()
)

st.bar_chart(category_count)

priority_count = (
    df["Priority"]
    .value_counts()
)

st.bar_chart(priority_count)


csv = df.to_csv(
    index=False
)

st.download_button(
    "Download Report",
    csv,
    "report.csv",
    "text/csv"
)