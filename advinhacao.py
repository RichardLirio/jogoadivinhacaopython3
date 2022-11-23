print('***********************\nBem vindo ao jogo de adivinhação!\n***********************')
numero_secreto = 42

chute = int(input('digite um numero:'))

maior = chute>numero_secreto
menor = chute<numero_secreto
acertou = chute == numero_secreto

if(acertou):
    print('Parabés voce acertou!')
else:
    if(maior):
        print('Meu número é menor que {}!'.format(chute))
    elif(menor):
        print('Meu número é maior que {}!'.format(chute))

