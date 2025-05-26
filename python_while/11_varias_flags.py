'''
Leia um programa que leia varios numeros pelo teclado. O programa só vai parar quando o usuario digitar 999. Que é a condição de parada, no final, mostre quantos numeros foram digitados e qual foi a soma entre eles desconsiderando o flag usando break 

'''
numero = cont=soma = 0
while True:
    numero = int (input('Digite um valor: [999 para parar]'))
    if numero == 999:
        break 
    cont += 1
    soma += numero
print(f'A soma dos valores foi {soma}')
print(f'Você digitou {cont} numeros')
print('Acabou')