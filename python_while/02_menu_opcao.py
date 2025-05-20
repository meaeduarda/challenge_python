'''
Faça um programa que solicite 2 numeros ao usuario e em seguida apareça um menu de opções
[1] somar
[2] multiplicar
[3] maior 
[4] novos números
[5] sair do programa
'''

primerio_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
opcao = 0


while opcao != 5:

    print ('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
        ''')
    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        soma = primerio_valor + segundo_valor
        print(f'A soma entre {primerio_valor} e {segundo_valor} é {soma}')
    elif opcao == 2:
        produto = primerio_valor * segundo_valor
        print(f'A multiplicação entre {primerio_valor} e {segundo_valor} é {produto}')
    elif opcao == 3:
        if primerio_valor > segundo_valor:
            maior = primerio_valor
        else: 
            maior = segundo_valor
        print(f'Entre {primerio_valor} e {segundo_valor} o maior valor é {maior}')
    elif opcao == 4:
        print ('Informe os numeros novamente?')
        primerio_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))

    elif opcao == 5:
        print ('Finalizando...')
    else:
        print('Opção invalida!! Digite um dos numeros do menu')
    print('=-='*10)
print('Fim do programa')




