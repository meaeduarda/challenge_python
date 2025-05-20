''''
calculando fatorial. solicite um numero, e mostre e mostre seu fatorial

ex: 5! = 5x4x3x2x1 = 120
'''

# forma tradicional e mais simples de fazer - importe o math factorial

'''from math import factorial
numero = int(input('Digite um número: '))
f = factorial(numero)
print (f'O fatorial de {numero} é {f}')''' 


numero = int(input('Digite um número: '))
contador = numero # o contador deve iniciar com o valor que o usuario digitar
fatorial = 1
print (f'Calculando {numero}! =')

while contador > 0:
    print (f' {contador}',end='')
    print (' x ' if contador > 1 else ' = ',end='') # Esse printe usamos o c para ficar contadorxcontadorxcontador = total.
    fatorial *= contador
    contador -= 1
    print (f'{fatorial}')
    

    
    
   