import requests
import json
import base64
import hmac
import hashlib
import datetime, time

# base_url = "https://api.sandbox.gemini.com"
base_url = "https://web-api-server-qa100-001.aws-qa.host.gem.link"
endpoint = "/v1/order/new"
url = base_url + endpoint

gemini_api_key = "account-ll3oUwD43N1hMr1nH3Qw"
gemini_api_secret = "3fwuxEJx6A2yLhirh3aMBdiWbKJa".encode()

t = datetime.datetime.now()
payload_nonce = time.time()

payload = {
   "request": "/v1/order/new",
   "nonce": payload_nonce,
   "symbol": "btcusd",
   "amount": "0.0001",
   "price": "60",
   "stop_price": "49",
   "side": "buy",
   # "type": "exchange limit"
   "type": "exchange stop limit"
}

encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

request_headers = { 'Content-Type': "text/plain",
                    'Content-Length': "0",
                    'X-GEMINI-APIKEY': gemini_api_key,
                    'X-GEMINI-PAYLOAD': b64,
                    'X-GEMINI-SIGNATURE': signature,
                    'Cache-Control': "no-cache" }

response = requests.post(url,
                        data=None,
                        headers=request_headers)

new_order = response.json()
print(response.status_code)
print(new_order)