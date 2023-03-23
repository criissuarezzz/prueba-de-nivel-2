import os
import sys
import helpers
import database as db

def menu():
    while True:
        helpers.limpiar_pantalla()
        print("·································")
        print("·········MENÚ DE PUNTOS··········")
        print("·································")
        print("        1. Crear punto")
        print("        2. Calcular cuadrante")
        print("        3. Calcular vector")
        print("        4. Calcular distancia")