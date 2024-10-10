import statsmodels.api as sm
from statsmodels.tsa.stattools import coint
import yfinance as yf

# Download historical price data
assets = ['TSLA', 'MSFT']
data = yf.download(assets, start="2020-01-01", end="2024-01-01")['Adj Close']

# Run cointegration test on asset pairs
score, p_value, _ = coint(data['TSLA'], data['MSFT'])

if p_value < 0.05:
    print("AAPL and MSFT are cointegrated")
else:
    print("They aint")