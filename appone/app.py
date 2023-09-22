# importar o App,Builder (GUI)
# # criar o nosso aplicativo
# # criar a função build

from kivy.app import App
from kivy.lang import Builder

GUI=Builder.load_file("tela.kv")


class MeuAplicativo(App):
   def build(self):
      return GUI


MeuAplicativo.()run()
