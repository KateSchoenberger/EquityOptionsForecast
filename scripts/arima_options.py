import pandas as pd
import numpy as np
from src.arima_model import ARIMAForecaster

# -----------------------------
# Mock Option Price Data (Monthly)
# -----------------------------
np.random.seed(42)
months = pd.date_range(start="2023-01-01", periods=24, freq='M')
# Simulate option prices (rough approximation)
option_prices = np.cumsum(np.random.normal(loc=1.0, scale=5.0, size=len(months))) + 100
option_series = pd.Series(option_prices, index=months)

# -----------------------------
# Train ARIMA model
# -----------------------------
arima_forecaster = ARIMAForecaster(order=(1,1,1))
arima_forecaster.train(option_series)

# -----------------------------
# Forecast next 12 months
# -----------------------------
forecasted_prices = arima_forecaster.forecast(steps=12)
print("Forecasted Option Prices for Next 12 Months:")
print(forecasted_prices)

# -----------------------------
# Plot results
# -----------------------------
arima_forecaster.plot_forecast(option_series, steps=12)

# -----------------------------
# Save the model
# -----------------------------
arima_forecaster.save_model("models/arima_options.pkl")
