'''
Gerador de PA:
leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
'''
print('GERADOR DE PA')
print ('=-'*10)
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
contador = 1 

while contador <= 10:
    print (f' {termo} -> ', end='')
    termo += razao
    contador += 1
print (' FIM ')