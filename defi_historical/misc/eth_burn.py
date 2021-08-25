import requests
import json 
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd 
import time
import plotly.express as px

eip_data = pd.read_csv('data/eip.csv')  
eip_data = eip_data.reindex(index=eip_data.index[::-1])
issuance = []
issuance.append(2)
blocks = 78996

#fig = px.bar(eip_data, x="number", y="Burned ETH per Block")

fig = go.Figure()


for x in range(0,blocks):
    issuance.append(2+issuance[x])
eip_data['issuance'] = issuance
print(eip_data['Burned ETH per Block'].mean())

eip_data['total_burn'] = -1 * eip_data['total_burn']
eip_data['cumulative_issuance'] = eip_data['issuance'] + eip_data['total_burn']

fig.add_trace(go.Scatter(x=eip_data['number'], y=eip_data['Burned ETH per Block'],
                    name='Burned ETH',
                    fill='tozeroy'))

'''
fig.add_trace(go.Scatter(x=eip_data['number'], y=eip_data['issuance'],
                    name='ETH Total Issuance',
                    fill='tonexty'))
fig.add_trace(go.Scatter(x=eip_data['number'], y=eip_data['total_burn'],
                    name='ETH Total Burn',
                    fill='tozeroy'))
fig.add_trace(go.Scatter(x=eip_data['number'], y=eip_data['cumulative_issuance'],
                    name='Issuance - Burn',marker_color='rgba(0, 0, 0, 0.5)'))
#print(eip_data)
'''
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