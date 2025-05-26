import pandas as pd
from IPython import display
import random as rnd
import os
import random as rnd
from draws import Print
from getpass import getpass
from IA import GeminiClient
import unicodedata
import math

class Jogo:
  def __init__(self) -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'dados.csv')
    self.dados = pd.read_csv(csv_path).values.tolist()
    self.wordshow = []
    self.realword = []
    self.maxtries = 7
    self.tries = 0

  def remover_acentos(self,palavra):
    return ''.join(
        c for c in unicodedata.normalize('NFD', palavra)
        if unicodedata.category(c) != 'Mn'
    )

  def startgame(self, difficulty):   
    #Funções locais para evitar o uso repetitivo do self.
    def validate_words():
      words = []
      #se acertar a palavra inteira em uma única tentativa         
      #Se tentou colocar uma palavra inteira e errou
      if len(letter) > 1:
        for char in letter:  # Itera sobre cada caractere da palavra digitada
          if char in gameword:
            # Revela todas as posições onde o caractere aparece em gameword
            for i in range(len(gameword)):
                if gameword[i] == char:
                    self.wordshow[i] = gameword[i]
                    if char not in words:
                        words.append(char)
          else:
            # Se a letra não está em gameword, adiciona às incorretas
            if char not in wrongletters:
                wrongletters.append(char)
                self.tries += 1
                print(f"Letra {char} é incorreta")
        print("Letras corretas:", ', '.join(words))
        #se houver apenas uma letra no input
      else:
        if letter not in gameword.lower():
          wrongletters.append(letter)
          self.tries += 1
          print("Resposta incorreta!")
        else:
          print("Certa resposta!")
          for i in range(len(gameword)):
            if gameword[i].lower() == letter:
              self.wordshow[i] = gameword[i]
    #===============================================================
    def gamewon():
      gamestate = 2
      winstate = 1
    #================================================================
    def gameover():
      gamestate = 2
      winstate = 2
    #================================================================    
    wrongletters = []
    self.tries = 0
    self.wordshow = []
    #Estado local para vitória do jogo, assim é possível recomeçar o jogo várias vezes
    #1 ativo, 2 encerrado
    gamestate = 1
    # 0 inativo, 1 game win, 2 game over
    winstate = 0

    #define a dificuldade do jogo
    gameword = ''
    word_list = []
    if difficulty == '1':
      for letter in self.dados:
        if len(letter[0]) <= 4:
          word_list.append(letter)
      gameword = rnd.choice(word_list)[0]
    elif difficulty == '2':
      for letter in self.dados:
        if len(letter[0]) >= 5 and len(letter[0]) < 8:
          word_list.append(letter)
      gameword = rnd.choice(word_list)[0]
    elif difficulty == '3':
      for letter in self.dados:
        if len(letter[0]) >= 8:
          word_list.append(letter)
      gameword = rnd.choice(word_list)[0]
    else:
      gameword = rnd.choice(self.dados)[0]

    #Define a dica dada por IA
    cliente = GeminiClient()
    hint = cliente.call(gameword)    
    gameword = self.remover_acentos(gameword).lower()
    
    for letter in gameword:
      self.realword.append(letter)
      self.wordshow.append('_')
    
    while gamestate == 1:
      print("A palavra é:", ' '.join(self.wordshow))
      print('Dica:',hint)

      Print.print_hanger(Print,self.tries)
      print('Letras erradas:',','.join(wrongletters))

      letter = input('Coloque uma letra ou palavra: ').lower()
      print("\n" * 100)    
      if letter == gameword:
        gamewon()
        break
      if letter in wrongletters and len(letter) == 1:
        print("Você já tentou essa letra.")    
      elif not letter.isalpha():
        print("Não é permitido números ou caracteres especiais, apenas letras.")
      if len(letter) > len(gameword):
        print("A palavra digitada é maior que a palavra do jogo")
        continue
      else:
        validate_words()

      if self.tries >= self.maxtries:
        gameover()
        break
      elif '_' not in self.wordshow or winstate == 1:
        gamewon()
        break
    
    print('Fim de jogo! A palavra era:', gameword)