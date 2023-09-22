import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar uma música
pygame.mixer.music.load('caminho/para/o/arquivo/musica.mp3')

# Reproduzir a música
pygame.mixer.music.play()

# Manter o programa em execução até que a música termine de tocar
while pygame.mixer.music.get_busy():
    continue
