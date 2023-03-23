import math
import turtle


class Punto():
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    def cuadrante(self):
        if self.x>0 and self.y>0:
            return "El punto ({0}, {1}) está en el primer cuadrante".format(self.x, self.y)
        elif self.x<0 and self.y>0:
            return "El punto ({0}, {1}) está en el segundo cuadrante".format(self.x, self.y)
        elif self.x<0 and self.y<0:
            return "El punto ({0}, {1}) está en el tercer cuadrante".format(self.x, self.y)
        elif self.x==0 and self.y==0:
            return "El punto ({0}, {1}) está en el origen".format(self.x, self.y)
        else:
            return "El punto ({0}, {1}) está en el cuarto cuadrante".format(self.x, self.y)
    
    def vector(self, punto):
        return Punto(punto.x-self.x, punto.y-self.y)
    
    def distancia(self, punto):
        return math.sqrt(((punto.x-self.x)**2)+(punto.y-self.y)**2)

class Rectangulo:
    def __init__(self, p1, p2):
        self.p1= p1
        self.p2= p2
    
    def base(self):
        return self.p1.distancia(Punto(self.p2.x, self.p1.y))

    def altura(self):
        return self.p1.distancia(Punto(self.p1.x, self.p2.y))
    
    def area(self):
        return self.base * self.altura
    



class Punto_menu():
    @staticmethod
    def crear_punto():
        x=input("Introduce la coordenada x:")
        y=input("Introduce la coordenada y:")
        punto=Punto(x, y)
        print("Has creado el punto ({0})".format(punto))
    
    @staticmethod
    def cuadrante():
        x=int(input("Introduce la coordenada x:"))
        y=int(input("Introduce la coordenada y:"))
        punto=Punto(x,y)
        cuadrantep=Punto.cuadrante(punto)
        return cuadrantep
    
    @staticmethod
    def vector():
        x1=("Introduce la coordenada x del primer punto:")
        y1=("Introduce la coordenada y del primer punto:")
        x2=("Introduce la coordenada x del segundo punto:")
        y2=("Introduce la coordenada y del segundo punto:")

        p1=Punto(x1, y1)
        p2=Punto(x2, y2)
        opcion=input('¿quieres saber el vector P1P2 o el P2P1?(P1P2/P2P1):')
        if opcion == "P1P2":
            return "El vector formado por {0} y {1} es: {2}".format(p1, p2, p1.vector(p2))
        elif opcion =="P2P1":
            return "El vector formado por {0} y {1} es: {2}".format(p2, p1, p2.vector(p1))

    @staticmethod
    def distancia():
        x1=("Introduce la coordenada x del primer punto:")
        y1=("Introduce la coordenada y del primer punto:")
        x2=("Introduce la coordenada x del segundo punto:")
        y2=("Introduce la coordenada y del segundo punto:")

        p1=Punto(x1, y1)
        p2=Punto(x2, y2)
        return "La distancia entre {0} y {1} es: {2}". format(p1, p2, p1.distancia(p2))
    
    @staticmethod
    def mas_lejos():
        x1 = input("Introduce la coordenada x del primer punto: ")
        y1 = input("Introduce la coordenada y del primer punto: ")
        x2 = input("Introduce la coordenada x del segundo punto: ")
        y2 = input("Introduce la coordenada y del segundo punto: ")
        x3 = input("Introduce la coordenada x del tercer punto: ")
        y3 = input("Introduce la coordenada y del tercer punto: ")
        origen=Punto(0, 0)
        p1 = Punto(x1, y1)
        p2 = Punto(x2, y2)
        p3 = Punto(x3, y3)
        distanciap1=p1.distancia(origen)
        distanciap2=p2.distancia(origen)
        distanciap3=p3.distancia(origen)

        print("La distancia del punto {0} al origen es: {1}".format(p1, distanciap1))
        print("La distancia del punto {0} al origen es: {1}".format(p2, distanciap2))
        print("La distancia del punto {0} al origen es: {1}".format(p3, distanciap3))
        
        if distanciap1>distanciap2 and distanciap1>distanciap3:
            print("El punto {} es el más lejano al origen".format(p1))
        elif distanciap2>distanciap1 and distanciap2>distanciap3:
            print("El punto {} es el más lejano al origen".format(p2))
        elif distanciap3>distanciap1 and distanciap3>distanciap2:
            print("El punto {} es el más lejano al origen".format(p3))

    @staticmethod
    def rectangulo():
        x1 = input("Introduce la coordenada x del primer punto: ")
        y1 = input("Introduce la coordenada y del primer punto: ")
        x2 = input("Introduce la coordenada x del segundo punto: ")
        y2 = input("Introduce la coordenada y del segundo punto: ")
        p1 = Punto(x1, y1)
        p2 = Punto(x2, y2)
        rect = Rectangulo(p1, p2)
        return "El rectángulo tiene una base de {0} y una altura de {1}, uno de los vértices está en la coordenada {2}, y en diagonal encontramos el otro punto {3}".format(rect.base(), rect.altura(), p1, p2)
    
    @staticmethod
    def dibujarRectangulo():
        x1 = input("Introduce la coordenada x del primer punto: ")
        y1 = input("Introduce la coordenada y del primer punto: ")
        x2 = input("Introduce la coordenada x del segundo punto: ")
        y2 = input("Introduce la coordenada y del segundo punto: ")
        p1 = Punto(x1, y1)
        p2 = Punto(x2, y2)
        turtle.setup(400, 400)
        turtle.setworldcoordinates(-10, -10, 10, 10)
        turtle.penup()
        turtle.goto(p1.x, p1.y)   #goto es para mover la flecha, y recorre todo el rectangulo en funcion de las coordenadas que le demos
        turtle.pendown()
        turtle.goto(p2.x, p1.y)
        turtle.goto(p2.x, p2.y)
        turtle.goto(p1.x, p2.y)
        turtle.goto(p1.x, p1.y)
        turtle.done()

    
A= Punto(2,3)
B=Punto(5, 5)
C=Punto(-3, -1)
D=Punto(0,0)

print('\033[35m'+ "LOS CUADRANTES " + '\033[0m')
cuadranteA=A.cuadrante
print(cuadranteA())
cuadranteB=B.cuadrante
print(cuadranteB())
cuadranteC=C.cuadrante
print(cuadranteC())
cuadranteD=D.cuadrante()
print(cuadranteD)

print('\033[35m'+ "LOS VECTORES " + '\033[0m')
vectorAB=A.vector(B)
print("El vector AB es:", vectorAB)
vectorBA=B.vector(A)
print("El vector BA es:", vectorBA)

print('\033[35m'+ "DISTANCIAS" + '\033[0m')
distanciaAB=A.distancia(B)
print("La distancia de {0} a {1} es: {2}".format(A, B, distanciaAB))
distanciaBA=B.distancia(A)
print("La distancia entre {0} y {1}, es: {2}".format(B, A, distanciaBA))

print('\033[35m'+ "¿CUÁL ESTÁ MÁS LEJOS DEL ORIGEN? " + '\033[0m')
distanciaAD=A.distancia(D)
distanciaBD=B.distancia(D)
distanciaCD=C.distancia(D)
print("La distancia de A al origen es:", distanciaAD)
print("La distancia de B al origen es:", distanciaBD)
print("La distancia de C al origen es:", distanciaCD)
if distanciaAD>distanciaBD and distanciaAD>distanciaCD:
    print("El punto A es el más lejano al origen") 
elif distanciaBD>distanciaAD and distanciaBD>distanciaCD:
    print("El punto B es el más lejano al origen") 
elif distanciaCD>distanciaAD and distanciaCD>distanciaBD:
    print("El punto C es el más lejano al origen")

print('\033[35m'+ "RECTÁNGULO" + '\033[0m')
rect=Rectangulo(A,B)
print("El rectángulo tiene una base {0}, y altura {1}".format(rect.base(), rect.altura()))

print('\033[35m'+ "DIBUJAR EL RECTÁNGULO" + '\033[0m')
turtle.setup(400, 400)
#hacer el rectangulo mas grande y centrado
turtle.setworldcoordinates(-10, -10, 10, 10)
turtle.speed(1)
turtle.penup()  #penup es para levantar el lapiz y no dibujar
turtle.goto(A.x, A.y)   #goto (go to) es para mover la flecha, y recorre todo el rectangulo en funcion de las coordenadas que le demos
turtle.pendown()  #pendown es para bajar el lapiz y dibujar
turtle.goto(B.x, A.y)
turtle.goto(B.x, B.y)
turtle.goto(A.x, B.y)
turtle.goto(A.x, A.y)
turtle.done()   #trabajo terminado