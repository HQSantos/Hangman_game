
import tkinter as tk

class Screen:
    def __init__(self) -> None:
      root = tk.Tk()
      root.title("Jogo da Forca")
      root.configure(background='light gray')

      self.root = root

      self.root.grid_columnconfigure(0, weight=1)
      self.root.grid_columnconfigure(1, weight=1)
      self.root.grid_columnconfigure(2, weight=1)
      
      # Primeira coluna: Botões e entrada
      self.left_frame = tk.Frame(self.root, bg='light gray')
      self.left_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
      
      #Seção de botões
      self.button_frame = tk.Frame(self.left_frame, bg='light gray')
      self.button_frame.pack(fill='x')

      self.novo_jogo_button = tk.Button(self.button_frame, text="Novo Jogo")
      self.novo_jogo_button.pack(side='left', padx=5, pady=5)

      self.mudar_dificuldade_button = tk.Button(self.button_frame, text="Mudar Dificuldade")
      self.mudar_dificuldade_button.pack(side='left', padx=5, pady=5)

      # Seção de entrada
      self.input_frame = tk.Frame(self.left_frame, bg='light gray')
      self.input_frame.pack(fill='x', pady=10)

      tk.Label(self.input_frame, text="Digite a letra ou palavra:", bg='light gray').grid(row=0, column=0, sticky='w')
      self.entry = tk.Entry(self.input_frame)
      self.entry.grid(row=0, column=1, padx=5)
      self.tentar_button = tk.Button(self.input_frame, text="Tentar")
      self.tentar_button.grid(row=0, column=2, padx=5)
      
      # seção de labels
      
      # Mensagens 
      self.word_frame = tk.Frame(self.left_frame, bg='light gray')  
      self.word_frame.pack(fill='x', pady=10)

      self.word_var = tk.StringVar()
      self.word_var.set("")
      self.word_label = tk.Label(self.word_frame, textvariable=self.word_var, bg='light gray')
      self.word_label.pack(fill='x', pady=10)

      # Seção de mensagens de erro
      self.message_frame = tk.Frame(self.left_frame, bg='light gray')
      self.message_frame.pack(fill='x', pady=10)

      self.message_var = tk.StringVar()
      self.message_var.set("Mensagens:")
      self.message_label = tk.Label(self.message_frame, textvariable=self.message_var, bg='light gray')
      self.message_label.pack()

      #total de letras da palavra
      self.total_frame = tk.Frame(self.left_frame, bg='light gray')
      self.total_frame.pack(fill='x', pady=5)

      tk.Label(self.total_frame, text="", bg='light gray').pack(side='left')
      self.total_letters_var = tk.StringVar()
      self.total_letters_label = tk.Label(self.total_frame, textvariable=self.total_letters_var, bg='light gray')
      self.total_letters_label.pack(fill='x', pady=10)


      # Segunda coluna: Informações do jogo e mensagens de erro
      self.mid_frame = tk.Frame(self.root, bg='light gray')
      self.mid_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

      # Seção de informações
      self.info_frame = tk.Frame(self.mid_frame, bg='light gray')
      self.info_frame.pack(fill='x')

      tk.Label(self.info_frame, text="Letras corretas:", bg='light gray').grid(row=0, column=0, sticky='w')
      self.correct_letters_var = tk.StringVar()
      self.correct_letters_var.set("")
      self.correct_letters_label = tk.Label(self.info_frame, textvariable=self.correct_letters_var, bg='light gray')
      self.correct_letters_label.grid(row=0, column=1, sticky='w')

      tk.Label(self.info_frame, text="Letras incorretas:", bg='light gray').grid(row=2, column=0, sticky='w')
      self.incorrect_letters_var = tk.StringVar()
      self.incorrect_letters_var.set("")
      self.incorrect_letters_label = tk.Label(self.info_frame, textvariable=self.incorrect_letters_var, bg='light gray')
      self.incorrect_letters_label.grid(row=2, column=1, sticky='w')

      # Terceira coluna: Imagem do personagem
      self.right_frame = tk.Frame(self.root, bg='light gray')
      self.right_frame.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)

      self.image_label = tk.Label(self.right_frame, text="Imagem do Personagem", bg='black', fg='white', width=360, height=450,)
      self.image_label.pack(expand=True, pady=20)
      

    @staticmethod
    def CenterScreen(janela, largura, altura):
      """
      Centraliza uma janela Tkinter com a largura e altura fornecidas.

      :param janela: instância de tk.Tk() ou tk.Toplevel()
      :param largura: largura desejada da janela em pixels
      :param altura: altura desejada da janela em pixels
      """
      janela.update_idletasks()  # Garante que winfo_screenwidth está atualizado

      screen_width = janela.winfo_screenwidth()
      screen_height = janela.winfo_screenheight()

      x = (screen_width // 2) - (largura // 2)
      y = (screen_height // 2) - (altura // 2)

      janela.geometry(f"{largura}x{altura}+{x}+{y}")