class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano invalido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver Filme {filme}")
        elif self.plano == "premium":
            print(f"Ver Filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça Upgrade para premium para ver esse filme")
        else:
            print("Plano Inválido")



cliente = Cliente("Lira", "Lira@gmail.com", "basic")
print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")

# No botão de Upgrade
cliente.mudar_plano("premium")
# cliente.mudar_plano("blablablabla") # Aqui vai tratar o "erro" ... vai sair Plano inválido
print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")