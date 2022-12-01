def jogar():
    print('***************************\nBem vindo ao jogo da Forca!\n***************************')

    palavra_secreta = 'banana'
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute =(input('Qual letra? ')).lower()
        index = 0

        for letra in palavra_secreta:
            if (chute == letra):
                print('Encontrei a letra {0} na posição:{1} '.format(chute,index))
            index = index + 1

      

                
    
   
    
    
    print('Fim de jogo!')





if(__name__ == '__main__'):
    jogar()