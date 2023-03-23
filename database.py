import math

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