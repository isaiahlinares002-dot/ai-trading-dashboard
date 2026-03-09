import streamlit as st
import yfinance as yf

st.title("AI Trading Dashboard")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

data = yf.download(ticker, period="6mo")

st.write("Stock Data")
st.write(data)

st.line_chart(data["Close"])