'''
As linguagens de prograçaão tem tres  estrutura de controle while, for, repeat - mas em python temos os while e do for 

estruturas de repetição com teste lógico no inicio e com teste logico no final 

#teste no inicio
enquanto não chegar na maça
    fazer loop
    se tiver chao 
    passo
    se tiver absmo 
    pula
    se tiver moeda 
    pegar
pegar maça 

Vamos fazer o teste lógico no final 

enquanto 
    se tiver chao
    fazer loop
    se tiver chao 
    passo
    se tiver absmo 
    pula
    se tiver moeda 
    pegar
    se tiver trofeu
    pula
    para --> (desvia para fora do laço)
acabou 

enquanto Verdadeiro
    se chao 
    passo
    se abismo
    pula
    se moeda
    pega
    se trofeu
    pula
    interrompa
pega

================================
while True:
    if chao
        passo
    if abismo
        pula
    if moeda
        pega
    if trofeu 
        pula
        break

pega    
------------------------------

Como funciona o comando break?
'''

'''
n = cont = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999: # o valor do flag e usamos o break para interromper
        break
    s += n    
print(f'A soma vale {s}') #interpolação dentro da string - e o fstring 
'''

'''Desafio. Crie um programa que leia varios numeros inteiros. O programa só para com o 999. No final mostre quantos numeros digitados e a soma entre eles desconsiderando o flag'''

numero = contador = soma = 0
while True:
    numero = int(input("Digite um valor: [999 para parar]"))
    if numero == 999: # o valor do flag e usamos o break para interromper
        break
    soma += numero 
    
    if numero == 999:
        break
    contador += 1 

print(f'Você digitou {contador} números')  
print(f'A soma vale {soma}') #interpolação dentro da string - e o fstring 


