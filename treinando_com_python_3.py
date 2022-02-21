'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro

link de estudo: https://www.codigofluente.com.br/algoritmo-linguagem-de-programacao/python/?orderby=title

Classes:
Construtor
Múltiplos argumentos para um método
'''

class Point:
    def __init__(self, x, y): # def __init__(self, x=0, y=0)
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)
'''
Obs: quando você compilar sem contruir o ponto abaixo, vai dar erro. Por que?
porque o construtor te obriga a passar valores a "x" e "y"
'''
# Construindo um ponto
point = Point(3, 5)
print(f"Nosso ponto é: {(point.x , point.y)}")


