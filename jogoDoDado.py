#crie um programa onde 4 jogadores jogam um dado e tenham resultados aleatorios

#guarde esses resultados em um dicionario

#no final coloque esse dicionario em ordem, sabendo que o vencedor é quem tirou o maior numero.

from random import randint #importei a biblioteca para gerar numeros aleatorios de 1 a 6 (o dado)
from time import sleep #importei a biblioteca time sleep para ter um intervalo entre os comandos
results = [] #criei uma lista que vai receber os valores do dado e sortear eles em ordem DECRESCENTE

dado = {'Jogador 1':randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}
#aqui eu já declaro os valores no dicionário e o que cada um vai receber.

print('<<<< JOGO DO DADO >>>>') #titulo do game

results.append(dado['Jogador 1']) 
results.append(dado['Jogador 2'])
results.append(dado['Jogador 3'])
results.append(dado['Jogador 4'])
#eu dou append dos resultados na lista results para colocar em ordem decrescente

results.sort(reverse=True) #sortando os numeros que eu dei append 
lista = sorted(dado, key = dado.get, reverse=True)
#aqui uma novidade. Existe uma sintaxe correta para eu dar SORT em um dicionario.
#a sintaxe é sorted(dicionario, key = dicionario.get)
#o ket = dicionario.get vai pegar os valores ao inves das keys para servir de parametros para a ordenação
#e o reverse = True serviu para fazer isso ser feito de forma decrescente.

for i , v in dado.items(): #para um indice e um valor varrendo os itens do dicionario do dado...
    print(f'Valor {i}: {v}') #eu imprimo formatado o {i} que corresponde ao 'Jogador x' e o {v} que corresponde ao valor do dado
    sleep(0.5) #aqui eu uso o sleep para tornar mais legal o programa

print('<<<< VENCEDORES EM ORDEM >>>>\n')

for v in range(0,4): #para um validador em um range de 0 a 3...
        print(f'O {v+1}º colocado foi o {lista[v]} com {results[v]}')
        #eu imprimo que o (validador + 1) colocado foi o equivalente ao enésimo colocado da lista sortada
        #que eu fiz anteriormente com o 'key = dado.get'. E imprimo cada valor correspondente ao que o meu validador varreu
        #e também o seu respectivo valor de acordo com o que eu fiz na sorted results.
        sleep(0.5) #dou um timing de 0.5 segundos.


