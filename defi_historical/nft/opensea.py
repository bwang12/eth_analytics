import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px
# Users over time 


opensea_usage = pd.read_csv('data/opensea_monthly_volume.csv')  
opensea_traders = pd.read_csv('data/openseatraders.csv')  

'''
fig = go.Figure(
    data=[
        go.Bar(
            x=opensea_traders["date"],
            y=opensea_traders["users"],
        ),
    ],
)
'''
fig = go.Figure(
    data=[
        go.Bar(
            x=opensea_usage["month"],
            y=opensea_usage["usd"],
        ),
    ],
)

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
