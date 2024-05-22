# Purpose
# 1. Using the account -- get the list of trades in the account at gemini
# 2. Then use a different account on different exchange -- possibly using CCXT


# gemini rest api sandbox -- https://api.sandbox.gemini.com


import requests
import json
import base64
import hmac
import hashlib
import time

url = "https://api.sandbox.gemini.com/v1/mytrades"
# url = "https://api.sandbox.gemini.com/v1/account"
gemini_api_key = "master-wWEJ48E5MQ5DhFmvNEI2"
gemini_api_secret = "44NcJKHvD2o5MCtiY97vnpgWunru".encode()

payload_nonce = time.time()

payload =  {"request": "/v1/mytrades", "account": "primary", "nonce": payload_nonce}
# [
# {'price': '70000.10', 'amount': '0.00728365', 'timestamp': 1716288990, 'timestampms': 1716288990003, 'type': 'Buy', 'aggressor': False, 'fee_currency': 'GUSD', 'fee_amount': '1.01971', 'tid': 2840140809898890, 'order_id': '73770411957537444', 'exchange': 'gemini', 'is_auction_fill': False, 'is_clearing_fill': False, 'symbol': 'BTCGUSD', 'client_order_id': ''},
# {'price': '70000.10', 'amount': '0.007', 'timestamp': 1716288592, 'timestampms': 1716288592816, 'type': 'Buy', 'aggressor': False, 'fee_currency': 'GUSD', 'fee_amount': '0.98', 'tid': 2840140809897871, 'order_id': '73770411957537444', 'exchange': 'gemini', 'is_auction_fill': False, 'is_clearing_fill': False, 'symbol': 'BTCGUSD', 'client_order_id': ''}
# ]

# payload =  {"request": "/v1/account", "account": "primary", "nonce": payload_nonce}
# {'account': {'accountName': 'Primary', 'shortName': 'primary', 'type': 'exchange', 'created': '1688110734350', 'verificationToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJHZW1pbmkiLCJleHAiOjE3MTYzOTcwODQsImlhdCI6MTcxNjM5NjQ4NDgxNiwiYWNjb3VudEhhc2hJZCI6IjNNUUQ5RzIxIiwiY3JlYXRlZEF0IjoxNjg4MTEwNzM0MzUwfQ.4X--DwKG2JHqmDm3oRLjlYuTitBrvhkjjyucEG-yxC0'}, 'users': [{'name': 'Nitin Sharma', 'lastSignIn': '2024-05-22T12:58:58.582Z', 'status': 'Active', 'countryCode': 'SG', 'isVerified': True}], 'memo_reference_code': 'GEMRZJZXWQ'}

encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

request_headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
    }

response = requests.post(url, headers=request_headers)

my_trades = response.json()
print(my_trades)