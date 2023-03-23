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
        print("        2. Consultar cuadrante")
        print("        3. Calcular vector")
        print("        4. Calcular distancia")
        print("        5. Crear rectángulo")
        print("        6. Dibujar rectángulo")
        print("        7. Salir")
        print("·································")

        opcion = input("Elige una opción: ")
        helpers.limpiar_pantalla()
        if opcion == "1":
            print("Has elegido la opción 1, crear punto")
            op=input("¿desea continuar?(s/n)")
            if op == "s":
                db.Punto_menu.crear_punto()
            else:
                print("Has elegido no continuar")
        
        elif opcion=="2":
            print("Has elegido la opción 2, consultar cuadrante")
            op=input("¿desea continuar?(s/n)")
            if op == "s":
                db.Punto_menu.cuadrante()
            else:
                print("Has elegido no continuar")
        
        elif opcion=="3":
            
