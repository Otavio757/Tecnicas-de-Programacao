import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

import csv

class obj:
    def __init__(self, date, hour, flow, total, dayOfWeek):
        self.date = date
        self.flow = flow
        self.total = total
        self.dayOfWeek = dayOfWeek

results = []
with open("datasets\\bydate.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE) # change contents to floats
    for row in reader: # each row is a list
        results.append(obj(row[0], row[1], row[2], row[3], row[4]))


#x = [t.age for t in mylist if t.person_id == 10]
x = []
y = []
for i in range(0, 23):
    x.append(i)
    y.append(results[i].flow)

# plotly.offline.plot({
#     "data": [Scatter(x=x, y=y)],
#     "layout": Layout(title="Freeway Load")
# })


##BAR CHART
# plotly.offline.plot({
#     "data":  [go.Bar(
#             x=x,
#             y=y
#     )],
#     "layout": Layout(title="Freeway Load")
# })


###BUBBLE
#plotly.offline.plot([go.Scatter(x=x, y=y, mode='markers', marker=dict(size=y))], filename='bubblechart-size')

trace1 = go.Scatter(
    x=x,
    y=y
)
trace2 = go.Bar(
    x=x,
    y=y
)

trace3 = go.Scatter(x=x, y=y, mode='markers', marker=dict(size=y))
data = [trace1, trace2, trace3]
plotly.offline.plot(data, filename='bar-line')