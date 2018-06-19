##Usando matplotlib para gerar os gráficos
# -*- coding:utf-8 -*-
## São usados 3 ferramentas

## pandas
## numpy
## pyplot importado do matplotlib
import pandas as pd
import numpy as np
from random import randint as rd
from leitura_csv_python import data
from leitura_csv_python import hora
from leitura_csv_python import precipitacao
from leitura_csv_python import velocidade_vento
from leitura_csv_python import temperatura
#from dadosGraph import dados
import matplotlib.pyplot as plt

'''
data_var = data
hora_var = hora
precipt = precipitacao
vel_vento = velocidade_vento
temp = temperatura

'''
hora_var = hora

temp = temperatura


yBar = temp ### EIXO Y COM VALORES FIXOS
xBar = hora_var
## FIXO X COM VALORES NOMES FIXOS
'''
def teste():
    for i in yBar:
        a = print(yBar.split(2))
'''

#b = teste()

#y = [b]
azul =  "blue"
verde = "green"
preto = "black"
## ACIMA
# cores para serem usadas no grafico

plt.title("Título")
plt.bar(xBar, yBar, color=verde) ## plota as barras e define as cores

plt.show() # mostra o gráfico na tela
