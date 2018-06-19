import uuid
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import csv 

class obj:
    def __init__(self, date, hour, flow, total, dayOfWeek):
        self.date = date
        self.flow = flow
        self.total = total
        self.dayOfWeek = dayOfWeek

def get_filename():
    return "UnisinosConcepa/Charts/" + uuid.uuid1().__str__() + ".png"

def format_date(full_date):
    splited = full_date.split("-")
    return "%s/%s" % (splited[-1:][0], splited[-2:-1][0])

def plot_weather(temperatures):

    filename = get_filename()
    x=list(map(lambda x: format_date(x[0]), temperatures))
    y=list(map(lambda x: x[1], temperatures))
    plt.bar(x, y)
    plt.ylabel('Temperature')
    plt.title('Forecast Weather')
    plt.savefig(filename)
    #plt.show()    
    return filename


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
 
            type(matrix[i][j])

    plotly.offline.plot({"data":  [go.Bar(matrix)], "layout": Layout(title="Freeway Load") })

def PlotByDayHourTotal():
    # Soma o total de cada dia da semana por hora
    pass

def PlotByDayHourAverage():
    # Faz a media de fluxo de cada dia da semana por hora
    rows = LoadCsv()
    daysOfWeek = [[], [], [], [], [], [], []]
    for row in rows:
        daysOfWeek[row.dayOfWeek].append(row.total)
    
    avg = {}
    for dayOfWeek in range(0, 7):
        avg[dayOfWeek] = sum(daysOfWeek[dayOfWeek], 0) / len(daysOfWeek[dayOfWeek])
        print("%d = %d" % (dayOfWeek, avg[dayOfWeek]))

def PlotHoursOfOneDay():
    x = []
    y = []
    results = LoadCsv()
    for i in range(0, 23):
        x.append(i)
        y.append(results[i].flow)

    # trace1 = go.Scatter(x=x, y=y)
    # trace2 = go.Bar(x=x, y=y)
    # trace3 = go.Scatter(x=x, y=y, mode='markers', marker=dict(size=y))

    # data = [trace1, trace2, trace3]

    # plotly.offline.plot(data, filename='bar-line')

def LoadCsv():
    results = []
    with open("D:\\PROJECTS\\Tecnicas-de-Programacao\\UnisinosDatasets\\bydate.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE) # change contents to floats
        for row in reader: # each row is a list
            results.append(obj(row[0], row[1], row[2], row[3], row[4]))
    return results

PlotByDayHourAverage()