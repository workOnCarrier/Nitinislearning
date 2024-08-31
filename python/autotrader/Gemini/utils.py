import json
import hashlib
import hmac
import base64
from config import GeminiConfig

def get_request_headers( config: GeminiConfig, payload: json):
    encoded_payload = json.dumps(payload).encode()
    b64 = base64.b64encode(encoded_payload)
    signature = hmac.new(config.gemini_api_secret, b64, hashlib.sha384).hexdigest()
    request_headers = {
        'Content-Type': "text/plain",
        'Content-Length': "0",
        'X-GEMINI-APIKEY': config.gemini_api_key,
        'X-GEMINI-PAYLOAD': b64,
        'X-GEMINI-SIGNATURE': signature,
        'Cache-Control': "no-cache"
        }
    return request_headers




def get_full_url(config: GeminiConfig, api_part):
    final_url =  config.base_url + api_part
    print(f"\t final url: {final_url}")
    return final_url