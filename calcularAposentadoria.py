import datetime #importando o datetime para mexer com variaveis de datas

anocont = 0
anohoje = datetime.date.today().year #o ano de hoje recebe a função para contabilizar o ano atual
infos = {}

infos['nome'] = str(input('Nome: ')) 
nasc = int(input('Ano de nascimento: '))
ctps = int(input('CTPS (digite [0] caso não tenha): '))
#colocando as primeiras informações na lista

if ctps != 0: #se a CTPS for diferente de 0:
    infos['carteira'] = ctps
    anocont = int(input('Ano de contratação: '))
    sal = float(input('Valor do último salário: '))
    infos['contratacao'] = anocont
    infos['salario'] = sal
    #colocando os dados no dicionario

infos['idade'] = anohoje - nasc
#calculando minha data de nascimento para colocar no dicionario

contribuicao = anohoje - anocont
#o periodo de contribuição equivale ao ano de hoje MENOS o ano de contratação.

difaposent = 35 - contribuicao
#a diferença da aposentadoria equivale aos 35 anos MENOS o periodo de contribuição ja passado.

infos['aposentadoria'] = anohoje + difaposent
#o ano de aposentadoria equivale ao ano de hoje + a diferença da aposentadoria

idadepos = (anohoje+difaposent) - nasc
#a idade da aposentadoria equivale ao ano de hoje MAIS a diferença da aposentadoria MENOS minha data de nascimento


print(f'Seu nome é {infos["nome"]}')
print(f'Você tem {infos["idade"]} anos')
#formatando as infos básicas

if ctps!=0:
    print(f'Considerando sua carteira de trabalho nº {infos["carteira"]}')
    print('E também considerando que o tempo minimo de contribuição com o INSS para se aposentar é de 35 anos...')
    print(f'Você irá se aposentar em {infos["aposentadoria"]}, com {idadepos} anos')
    #somente imprimo isso caso eu tiver colocado minha CTPS por lá.

elif ctps == 0:
    print('Os dados são insuficientes para calcular sua aposentadoria ou você não tem Carteira de Trabalho. Programa finalizado.')
    #caso contrário, eu imprimo isso na tela.
