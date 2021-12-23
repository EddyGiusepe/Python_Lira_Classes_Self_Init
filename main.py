'''
Aqui o professor Lira faz um exemplo com um controle remoto.

O controle remoto tem características (atributos) e tem métodos.
Característica: cor (Preto), altura, profundidade, largura, etc   ( coisas fixas)
Métodos: método de aumentar volume, método de selecionar canal, etc  (o que faz)
'''
class ControleRemoto:
    # O self --> seria o próprio control remoto
    def __init__(self, cor, altura, profundidade, largura):  # Inicializa a classe
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o canal")
        elif botao == "+":
            print("Diminuir o canal")



print("Aqui vamos a imprimir um primeiro CONTROLE: ")
controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
print(controle_remoto.altura)
controle_remoto.passar_canal("+")
print("")
print("Aqui vamos a imprimir um segundo CONTROLE: ")
controle_remoto2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")
print(controle_remoto2.cor)
controle_remoto2.passar_canal("-")

















