import sys
import unicodedata
import pandas as pd
import os
import random as rnd
from draws import Printer
from IA import GeminiClient
import tkinter as tk
from game_screen import Screen
import threading
class Jogo:
    def __init__(self, menu):
        self.menu = menu
        if hasattr(sys, '_MEIPASS'):
            base_dir = sys._MEIPASS
        else:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        csv_path = os.path.join(base_dir, "assets", "dados.csv")

        with open(csv_path, 'r', encoding='utf-8') as f:
            self.dados = pd.read_csv(f).values.tolist()

        self.tela = Screen(menu.root)
        self.wordshow = []
        self.realword = []
        self.wrongletters = []
        self.correctletters = []
        self.maxtries = 6
        self.tries = 0
        self.winstate = False
        self.gameword = ''
        self.difficulty = ''
        self.tela.root.protocol("WM_DELETE_WINDOW", self.fechar_tudo)


    def NewGame(self):
        self.wordshow = []
        self.realword = []
        self.wrongletters = []
        self.correctletters = []
        self.winstate = False
        self.tries = 0
        self.gameword = ''
        self.tela.message_var.set('')
        self.StartGame(self.difficulty)
        self.SetupScreen(self.tela)
    

    def ChangeDifficulty(self):
        from main import TelaInicial
        self.tela.root.withdraw()

        new_root = tk.Tk()
        new_menu = TelaInicial(new_root)
        Screen.CenterScreen(new_root, 250, 200)
        #new_menu.setup_ui()



    def StartGame(self, difficulty):  
        self.difficulty 
        word_list = []
        self.gameword = ''
        if difficulty == '1':
            for letter in self.dados:
                if len(letter[0]) <= 4:
                    word_list.append(letter)
            self.gameword = rnd.choice(word_list)[0]
        elif difficulty == '2':
            for letter in self.dados:
                if len(letter[0]) >= 5 and len(letter[0]) < 8:
                    word_list.append(letter)
            self.gameword = rnd.choice(word_list)[0]
        elif difficulty == '3':
            for letter in self.dados:
                if len(letter[0]) >= 8:
                    word_list.append(letter)
            self.gameword = rnd.choice(word_list)[0]
        else:
            self.gameword = rnd.choice(self.dados)[0]
        
        for letter in self.gameword:
            self.realword.append(letter)
            self.wordshow.append('_')
        
        self.gameword = self.RemoveAccent()
        cliente = GeminiClient()
        palavra = cliente.call(self.gameword)
        if palavra:
            self.carregar_dica_em_background()
        else:
            self.tela.total_letters_var.set(f"Total de letras: {len(self.gameword)}\nDica: {cliente.call(self.gameword)  }")
        self.tela.word_var.set(' '.join(self.wordshow))
        self.SetupScreen(self.tela)
        self.tela.root.mainloop()



    def SendWord(self, letter):
        def validate_input():
            mensagem = ""
            if len(letter) > 1:
                mensagem = self.FullWordValidate(letter)
            else:
                mensagem = self.SingleWordValidate(letter)            
            
            self.tela.correct_letters_var.set(','.join(self.correctletters))
            self.tela.incorrect_letters_var.set(','.join(self.wrongletters))
            self.tela.message_var.set(mensagem)



        if not self.winstate:
            if letter == self.gameword:
                self.GameWon()
            if (letter in self.wrongletters or letter in self.correctletters) and len(letter) == 1:
                self.tela.message_var.set("Você já tentou essa letra.")                
            elif not letter.isalpha():
                self.tela.message_var.set("Não é permitido números ou caracteres especiais, apenas letras.")            
            if len(letter) > len(self.gameword):
                self.tela.message_var.set("A palavra digitada é maior que a palavra do jogo")       
            else:
                validate_input()

        self.tk_image = Printer.PrintHanger(self.tries)
        self.tela.image_label.config(image=self.tk_image)
        self.tela.image_label.image_names = self.tk_image 

        self.tk_image = Printer.PrintHanger(self.tries)
        self.tela.image_label.config(image=self.tk_image, text="")

        if self.tries >= self.maxtries:
            self.GameOver()            
        elif '_' not in self.wordshow:
            self.GameWon()



    def SetupScreen(self, tela):
        Screen.CenterScreen(tela.root, 1200, 500)
        tela.novo_jogo_button.config(command=lambda: self.NewGame())
        tela.mudar_dificuldade_button.config(command=lambda: self.ChangeDifficulty())
        tela.entry.bind("<Return>",  lambda event: (self.SendWord(tela.entry.get().lower()), tela.entry.delete(0, tk.END)))
        tela.tentar_button.config(command=lambda: (self.SendWord(tela.entry.get().lower()), tela.entry.delete(0, tk.END)))
        self.tries = 0
        self.tk_image = Printer.PrintHanger(self.tries)
        tela.image_label.config(image=self.tk_image)
        self.tela.message_var.set('')
        self.tela.correct_letters_var.set('')
        self.tela.incorrect_letters_var.set('')



    def FullWordValidate(self, input_word):
        mensagem = ''
        # Itera sobre cada caractere da palavra digitada
        for char in input_word:
            # Se a letra está em gameword, adiciona às corretas
            if char in self.gameword and char not in self.correctletters:
                self.reveal_correct_positions(char, self.gameword)
                self.correctletters.append(char)
                mensagem += f"'{char}' está na palavra! \n"
                

            #Se não está em nenhuma das listas, inclui nas palavras incorretas
            elif char not in self.wrongletters and char not in self.correctletters:
                self.wrongletters.append(char)
                self.tries += 1
                mensagem += f"'{char}' não está na palavra. \n"
        
        return mensagem


    def SingleWordValidate(self, letter):
        mensagem = ''
        if letter in self.gameword and letter not in self.correctletters:
            mensagem = f"'{letter}' está na palavra!"
            self.reveal_correct_positions(letter, self.gameword)
            self.correctletters.append(letter)
        elif letter not in self.wrongletters:
            self.wrongletters.append(letter)
            self.tries += 1
            mensagem = f"'{letter}' não está na palavra."
        
        return mensagem

  
  
    def reveal_correct_positions(self, char, gameword):
        # Revela todas as posições onde o caractere aparece em gameword
        for i, game_char in enumerate(gameword):
            if game_char == char:
                self.wordshow[i] = game_char

        self.tela.word_var.set(' '.join(self.wordshow))


    def RemoveAccent(self):
        return ''.join(
            c for c in unicodedata.normalize('NFD', self.gameword)
            if unicodedata.category(c) != 'Mn'
        )      
        

    def GameWon(self):
        self.SetWinState(True)
        self.tela.word_var.set(' '.join(self.gameword))
        self.tela.message_var.set('FIM DE JOGO, VOCÊ GANHOU')


    def GameOver(self):
        self.SetWinState(True)
        self.tela.message_var.set(f'FIM DE JOGO, VOCÊ PERDEU \n A PALAVRA ERA {self.gameword.upper()}')        


    def SetWinState(self, value):        
        self.winstate = value


    def fechar_tudo(self):
        self.tela.root.destroy()
        self.menu.root.destroy()
        sys.exit()


    def carregar_dica_em_background(self):
        def task():
            cliente = GeminiClient()
            dica = cliente.call(self.gameword)
            self.tela.total_letters_var.set(
                f"Total de letras: {len(self.gameword)}\nDica: {dica}"
            )

        threading.Thread(target=task).start()

