import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px
# Users over time 
daily_dex_data = pd.read_csv('data/daily_dex.csv')  
#print(daily_dex_data)
monthly_dex_data = pd.read_csv('data/monthly_dex.csv')  
synthetix_dex_data = pd.read_csv('data/synthetix_volume.csv')  
perp_dex_data = pd.read_csv('data/perp_traders.csv')  
ohm_dex_data = pd.read_csv('data/ohm_fees.csv')  

#cust_sell = mainDf[mainDf.Type == 'S']
#cust_buy = mainDf[mainDf.Type == 'P']


fig = go.Figure(
    data=[
        go.Bar(
            x=monthly_dex_data["date_trunc"],
            y=monthly_dex_data["usd_volume"],
        ),
    ],
)


#daily_volume = daily_dex_data.groupby(["date_trunc"]).usd_volume.sum().reset_index()
#print(daily_volume)
#fig = px.bar(perp_dex_data, x="_date", y="_traders")

fig.update_layout(
    barmode='stack',
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
