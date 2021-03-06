import plotly
import plotly.graph_objs as go
import os
import json
from localPath import *
import datetime
from dateutil.parser import parse

def to_unix_time(dt):
    epoch =  datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000

def timeSeries(x, y, title, fileName):
    data = [go.Scatter(
            x=x,
            y=y,
            name='scatter'),
            go.Scatter(
            x=x,
            y=y,
            name='curve',
            mode='markers',
            marker=dict(
                    size=5,
                    color='rgba(255, 0, 0)',
                ))]

    layout = go.Layout(
        title = title,
        xaxis = dict(range = [to_unix_time(x[0]),to_unix_time(x[-1])]))

    fig = go.Figure(data = data, layout = layout)
    plotly.offline.plot(fig, filename=os.path.join(htmlPath, fileName))


if __name__ == '__main__':
    with open(os.path.join(jsonPath, 'dailyStationNumber.json'), 'r') as f:
        dailyStationNumber = json.load(f)
    x = [parse(e) for e in dailyStationNumber['x']]
    y = dailyStationNumber['y']
    title = "Changes of Bike-Station Numbers over Time"
    fileName = 'dailyIncrease'
    timeSeries(x, y, title, fileName)