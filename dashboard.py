import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.title("AI Trading Dashboard")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

data = yf.download(ticker, period="6mo")

# Moving averages
data["SMA20"] = data["Close"].rolling(20).mean()
data["SMA50"] = data["Close"].rolling(50).mean()

# Buy/Sell signals
data["Signal"] = 0
data.loc[data["SMA20"] > data["SMA50"], "Signal"] = 1
data.loc[data["SMA20"] < data["SMA50"], "Signal"] = -1

# Candlestick chart
fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=data.index,
    open=data["Open"],
    high=data["High"],
    low=data["Low"],
    close=data["Close"],
    name="Candles"
))

# Moving averages
fig.add_trace(go.Scatter(x=data.index, y=data["SMA20"], name="SMA20"))
fig.add_trace(go.Scatter(x=data.index, y=data["SMA50"], name="SMA50"))

st.subheader("Candlestick Chart")
st.plotly_chart(fig)

# Show signals
latest_signal = data["Signal"].iloc[-1]

if latest_signal == 1:
    st.success("BUY Signal 📈")
elif latest_signal == -1:
    st.error("SELL Signal 📉")
else:
    st.write("No clear signal")

st.dataframe(data.tail())