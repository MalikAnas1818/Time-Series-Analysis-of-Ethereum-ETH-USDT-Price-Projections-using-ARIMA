import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
from statsmodels.tsa.arima.model import ARIMAResults
# Title
st.title("📊 Ethereum Price Forecasting (ETH/USDT)")
st.markdown("Predict future prices using a pre-trained ARIMA model.")
df = pd.read_csv("eth_price.csv")
df.reset_index().drop('index', axis=1)
@st.cache_data
def load_data():
    df = pd.read_csv("eth_price.csv")
    df = df.reset_index().drop('index', axis=1)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index("Date", inplace=True)
    return df
@st.cache_resource
def load_model():
    model = ARIMAResults.load("arima_model.pkl")
    return model
# Load
df = load_data()
model = load_model()
# Date filter
st.subheader("📅 Select Date Range to View Historical Data")
start_date = st.date_input("Start Date", df.index.min().date())
end_date = st.date_input("End Date", df.index.max().date())
# Filtered Data
filtered_df = df.loc[start_date:end_date]
# Show historical data
st.subheader("📈 Historical ETH Price")
st.line_chart(filtered_df["C"])
# User input for prediction
n_days = st.number_input("🔮 Number of Days to Forecast", min_value=1, max_value=100, value=10)
# Predict
if st.button("🚀 Predict Future Prices"):
    forecast = model.get_forecast(steps=n_days)
    pred = forecast.predicted_mean

    last_date = df.index[-1]
    future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=n_days)

    pred_df = pd.DataFrame({'Predicted Price': pred.values}, index=future_dates)
        # Combined chart
    combined = pd.concat([df["C"].tail(30), pred_df["Predicted Price"]])
    st.subheader("📊 Combined Chart: Last 30 Days + Forecast")
    st.line_chart(combined)
        # Show forecast table (optional)
    st.subheader("🧾 Forecast Data")
    st.dataframe(pred_df)
