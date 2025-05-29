import os
from PIL import Image, ImageTk

class Printer():
    @staticmethod
    def PrintHanger(tries):
        largura = 360
        altura = 450
        base_path = os.path.dirname(__file__)
        imagem_path = os.path.join(base_path, '..', 'assets', 'f"{tries}.png')
        try:
            imagem = Image.open(imagem_path)
            imagem = imagem.resize((largura, altura), Image.Resampling.LANCZOS)  
            return ImageTk.PhotoImage(imagem)
        except FileNotFoundError:
            print(f"Erro: Imagem não encontrada em {imagem_path}")
            return None