##Usando matplotlib para gerar os gráficos
# -*- coding:utf-8 -*-
## São usados 3 ferramentas

## pandas
## numpy
## pyplot importado do matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
yBar e xBar ainda em testes
'''
yBar = [23,23,23] ### EIXO Y COM VALORES FIXOS
xBar = ['um', 'dois', 'tres']
### 'quatro', 'cinco', 'seis', 'sete', 'oito'
## FIXO X COM VALORES NOMES FIXOS

azul = "blue"
verde = "green"
preto = "black"
## ACIMA
# cores para serem usadas no grafico

plt.bar(xBar, yBar, color=verde) ## plota as barras e define as cores

plt.show() # mostra o gráfico na tela
