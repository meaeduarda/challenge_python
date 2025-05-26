'''
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo 

digite um valor: 
Par ou Impart [P/I]?

--------------------------
voce jogou -- e o computador --. O total é --, deu --
---------------
Voce Ganhou ou Perdeu 
--------------
GAME OVER. Voce venceu --- vezes
-------------
'''

from random import randint

vitorias = 0

while True:
    # Entrada do jogador
    jogador = int(input("Digite um valor: "))
    computador = randint(0, 10)
    soma = jogador + computador

    # Perguntando ao jogador se ele quer par ou ímpar
    resposta = ""
    while resposta not in ["P", "I"]:
        resposta = input("Você escolhe Par ou Ímpar? [P/I] ").strip().upper()[0]

    # Exibição dos valores
    print(f"Você jogou {jogador} e o computador jogou {computador}. O total é {soma}, ", end="")

    if soma % 2 == 0:
        print("deu PAR.")
        resultado = "P"
    else:
        print("deu ÍMPAR.")
        resultado = "I"

    # Verificação do vencedor
    if resposta == resultado:
        print("Você venceu!")
        vitorias += 1
        print("Vamos jogar novamente...\n")
    else:
        print("Você perdeu!")
        break

# Exibição do total de vitórias consecutivas
print(f"GAME OVER! Você venceu {vitorias} vezes.")


        
    

      
