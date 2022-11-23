print('***********************\nBem vindo ao jogo de adivinhação!\n***********************')
numero_secreto = 42
total_de_tentativas = 3
rodada = 1
while(rodada <= 3 ):

    print('Rodada {0}/{1}'.format(rodada,total_de_tentativas))
    chute = int(input('digite um numero:'))
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acertou = chute == numero_secreto
    
    if(acertou):
        print('Parabés voce acertou!')
        rodada = 4
    else:
        if(maior):
            print('Meu número é menor que {}'.format(chute))
        elif(menor):
            print('Meu número é maior que {}'.format(chute))
        rodada = rodada + 1
    

print('Fim do jogo!')        
