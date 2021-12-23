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

    def passar_canal(self):





print("Aqui vamos a imprimir um exemplo: ")
controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm")
print(controle_remoto.altura)




















