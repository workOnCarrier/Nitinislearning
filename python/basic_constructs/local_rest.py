import requests as requests

url_format = """http://{}/v1/symbols/details/{}"""
url = """https://api.sandbox.gemini.com/v1/symbols/details/BTCGUSDPERP"""

server_localhost = "localhost:9003"
server_sandbox = "api.sandbox.gemini.com"
symbol_params = "BTCGUSDPERP"

def get_response(server, request_format, parameters):
    url_test = request_format.format(server, parameters)
    print(f"attempting with url:{url_test}")
    response = requests.get(url_test)
    print(response.text)


if __name__ == "__main__":
    get_response(server_localhost, url_format, symbol_params)