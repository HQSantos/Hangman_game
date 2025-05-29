import tkinter as tk
from game_screen import Screen
from game import Jogo

class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.setup_ui()

    def setup_ui(self):
        ui_frame = tk.Frame(self.root)
        ui_frame.place(relx=0.5,# rely=0.5,
                        anchor="n")

        # Adicionar o label
        tk.Label(ui_frame, text="Escolha a dificuldade:").pack(side="top", anchor="w")
        self.dificuldade_var = tk.StringVar(value="0")

        # Adicionar os radiobuttons
        tk.Radiobutton(ui_frame, text="Todas as palavras", variable=self.dificuldade_var, value="0").pack(side="top", anchor="w")
        tk.Radiobutton(ui_frame, text="Fácil", variable=self.dificuldade_var, value="1").pack(side="top", anchor="w")
        tk.Radiobutton(ui_frame, text="Médio", variable=self.dificuldade_var, value="2").pack(side="top", anchor="w")
        tk.Radiobutton(ui_frame, text="Difícil", variable=self.dificuldade_var, value="3").pack(side="top", anchor="w")

        # Botão para confirmar
        tk.Button(ui_frame, text="Iniciar Jogo", command=self.confirmar_dificuldade).pack(side="bottom", anchor="w")
    
    def confirmar_dificuldade(self):
        nivel = self.dificuldade_var.get()  
        self.root.destroy()
        self.iniciar_jogo(nivel)

    def iniciar_jogo(self, dificuldade):
        jogo = Jogo(self) # type: ignore
        jogo.StartGame(dificuldade)

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    Screen.CenterScreen(root, 250, 200)
    root.mainloop()