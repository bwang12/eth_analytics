import pandas as pd 
#import plotly.graph_objects as go
import plotly.express as px
# Users over time 
cryptopunks_prices = pd.read_csv('data/cryptopunks.csv')  
boredapes_prices = pd.read_csv('data/boredapes.csv')  


'''
fig = go.Figure(
    data=[
        go.Bar(
            x=monthly_dex_data["date_trunc"],
            y=monthly_dex_data["usd_volume"],
            color='project',
        ),
    ],
)
'''
fig = px.line(boredapes_prices, x="date", y="eth")

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
