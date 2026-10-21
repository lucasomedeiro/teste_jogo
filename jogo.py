class Jogador:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.pontos = 0

    def receber_dano(self, dano):
        self.vida = self.vida - dano

    def curar(self, quantidade):
        self.vida = self.vida + quantidade

    def esta_vivo(self):
        return self.vida > 0

    def ganhar_pontos(self, pontos):
        self.pontos = self.pontos + pontos
