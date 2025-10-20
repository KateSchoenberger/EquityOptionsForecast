
**Equity Options Forecast** is an ARIMA Python project that predicts the future prices of equity options based on historical price data (univariate). Using the ARIMA (AutoRegressive Integrated Moving Average) model, this tool can forecast the next 12 months of option prices using the previous 12–24 months of historical data.

This project is designed as a **modular, class-based system**, making it easy to extend for multiple options, different strike prices, or additional time series. It is ideal for traders, analysts, or developers interested in prototyping option price forecasts and understanding historical trends.

---

## Features

- Load historical option price data (mock or CSV)
- Train ARIMA models for time series forecasting
- Forecast next 12 months of option prices
- Visualize historical and forecasted option prices
- Save and load trained models using `.pkl` files
- Modular class design for easy integration with other trading tools

# Installation 

To set up the project on your local machine:

Clone the repository:

git clone https://github.com/KateSchoenberger/EquityOptionsForecast.git
cd EquityOptionsForecast


Install the required dependencies:

pip install -r requirements.txt


Prepare your historical option price data in a CSV format with appropriate columns.

# Usage

Load your historical option price data into the system.

Utilize the provided classes and methods to fit the ARIMA model to your data.

Generate forecasts for the next 12 months.

Analyze the results to inform your trading or analysis strategies.


Ensure all tests pass before deploying to production.

# Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.

# License

This project is licensed under the MIT License - see the LICENSE
 file for details.

ChatGPT can ma

