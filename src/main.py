from game import Jogo

def main():
    print('Bem-vindo ao jogo da forca')
    print('===========================')
    letter = '1'
    jogo = Jogo()
    while letter == '1':
        print('Selecione a dificuldade do jogo:')
        print('0: Todas as letras   1: Fácil')
        print('2: Médio             3: Difícil')
        letter = input('').lower()
        print("\n" * 100) 
        jogo.startgame(letter)
        print('Deseja jogar novamente?:')
        print('1-Sim:')
        print('0-Não:')
        letter = input('').lower()

if __name__ == "__main__":
    main()