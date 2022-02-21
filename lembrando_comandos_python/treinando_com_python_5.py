'''
link de estudo: https://www.youtube.com/watch?v=aj4PEXq0zuc
'''
# Classe Lamapra: encendida e apagada
class Lamp:
    _ESTADOS = ["Lamp_encendida", "lamp_não_encendida"]

    def __init__(self, esta_encendida):
        self.esta_encendida = esta_encendida

    def show_lamp(self):
        if self.esta_encendida == True:
            print(self._ESTADOS[0])
        else:
            print(self._ESTADOS[1])

    def lamp_on(self):
        self.esta_encendida = True
        self.show_lamp()

    def lamp_off(self):
        self.esta_encendida = False
        self.show_lamp()


if __name__ == '__main__':
    lampara = Lamp(esta_encendida=False)
    menu = ''' Menu:
    0 --> Lampara OFF
    1 --> Lampara ON
    x --> Sair'''
    while True:
        print(menu)
        op = input("Escolha a opção desejada: ")
        if op == '0':
            lampara.lamp_off()
        elif op == '1':
            lampara.lamp_on()
        else:
            break


