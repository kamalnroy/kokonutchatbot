import streamlit as st

st.title("Simple Stock Price Viewer")

stock = st.text_input("Enter Stock Symbol", "AAPL")
st.write(f"You selected: {stock}")