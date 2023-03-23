import os
import platform

def limpiar_pantalla():      # Función para limpiar la pantalla
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')