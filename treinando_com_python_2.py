'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Programação orientada a objetos
# Criamos a nossa primeira classe
# Calcularemos a DISTÂNCIA EUCLIDIANA

import math

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)            

# Instanciamos dois pontos
point1 = Point()
point2 = Point()

# Reseteamos nossos pontos
point1.reset()
print("Depois de reset, o x = ", point1.x)
print("Depois de reset, o y = ", point1.y)

# O outro ponto2 será
point2.move(5, 0)
print(f"O outro ponto será: (x, y) = {(point2.x, point2.y)}")

# Calculando a distância
print(point1.calculate_distance(point2))

# Movemos os ponto1 e calculamos a nova distância
point1.move(3, 4)
print(point1.calculate_distance(point2))