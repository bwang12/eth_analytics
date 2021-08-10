import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px

# Users over time 
ohm_apy_data = pd.read_csv('data/ohm_apy.csv')  
ohm_staked_data = pd.read_csv('data/ohm_staked.csv')  
ohm_treasury_data = pd.read_csv('data/ohm_treasury.csv')  
ohm_marketcap_data = pd.read_csv('data/ohm_marketcap.csv')  
ohm_holders_data = pd.read_csv('data/ohm_holders.csv')  
ohm_runway_data = pd.read_csv('data/ohm_runway.csv')  
ohm_rfv_data = pd.read_csv('data/ohm_rfv.csv')  
ohm_pol_data = pd.read_csv('data/ohm_pol.csv')  


#print(ohm_apy_data.columns)
fig = px.line(ohm_marketcap_data, x="date", y="pol")


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
            size=20,
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
            size=20,
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
