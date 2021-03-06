import os
from localPath import *
import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import json

mapboxAccessToken = "pk.eyJ1Ijoicm1ldGZjIiwiYSI6ImNqN2JjN3l3NjBxc3MycXAzNnh6M2oxbGoifQ.WFNVzFwNJ9ILp0Jxa03mCQ"

with open(os.path.join(jsonPath, 'bikeLocation.json'), 'r') as f:
    bikeLocation = json.load(f)

lat = bikeLocation['lat']
lng = bikeLocation['lng']
buildOrder = bikeLocation['buildOrder']
name = bikeLocation['name']
idList = bikeLocation['idList']
# set different color

S_STAR = ['3489', '3461', '3431', '3485', '3632', '3468', '3463', '3249', '3469', '3281', '3472', '3428', '3481']



color = []
for i in range(idList.__len__()):
    stationID = idList[i]
    if stationID in S_STAR:
        color.append('rgb(0, 0, 255)')
    else:
        color.append('rgb(%s, %s, %s)' % (255, 195-buildOrder[i], 195-buildOrder[i]))

bikeStations = [Scattermapbox(
        lon = lng,
        lat = lat,
        text = name,
        mode='markers',
        marker = dict(
            size = 6,
            color = color,  # ['rgb(%s, %s, %s)' % (255, 195-e, 195-e) for e in buildOrder],
            opacity=1,
        ))]

layout = Layout(
    title='Bike Station Location & The latest built stations with deeper color',
    autosize=True,
    hovermode='closest',
    showlegend=False,
    mapbox=dict(
        accesstoken=mapboxAccessToken,
        bearing=0,
        center=dict(
            lat=40.7381765,
            lon=-73.97738662
        ),
        pitch=0,
        zoom=11,
        style='light'
    ),
)

fig = dict(data=bikeStations, layout=layout)
plotly.offline.plot(fig, filename=os.path.join(htmlPath, 'BikeStationLocationWithBuildTime'))
