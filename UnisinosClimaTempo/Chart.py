import uuid
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

def get_filename():
    return "UnisinosClimaTempo/Charts/" + uuid.uuid1().__str__() + ".png"

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

