## Arquivo para leitura do arquivo CSV gerado pela api CLIMATEMPO

import csv

#print(pd.read_csv('C:\\Users\\#000000\\Documents\\GitHub\\temph.csv'))
#results ="C:\\Users\\#000000\\Documents\\GitHub\\temph.csv"

teste = 'C:\\Users\\#000000\\Documents\\GitHub\\temph.csv' # define o caminho do arquivo
#hora=''

with open(teste, 'r') as arquivo:
    reader = csv.reader(arquivo, delimiter=';', quoting=csv.QUOTE_NONE)
    for linha in reader:
        data=linha[:-4]
        hora=linha[1:-3]
        precipitacao=linha[2:-2]
        velocidade_vento=linha[3:-1]
        temperatura=linha[4:]
        break


#print(data)
#print(hora)
#print(precipitacao)
#print(velocidade_vento)
#print(temperatura)


'''
    for linha in reader:
        hora=print(linha[:-4])
        break
'''


#EXAMPLE
'''
with open('ficheiro', 'rb') as ficheiro:
    reader = csv.reader(ficheiro, delimiter=':', quoting=csv.QUOTE_NONE)
    for linha in reader:
        print linha
'''


'''
results = [pd.read_csv('C:\\Users\\#000000\\Documents\\GitHub\\temph.csv')]

limitador = csv.reader(results, delimiter=';')

for i in limitador:
    print(results[0])

'''


'''
O divisor é ponto e vírgula ; e está organizado da seguinte forma:
[data];[hora];[precipitação];[velocidade do vento];[temperatura]

20/05/2018;00:00:00;0;12.2;14
20/05/2018;01:00:00;0;12.2;13
data       hora     p  vv   # TEMP

'''
