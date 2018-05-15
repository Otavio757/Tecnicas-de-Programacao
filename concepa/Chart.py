import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout
import numpy

import csv

class obj:
    def __init__(self, date, hour, flow, total, dayOfWeek):
        self.date = date
        self.flow = flow
        self.total = total
        self.dayOfWeek = dayOfWeek

def PlotByDayOfWeek():
    # day of week Vs day hours - each day of week have 24hour

    import numpy
    matrix = numpy.zeros((24, 7))

    # results = []
    with open("datasets\\bydate.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE) # change contents to floats
        for row in reader: # each row is a list
            #results.insert(row[1], obj(row[0], row[1], row[2], row[3], row[4]))
            # print(str(row[1]+1)
            # print(str(row[4]+1))
            i = int(row[1])+1
            j = int(row[4])
            #print(matrix[i][j])
            #matrix[i][j] += row[3]
            type(matrix[i][j])
    
    # x = []
    # y = []
    # results = LoadCsv()
    # for i in range(0, 6):
    #     x.append(i)
    #     y.append(results[i].flow)

    plotly.offline.plot({"data":  [go.Bar(matrix)], "layout": Layout(title="Freeway Load") })

def PlotByDayHourTotal():
    # Soma o total de cada dia da semana por hora
    pass
def PlotByDayHourAverage():
    # Faz a media de fluxo de cada dia da semana por hora
    pass

def PlotHoursOfOneDay():
    x = []
    y = []
    results = LoadCsv()
    for i in range(0, 23):
        x.append(i)
        y.append(results[i].flow)

    trace1 = go.Scatter(x=x, y=y)
    trace2 = go.Bar(x=x, y=y)
    trace3 = go.Scatter(x=x, y=y, mode='markers', marker=dict(size=y))

    data = [trace1, trace2, trace3]

    plotly.offline.plot(data, filename='bar-line')

def LoadCsv():
    results = []
    with open("datasets\\bydate.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE) # change contents to floats
        for row in reader: # each row is a list
            results.append(obj(row[0], row[1], row[2], row[3], row[4]))
    return results


#x = [t.age for t in mylist if t.person_id == 10]


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

PlotByDayOfWeek()