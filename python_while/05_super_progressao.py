'''
Gerador de PA:
leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while e em seguida pergunte se o usuario quer mostrar mias termos. O programa termina quando ele clicar em 0
'''
print('GERADOR DE PA')
print ('=-'*10)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 1 
total = 0
mais_termos = 10
while mais_termos != 0:
    total = total + mais_termos
    while contador <= total:
        print (f' {termo} -> ', end='')
        termo += razao
        contador += 1
    print (' Pausa ')
    mais_termos = int(input('Quantos termos voce quer mostrar a mais? '))
print (f'o total de termos foi de {total}')
print ('FIM')

