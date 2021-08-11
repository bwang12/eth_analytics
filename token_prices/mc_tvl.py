from pycoingecko import CoinGeckoAPI
from datetime import datetime
cg = CoinGeckoAPI()
tokens = cg.get_coins_list()
#print(tokens)
date = []
eth_price = []
sushi_price = []
dpi_price = [] 
solana_price = []
avalanche_price = []
binance_price = []
terrausd_price = []
sushi_price = []

# retreive JSONs
eth_price_history = cg.get_coin_market_chart_by_id(id='olympus', include_market_cap='true', vs_currency='usd', days='60')
print(eth_price_history)
#dpi_price_history = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='usd', days='60')
