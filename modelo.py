from random import randint

class Programa:  # Classe mãe / SuperClasse
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):  # Herança
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return("{} - {} - {} min - Likes: {}"
               .format(self.nome, self.ano, self.duracao, self.likes))

class Serie(Programa):  # Herança
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return("{} - {} - {} temporadas - Likes: {}"
               .format(self.nome, self.ano, self.temporadas, self.likes))

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

avengers_endgame = Filme('vingadores: ultimato', 2018, 160)
spiderman_nwh = Filme('homem-aranha: sem volta pra casa', 2021, 180)
stranger_things = Serie('stranger things', 2016, 4)
flash = Serie("the flash", 2014, 8)

lista = [avengers_endgame, stranger_things, spiderman_nwh, flash]

for programa in lista:  # Dar um numero random de likes
    for _ in range(randint(1, 10)):
        programa.dar_like()

playlist = Playlist("playlist", lista)

for programa in lista:
    print(programa)

print(f'Tamanho da playlist: {len(playlist)}')
print(f'Tá ou não tá? {avengers_endgame in playlist}')
