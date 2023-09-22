import tkinter as tk
from tkinter import filedialog

def salvar_arquivo():
    arquivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
    if arquivo is None:
        return
    conteudo = texto.get(1.0, tk.END)
    arquivo.write(conteudo)
    arquivo.close()

def abrir_arquivo():
    arquivo = filedialog.askopenfile(filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
    if arquivo is None:
        return
    texto.delete(1.0, tk.END)
    conteudo = arquivo.read()
    texto.insert(tk.END, conteudo)
    arquivo.close()

janela = tk.Tk()
janela.title("Bloco de Notas")

texto = tk.Text(janela)
texto.pack()

menu = tk.Menu(janela)
janela.config(menu=menu)

menu_arquivo = tk.Menu(menu)
menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)

janela.mainloop()
