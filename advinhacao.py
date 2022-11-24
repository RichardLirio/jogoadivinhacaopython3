print('***********************\nBem vindo ao jogo de adivinhação!\n***********************')
numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1,total_de_tentativas+1):

    print('Rodada {0}/{1}'.format(rodada,total_de_tentativas))
    chute = int(input('digite um numero entre 0 e 100:\n'))
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acertou = chute == numero_secreto
    if(chute < 1 or chute > 100):
        print('Voce deve digitar um numero entre 1 e 100!')
    else:
        if(acertou):
            print('Parabés voce acertou!')
            break
            
        else:
            if(maior):
                print('Meu número é menor que {}'.format(chute))
            elif(menor):
                print('Meu número é maior que {}'.format(chute))
        
    

print('Fim do jogo!')        
