import tkinter as tk
import random

def change_color():
    # Gera três valores aleatórios entre 0 e 255 para os componentes RGB
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    # Converte os valores para uma cor hexadecimal
    color = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
    
    # Atualiza a cor de fundo da janela
    window.configure(bg=color)

# Cria uma janela
window = tk.Tk()

# Cria um botão na janela
button = tk.Button(window, text="Mudar cor", command=change_color)
button.pack()

# Executa o loop principal da janela
window.mainloop()
