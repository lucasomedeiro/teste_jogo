class Inventario:
    def __init__(self, capacidade=3):
        self.capacidade = capacidade
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)
        return True

    def remover(self, item):
        self.itens.remove(item)
        return True

    def tem_item(self, item):
        return item in self.itens

    def esta_cheio(self):
        return len(self.itens) >= self.capacidade

    def quantidade(self):
        return len(self.itens)
