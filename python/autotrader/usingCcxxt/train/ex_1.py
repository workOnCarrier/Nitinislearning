import ccxt




def get_all_exchanges():
    print (ccxt.exchanges)
#['ace', 'alpaca', 'ascendex', 'bequant', 'bigone', 'binance', 'binancecoinm', 'binanceus', 'binanceusdm', 'bingx', 'bit2c', 'bitbank', 'bitbay', 'bitbns', 'bitcoincom', 'bitfinex', 'bitfinex2', 'bitflyer', 'bitget', 'bithumb', 'bitmart', 'bitmex', 'bitopro', 'bitpanda', 'bitrue', 'bitso', 'bitstamp', 'bitteam', 'bitvavo', 'bl3p', 'blockchaincom', 'blofin', 'btcalpha', 'btcbox', 'btcmarkets', 'btcturk', 'bybit', 'cex', 'coinbase', 'coinbaseadvanced', 'coinbaseexchange', 'coinbaseinternational', 'coincheck', 'coinex', 'coinlist', 'coinmate', 'coinmetro', 'coinone', 'coinsph', 'coinspot', 'cryptocom', 'currencycom', 'delta', 'deribit', 'digifinex', 'exmo', 'fmfwio', 'gate', 'gateio', 'gemini', 'hitbtc', 'hitbtc3', 'hollaex', 'htx', 'huobi', 'huobijp', 'hyperliquid', 'idex', 'independentreserve', 'indodax', 'kraken', 'krakenfutures', 'kucoin', 'kucoinfutures', 'kuna', 'latoken', 'lbank', 'luno', 'lykke', 'mercado', 'mexc', 'ndax', 'novadax', 'oceanex', 'okcoin', 'okx', 'onetrading', 'p2b', 'paymium', 'phemex', 'poloniex', 'poloniexfutures', 'probit', 'timex', 'tokocrypto', 'tradeogre', 'upbit', 'wavesexchange', 'wazirx', 'whitebit', 'woo', 'woofipro', 'yobit', 'zaif', 'zonda'] 


def check_connect_gemini():
    exchaange = ccxt.gemini()
    


if __name__ == "__main__":
