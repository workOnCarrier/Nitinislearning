import requests
import json
from utils import *
from  config import GeminiConfig


def get_symbols():
    config = GeminiConfig()
    response = requests.get(get_full_url(config, config.symbols_url))
    symbols = response.json()
    print(symbols)

def get_symbol_data(symbol):
    config = GeminiConfig()
    response = requests.get(get_full_url(config, config.get_symbol_data_url(symbol)))
    symbols = response.json()
    print(symbols)

if __name__ == '__main__':
    get_symbols()
    symbol = 'BTCUSD'
    get_symbol_data(symbol)
