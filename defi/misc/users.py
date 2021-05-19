import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px

# Users over time 
users_data = pd.read_csv('data/total_users.csv')  
uniswap_users_data = pd.read_csv('data/uniswap_users.csv')  
compound_users_data = pd.read_csv('data/compound_users.csv')  
yearn_users_data = pd.read_csv('data/yearn_users.csv')  
uniswap_retention = pd.read_csv('data/uniswap_retention.csv')  
sushiswap_retention = pd.read_csv('data/sushiswap_retention.csv')
print(uniswap_retention)
# users
'''
fig = go.Figure()
fig.add_trace(go.Scatter(x=yearn_users_data['date'], y=yearn_users_data['total_users'],
                    mode='lines',
                    name='lines',
                    line_color='blue'))
'''
#retention 
fig = px.bar(sushiswap_retention, sushiswap_retention["month"], y=sushiswap_retention["count"], color="status")



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
            size=14,
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
            size=14,
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
