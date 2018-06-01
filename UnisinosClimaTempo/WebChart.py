import uuid
import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout
import numpy

def get_filename():
    return "UnisinosClimaTempo/Charts/" + uuid.uuid1().__str__()

def plot_weather(temperatures):

    filename = get_filename()

    plotly.offline.plot({
        'data': [go.Bar(
                x=list(map(lambda x: x[0], temperatures)),
                y=list(map(lambda x: x[1], temperatures))
        )],
        'layout': {'title': 'Forecast Temperatures', 'font': dict(size=16)}
        }, image='png', image_filename=filename, auto_open=True, filename=filename + ".html")

    return filename + ".png"
