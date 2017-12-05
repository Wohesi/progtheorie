import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd

#df = pd.read_csv("US states/us_states.csv")
#print (df[:10])



trace1 = Choropleth(
    z=['1', '1', '1', '1', '1', '1', '1'],
    autocolorscale=False,
    colorscale=[[0, 'rgb(255, 0, 0)'], [1, 'rgb(255, 0, 0)']],
    hoverinfo='text',
    locationmode='USA-states',
    locations=['AR', 'GA', 'KY', 'MO', 'UT', 'TX', 'WY'],
    showscale=False,
    text=['Arkansas', 'Georgia', 'Kentucky', 'Missouri', 'Utah', 'Texas', 'Wyoming'],
    zauto=False,
    zmax=1,
    zmin=0,
)



data = Data([trace1])
layout = Layout(
    autosize=False,
    geo=dict(
        countrycolor='rgb(102, 102, 102)',
        countrywidth=0.1,
        lakecolor='rgb(255, 255, 255)',
        landcolor='rgba(237, 247, 138, 0.28)',
        lonaxis=dict(
            gridwidth=1.6,
            #range=[-180, -50],
            showgrid=False
        ),
        projection=dict(
            type='albers usa'
        ),
        scope='usa',
        showland=True,
        showrivers=False,
        showsubunits=True,
        subunitcolor='rgb(102, 102, 102)',
        subunitwidth=0.5
    )
)
fig = Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='countries')
