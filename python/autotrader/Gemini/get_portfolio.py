# Purpose
# 1. Using the account -- get the list of trades in the account at gemini
# 2. Then use a different account on different exchange -- possibly using CCXT


# gemini rest api sandbox -- https://api.sandbox.gemini.com


import requests
import json
from utils import *
from  config import GeminiConfig


def get_my_trades():
    config = GeminiConfig()
    payload = config.get_trades_payload()
    request_headers = get_request_headers(config, payload)
    response = requests.post(get_full_url(config, config.mytrades_url), headers=request_headers)
    my_trades = response.json()
    print(my_trades)

if __name__ == '__main__':
    get_my_trades()