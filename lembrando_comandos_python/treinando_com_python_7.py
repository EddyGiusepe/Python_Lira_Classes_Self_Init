'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro

Link de estudo: https://www.youtube.com/watch?v=E76ErVQ1xNI&list=PLqlQ2-9ypflT5Lx864RXtJx4s7i3sxgs0&index=16
'''
# Python: Herença
'''
A herença é a capacidade que tem uma classe de heredar os ATRIBUTOS e MÉTODOS de outra, isso nos ajuda a reutilizar
código e fazer que nossos programas sejam muito mais ótimos.  
'''

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas 

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        cad = "color {}, {} km/h, {} ruedas, {} cc"
        return cad.format(self.color, self.velocidad, self.ruedas, self.cilindrada)


if __name__ == "__main__":
    print("Testamos a classe Vehiculo: ")
    # Instânciamos um objeto
    x = Vehiculo("azul", 4)
    print(x)
    print("")
    print("Testamos a classe coche: ")
    # Instânciamos um objeto
    y = Coche("azul", 4, 120, 1500)
    print(y)