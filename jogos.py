import forca
import advinhacao

def escolhe_jogo():
    print('LISTA DE JOGOS:\n(1)Advinhação\n(2)Forca')
    jogo = int(input('Selecione qual jogo voce deseja jogar:'))

    if(jogo == 1):
        print('Voce selecionou o jogo de Advinhação.\nBoa sorte!')
        advinhacao.jogar()
        
    elif(jogo == 2):
        print('Voce selecionou o jogo da Forca.\nBoa sorte!')
        forca.jogar()

if(__name__ == '__main__'):
    escolhe_jogo()