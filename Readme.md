# Binance Futures Demo Trading Bot

## Setup

Install dependencies:

pip install -r requirements.txt

Set API keys (PowerShell):

$env:BINANCE_API_KEY="your_api_key"
$env:BINANCE_API_SECRET="your_secret_key"

## Run Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

## Run Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 72000