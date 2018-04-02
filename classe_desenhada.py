# Base e Altura tenha no máximo 10 e Min 2
# print em forma de desenho

class Retangulo:

    def __init__(self):
        self._seta_lado()

    def _seta_lado(self):
        self.base = int(input('tamanho da base:(min. 2 / max 10) '))
        self.altura = int(input('tamanho da altura:(min. 2 / max 10) '))

    def _limite(self):
        self.base = max(min(self.base, 10), 2)
        self.altura = max(min(self.altura, 10), 2)

    def imagens(self):
        print(self.base * '-')

        for i in range(self.altura - 2):
            espaco = self.base - 4
            espaco = espaco * ' '
            print('|', espaco, '|')

        print(self.base * '-')

retangulo = Retangulo()
retangulo.imagens()
