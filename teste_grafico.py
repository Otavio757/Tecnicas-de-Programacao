##Usando Pylab para gerar os gráficos

# -*- coding:utf-8 -*-

import pylab

# função usada como exemplo
def cubo (x):
    return x * x

# pylab.arange(inicio, fim, passo) - define um 'arranjo' com os valores de entrada.
entrada = pylab.arange(0, 20, 1)

# saida - recebe um 'arranjo' com os resultados da
# função sobre cada ítem de 'entrada'.
saida = cubo(entrada)

# pylab.plot(e, s) - 'plota' os dados de entrada e saída
# no grafico.
pylab.plot(entrada, saida)

# pylab.xlabel(s) - define o label do eixo x.
pylab.xlabel('Entrada')

# pylab.ylabel(s) - define o label do eixo y.
pylab.ylabel('Cubo')

# pylab.title(s) - define o titulo do grafico.
pylab.title('Funcao do Cubo')

# pylab.grid(boleano) - define se exibirá ou não as 'grids'
# no gráfico.
pylab.grid(True)

# pylab.show() - exibe o gráfico
pylab.show() 


