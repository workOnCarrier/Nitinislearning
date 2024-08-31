
import time

base_url = "https://api.sandbox.gemini.com"
mytrades_url = "/v1/mytrades"
symbols_url = "/v1/symbols"
# symbol_data_url = "/v1/symbols/details:{}"
symbol_data_url = "/v1/symbols/details:symbol=btcusd"
gemini_api_key = "master-wWEJ48E5MQ5DhFmvNEI2"
gemini_api_secret = "44NcJKHvD2o5MCtiY97vnpgWunru".encode()


def get_nounce():
    payload_nonce = time.time()
    return payload_nonce

class GeminiConfig:
    def __init__(self) -> None:
        self.base_url = base_url
        self.mytrades_url = mytrades_url
        self.gemini_api_key = gemini_api_key
        self.gemini_api_secret = gemini_api_secret
        self.symbols_url = symbols_url
        self.symbol_data_url = symbol_data_url
        pass
    def get_trades_payload(self):
        payload_nonce = get_nounce()
        payload =  {"request": self.mytrades_url, "account": "primary", "nonce": payload_nonce}
        return payload
    def get_symbol_data_url(self, symbol):
        # symbol_data_url = self.symbol_data_url.format(symbol)
        symbol_data_url = self.symbol_data_url
        print(f"\t symbol url:{symbol_data_url}")
        return symbol_data_url


