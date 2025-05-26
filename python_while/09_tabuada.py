'''
Faça um programa que mostre a tabuada de varios números,um de cada vez, para cada valor digitado pelo usuario. O programa será interrompido(break) quando o numero solicitado for negativo

'''

incremento = resultado = 0

while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        print('Você digitou um número negativo. Digite um número positivo.')
        print(f'='*30)
        break
    print(f'='*30)
    for incremento in range (1,11):
        print (f'{numero} x {incremento} = {numero*incremento}')
    print(f'='*30)   
      
    
    