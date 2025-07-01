import sys
import tkinter as tk
from game_screen import Screen
from game import Jogo

class TelaInicial:
    '''def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.geometry("1000x600")
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_tudo)
        self.dificuldade_var = tk.StringVar()
        self.dificuldade_var.set("0")
        self.ui_frame = None'''

    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.root.geometry("300x200")
        self.dificuldade_var = tk.StringVar(value="0")
        self.root.protocol("WM_DELETE_WINDOW", self.fechar_tudo)
        btn = tk.Button(root, text="Selecionar dificuldade", command=self.abrir_dificuldade)
        btn.pack(pady=20)

    def abrir_dificuldade(self):
        # Fecha a janela atual (opcional)
        self.root.withdraw()

        # Cria uma nova janela (filha, não Tk novamente!)
        nova_janela = tk.Toplevel()
        nova_janela.title("Escolher Dificuldade")
        nova_janela.geometry("300x200")
        Screen.CenterScreen(nova_janela, 300, 200)
        nova_janela.protocol("WM_DELETE_WINDOW", self.fechar_tudo)

        tk.Label(nova_janela, text="Escolha a dificuldade:").pack(anchor="w", padx=10)

        opcoes = [("Todas as palavras", "0"),
                  ("Fácil", "1"),
                  ("Médio", "2"),
                  ("Difícil", "3")]

        for texto, valor in opcoes:
            tk.Radiobutton(nova_janela, text=texto,
                           variable=self.dificuldade_var,
                           value=valor).pack(anchor="w", padx=20)

        def iniciar():
            print("Dificuldade escolhida:", self.dificuldade_var.get())
            nova_janela.destroy()
            self.confirmar_dificuldade()

        tk.Button(nova_janela, text="Iniciar Jogo", command=iniciar).pack(pady=10)
    '''def setup_ui(self):
        try:
            if  self.ui_frame is not None:
                self.ui_frame.destroy()
        except AttributeError:
            pass
        self.ui_frame = tk.Frame(self.root)
        self.ui_frame.pack(padx=10, pady=10)

        tk.Label(self.ui_frame, text="Escolha a dificuldade:").pack(anchor="w")

        tk.Radiobutton(self.ui_frame, text="Todas as palavras", variable=self.dificuldade_var, value="0").pack(anchor="w")
        tk.Radiobutton(self.ui_frame, text="Fácil", variable=self.dificuldade_var, value="1").pack(anchor="w")
        tk.Radiobutton(self.ui_frame, text="Médio", variable=self.dificuldade_var, value="2").pack(anchor="w")
        tk.Radiobutton(self.ui_frame, text="Difícil", variable=self.dificuldade_var, value="3").pack(anchor="w")

        for widget in self.ui_frame.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.deselect()

        self.dificuldade_var.set("0")
        tk.Button(self.ui_frame, text="Iniciar Jogo", command=self.confirmar_dificuldade).pack(anchor="w")'''


    def confirmar_dificuldade(self):
        nivel = self.dificuldade_var.get()
        self.root.withdraw()
        self.iniciar_jogo(nivel)


    def iniciar_jogo(self, dificuldade):
        jogo = Jogo(self)
        jogo.StartGame(dificuldade)


    def fechar_tudo(self):
        self.root.destroy()
        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    Screen.CenterScreen(root, 250, 200)
    root.mainloop()