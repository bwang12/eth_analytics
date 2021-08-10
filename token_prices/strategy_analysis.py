import pandas as pd 
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
tokens = cg.get_coins_list()
from datetime import datetime
date = []
# Price History of Yearn DAI deposit 
'''
total_yield = .28
daily_reduction = .00105
starting_value = 10000
days = 180 
values = []
while days > 0: 
    print(starting_value)
    starting_value = starting_value + (starting_value*(total_yield/365))
    total_yield = total_yield - daily_reduction
    values.append(starting_value)
    days = days - 1 

print(len(values))
'''
# Price History of ETH
eth_price = []
eth_price_history = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='usd', days='179')
eth_price_dict = eth_price_history['prices']
for x in eth_price_dict: 
    date.append(datetime.fromtimestamp(x[0]/1000))
    eth_price.append(15.5*x[1])
#eth_price = eth_price[::24]

# Price history of DPI 
dpi_price = []
dpi_price_history = cg.get_coin_market_chart_by_id(id='defipulse-index', vs_currency='usd', days='179')
dpi_price_dict = dpi_price_history['prices']
for x in dpi_price_dict: 
    date.append(datetime.fromtimestamp(x[0]/1000))
    dpi_price.append(x[1])
#dpi_price = dpi_price[::24]

print(len(dpi_price))

# Price History of Sushiswap strategy 
# 3x in pool value, 300% declining 1.2% daily 
total_yield = 3.4
daily_il_yield = .01777
daily_sushi_yield = .0133
daily_reduction = .00105
starting_value = 10000
starting_value2 = 10000
days = 180 
values = []
while days > 0: 
    print(starting_value)
    starting_value = starting_value + (starting_value*(daily_il_yield))
    #total_yield = total_yield - daily_reduction
    values.append(starting_value)
    days = days - 1 

print(len(values))




import statistics

import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(specs=[[{"secondary_y": True}]])

print(len(eth_price))
print(len(values))
fig.add_trace(go.Scatter(x=date, y=eth_price,
                    mode='lines',
                    name='ETH Returns',
                    line_color='blue'))
fig.add_trace(go.Scatter(x=date, y=values,
                    mode='lines',
                    name='yvDAI Returns'))
#name='yvDAI Returns',yaxis='y2'))
'''
fig.add_trace(go.Scatter(x=date, y=avalanche_price,
                    mode='lines',
                    name='AVAX Price',yaxis='y3'))
fig.add_trace(go.Scatter(x=date, y=binance_price,
                    mode='lines',
                    name='BNB Price',yaxis='y4'))
fig.add_trace(go.Scatter(x=date, y=terrausd_price,
                    mode='lines',
                    name='TerraUSD Price',
                    line_color='blue'))
'''
fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linewidth=2,
        zeroline=True,
        linecolor='#F4F4F4',
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=22,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=22,
            color='blue',
        ),
    ),
    yaxis2=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=22,
            color='blue',
        ),
    ),
    yaxis3=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=22,
            color='blue',
        ),
    ),
    yaxis4=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=True,
        gridcolor='#F4F4F4',
        tickfont=dict(
            family='Arial',
            size=22,
            color='blue',
        ),
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    autosize=True,

    plot_bgcolor='white'
)

fig.show()
