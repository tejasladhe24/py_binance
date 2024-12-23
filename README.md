# PyBinance: Binance API Python Client

## Overview
PyBinance provides a Python client for interacting with the Binance API. It includes utilities and market-related methods to simplify accessing Binance's endpoints. The client is modular, making it easy to add new functionality or customize it for specific use cases.

## Installation
Clone the repository and install the required dependencies:

```bash
curl https://raw.githubusercontent.com/tejasladhe24/py_binance/refs/heads/main/install.bash | bash
```

## Development
Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/tejasladhe24/py-binance.git

# Navigate to the directory
cd py_binance

# Install dependencies
pip install -r requirements.txt
```

## Features
- Ping Binance API
- Retrieve server time
- Fetch exchange information
- Get order book data
- Retrieve recent and historical trades
- Fetch aggregate trades
- Retrieve candlestick data (klines and UI klines)
- Get average price of a symbol

## Usage

### Initialize the Client
The client is resource-specific. Use `create_client` to create a client for either `market` or `utils` resources.

```python
from py_binance import create_client

# Create a market client
market_client = create_client(resource="market")

# Create a utils client
utils_client = create_client(resource="utils")
```

### Examples

#### Ping Binance API
```python
response = utils_client.ping()
print(response)  # Should return an empty response if the API is reachable
```

#### Retrieve Server Time
```python
server_time = utils_client.get_server_time()
print(f"Server Time: {server_time}")
```

#### Get Recent Trades
```python
recent_trades = market_client.get_recent_trades(symbol="BTCUSDT")
print(recent_trades)
```

#### Fetch Exchange Information
```python
exchange_info = market_client.get_exchange_info()
print(exchange_info)
```

#### Retrieve Order Book
```python
order_book = market_client.get_order_book(symbol="BTCUSDT", limit=100)
print(order_book)
```

#### Get Historical Trades
```python
historical_trades = market_client.get_historical_trades(symbol="BTCUSDT", fromId=123456)
print(historical_trades)
```

#### Fetch Candlestick Data (Klines)
```python
klines = market_client.get_klines(symbol="BTCUSDT", interval=Interval._1_DAY, limit=50)
print(klines)
```

#### Get Average Price
```python
average_price = market_client.get_average_price(symbol="BTCUSDT")
print(average_price)
```

## API Resources

### MarketClient
- `get_exchange_info(symbols=None, permissions=None, showPermissionSets=True, symbolStatus=None)`: Fetch information about symbols and exchange status.
- `get_order_book(symbol, limit=100)`: Retrieve order book data.
- `get_recent_trades(symbol, limit=100)`: Fetch the most recent trades for a symbol.
- `get_historical_trades(symbol, fromId, limit=100)`: Retrieve historical trades.
- `get_aggregate_trades(symbol, fromId, startTime, endTime, limit=100)`: Fetch aggregate trade data.
- `get_klines(symbol, interval, startTime=None, endTime=None, timeZone=None, limit=100)`: Retrieve candlestick data.
- `get_uiKlines(symbol, interval, startTime=None, endTime=None, timeZone=None, limit=100)`: Fetch UI candlestick data.
- `get_average_price(symbol)`: Get the average price of a symbol.

### UtilsClient
- `ping()`: Check Binance API connectivity.
- `get_server_time()`: Retrieve the current server time.

## Error Handling
If an error occurs while making a request, a `RuntimeError` will be raised with the error details.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

