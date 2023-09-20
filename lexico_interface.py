import tkinter as tk
from tkinter import filedialog
from lexico_processamento import le_arquivo

def abrir_arquivo():
    arquivo_path = filedialog.askopenfilename()
    entrada_caminho.delete(0, tk.END)
    entrada_caminho.insert(0, arquivo_path)

def processar_arquivo():
    caminho = entrada_caminho.get()
    if caminho:
        tokens = le_arquivo(caminho)
        resultado.config(text=f"{tokens}")
    else:
        resultado.config(text="Nenhum arquivo selecionado")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Selecionar Arquivo")
janela.geometry("600x400")  # Tamanho da janela

# Centralizar a janela na tela
largura_janela = janela.winfo_reqwidth()
altura_janela = janela.winfo_reqheight()
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = (largura_tela // 2) - (largura_janela // 2)
posicao_y = (altura_tela // 2) - (altura_janela // 2)
janela.geometry(f"+{posicao_x}+{posicao_y}")

# Rótulo principal
titulo = tk.Label(janela, text="Processamento de Arquivo", font=("Arial", 16))
titulo.pack(pady=10)

# Frame para a entrada e botões
frame = tk.Frame(janela)
frame.pack()

rotulo_caminho = tk.Label(frame, text="Caminho do Arquivo:")
rotulo_caminho.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entrada_caminho = tk.Entry(frame, width=40)
entrada_caminho.grid(row=0, column=1, padx=10, pady=5)
entrada_caminho.insert(0, "C:/Users/Gabriel/Documents/arquivo2.txt")

botao_selecionar = tk.Button(frame, text="Selecionar Arquivo", command=abrir_arquivo)
botao_selecionar.grid(row=0, column=2, padx=10, pady=5)

botao_processar = tk.Button(frame, text="Processar Arquivo", command=processar_arquivo)
botao_processar.grid(row=1, column=1, pady=10)

# Espaço para exibir o resultado
resultado = tk.Label(janela, text="", font=("Arial", 12), justify="left")
resultado.pack(pady=10)

janela.mainloop()
