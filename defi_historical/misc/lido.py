import requests
import json 
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd 
import time
import plotly.express as px

lido_data = pd.read_csv('data/lido_deposits.csv')  

#fig = px.bar(eip_data, x="number", y="Burned ETH per Block")

fig = go.Figure()

fig.add_trace(go.Scatter(x=lido_data['time'], y=lido_data['staked'],
                    name='Lido Total Staked',
                    fill='tonexty'))

'''
fig = go.Figure()
fig.add_trace(go.Scatter(x=eip_data['number'], y=eip_data['total_burn'],
                    mode='lines',
                    name='EIP-1559 Burn',
                    line_color='blue'))
'''

'''
#eth_price = '$' + str(int(float((eth_price.json()[-1]['v']))))
fig.add_trace(go.Scatter(x=date, y=value,
                    mode='lines',
                    name='Total Value Locked',
                    line_color='blue'))
'''
'''
fig.add_trace(go.Scatter(x=gn_date, y=gn_value,
                    mode='lines',
                    name='Ethereum Price'),secondary_y=True)
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
            color='grey',
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
            color='grey',
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

'''
fig.add_layout_image(
    dict(
        source="https://images.plot.ly/language-icons/api-home/python-logo.png",
        xref="x",
        yref="y",
        x=0,
        y=3,
        sizex=2,
        sizey=2,
        sizing="stretch",
        opacity=0.5,
        layer="below")
)
'''
fig.show()