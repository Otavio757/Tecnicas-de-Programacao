##Usando Pylab para gerar os gráficos
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

# função usada como exemplo
'''
def cubo (x):
    return x * x
'''
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

# saida - recebe um 'arranjo' com os resultados da
# função sobre cada ítem de 'entrada'.
#saida = cubo(entrada)

azul = "blue"
verde = "green"
preto = "black"
## ACIMA
# cores do grafico


def plota_barra_1():
    plt.bar(xBar, yBar, color=azul)


# pylab.plot(e, s) - 'plota' os dados de entrada e saída
# no grafico.
#pylab.plot(entrada, saida)

# pylab.xlabel(s) - define o label do eixo x.
#pylab.xlabel('Entrada')

# pylab.ylabel(s) - define o label do eixo y.
#pylab.ylabel('Estrada') #antes era cubo

# pylab.title(s) - define o titulo do grafico.
#pylab.title('Condição da Estrada')
#titulo

# pylab.grid(boleano) - define se exibirá ou não as 'grids'
# no gráfico.
#pylab.grid(True)

# pylab.show() - exibe o gráfico
#pylab.show()
