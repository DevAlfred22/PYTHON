import tkinter as tk
import kivy

# Exemplo usando tkinter
window = tk.Tk()
label = tk.Label(window, text="Olá, mundo!")
label.pack()
window.mainloop()

# Exemplo usando kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Olá, mundo!")

MyApp().run()
