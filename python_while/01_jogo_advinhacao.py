'''faça um jogo que exiba a mensagem 'sou seu comutador... acabei de pensar em um numero entre 0 e 10 .Será que voce consegue advinhar. A mensagem qual é o seu palpite deve ser exibida e o programa deve sugerir que um valor é maior ou menor ate que chegue a resposta. Ao final. Informe quantas tentativas foram usadas e parabenize o usuario'''

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
tentativas = 0
while not acertou:
    palpite = int(input('Qual é o seu palpite entre [0 e 10]? '))
    tentativas += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print('Está quente. É um valor maior.Tente mais uma vez')
        elif palpite > computador:
            print ('Está quente... É um valor menor. Tente mais uma vez')
print('Acertou!!')
print('Com {} tentativas. Parabéns!!'.format(tentativas))


