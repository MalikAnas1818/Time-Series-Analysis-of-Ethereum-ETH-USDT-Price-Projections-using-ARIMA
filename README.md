# 🧠 Time Series Analysis of Ethereum (ETH/USDT) Price Projections using ARIMA
    This project presents a time series forecasting model for Ethereum (ETH/USDT) using the ARIMA (AutoRegressive Integrated Moving Average) method. It is designed to analyze historical cryptocurrency price data and make future projections, helping understand trends and possible market movements.

## 📈 Project Overview
#### Objective: Forecast future Ethereum prices based on past data using ARIMA, a statistical time series modeling technique.

#### Dataset: Historical daily ETH/USDT data from 2017 to 2024.

#### Tools & Libraries: Python, Pandas, Matplotlib, Statsmodels, ARIMA

#### 🔍 Key Features
##### Exploratory Data Analysis (EDA) and visualization of ETH/USDT trends.

##### Stationarity testing using ADF (Augmented Dickey-Fuller) test.

##### Time series decomposition into trend, seasonality, and residuals.

##### Auto ARIMA for optimal parameter selection (p, d, q).

##### Model training, evaluation, and forecasting.

##### Forecast visualization with confidence intervals.

## 📊 Visual Outputs
### The notebook includes graphs such as:

Line plots of ETH prices

ACF and PACF plots

Time series decomposition plots

Forecast results with lower/upper confidence bounds

## 🛠️ How to Use
### Clone the repository:

bash
Copy
Edit
git clone https://github.com/MalikAnas1818/Time-Series-Analysis-of-Ethereum-ETH-USDT-Price-Projections-using-ARIMA.git
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Jupyter notebook:

bash
Copy
Edit
jupyter notebook ETH_ARIMA_Forecast.ipynb
📁 File Structure
ETH_ARIMA_Forecast.ipynb: Main notebook for the analysis and forecasting.

data/: Contains the Ethereum price dataset (if available).

plots/: Forecast and analysis visualizations.

## 📌 Insights
The ARIMA model captures trends well but has limitations in high-volatility crypto markets.

Seasonal effects and price spikes are visualized and accounted for using differencing and residual analysis.

This project can serve as a foundational model for more advanced machine learning and deep learning models in crypto price prediction.

## 📫 Contact
Created by Malik Anas — for inquiries or collaboration, feel free to reach out via LinkedIn or GitHub Issues.
https://www.linkedin.com/in/muhammad-anis-09619a353/

