import math

class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def __str__(self):
        return "Has creado el punto ({0}, {1})".format(self.x, self.y)
    def cuadrante(self):
        if self.x>0 & self.y>0:
            return "El punto ({0}, {1}) está en el primer cuadrante"
        elif self.x<0 & self.y>0:
            return "El punto ({0}, {1}) está en el segundo cuadrante"
        elif self.x<0 % self.y<0:
            return "El punto ({0}, {1}) está en el tercer cuadrante"
        else:
            return "El punto ({0}, {1}) está en el cuarto cuadrante"
    
    def vector(self, punto):
        return Punto(punto.x-self.x, punto.y-self.y)
    
    def distancia(self, punto):
        return math.sqrt(((punto.x-self.x)**2)+(punto.y-self.y)**2)
    
    