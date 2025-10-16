import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import joblib
import matplotlib.pyplot as plt


class ARIMAForecaster:
    def __init__(self, order=(1, 1, 1)):
        """
        order: ARIMA(p,d,q) tuple
        """
        self.order = order
        self.model_fit = None

    def train(self, series: pd.Series):
        """
        series: pd.Series with datetime index (option prices)
        """
        model = ARIMA(series, order=self.order)
        self.model_fit = model.fit()
        return self

    def forecast(self, steps=12):
        if self.model_fit is None:
            raise ValueError("Model not trained yet.")
        forecast = self.model_fit.forecast(steps=steps)
        return forecast

    def plot_forecast(self, historical_series: pd.Series, steps=12):
        forecast = self.forecast(steps)
        future_index = pd.date_range(
            start=historical_series.index[-1] + pd.offsets.MonthBegin(1),
            periods=steps, freq='M'
        )
        plt.figure(figsize=(10, 5))
        plt.plot(historical_series.index, historical_series, label="Historical Option Prices")
        plt.plot(future_index, forecast, linestyle='--', label="Forecasted Option Prices")
        plt.title("Option Price Forecast Next 12 Months (ARIMA)")
        plt.xlabel("Month")
        plt.ylabel("Option Price")
        plt.legend()
        plt.show()

    def save_model(self, path="models/arima_options.pkl"):
        joblib.dump({"order": self.order, "model_fit": self.model_fit}, path)

    def load_model(self, path="models/arima_options.pkl"):
        data = joblib.load(path)
        self.order = data["order"]
        self.model_fit = data["model_fit"]
