##Usando matplotlib para gerar os gráficos
# -*- coding:utf-8 -*-
## São usados 3 ferramentas

## pandas
## numpy
## pyplot importado do matplotlib


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Abaixo, alguma variáveis a serem usadas
## os vetores x e y

# pylab.arange(inicio, fim, passo) - define um 'arranjo' com os valores de entrada.
x = [0, 20, 1]
y = [10,20,30]
y2 = [15,10,40]
y3 = [20,10,35]
### ACIMA

## arranjo de resultados
yBar = [3,10,7,6,58,56,12,3]
z = [i * 1.5 for i in yBar]
xBar = range(len(yBar))

azul = "blue"
verde = "green"
preto = "black"
## ACIMA
# cores do grafico

plt.bar(xBar, yBar, color=azul)

plt.show()
# mostra o gráfico na tela
