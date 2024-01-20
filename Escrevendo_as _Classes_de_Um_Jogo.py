class jogador:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

        if tipo == "mago" :
            self.ataque = "magia"
        elif tipo == "guerreiro" :
            self.ataque = "espada"
        elif tipo == "monge" :
            self.ataque = "artes marciais"
        elif tipo == "ninja" :
            self.ataque = "shuriken"


nome = input('Digite o nome do jogador: ')
idade = int(input('Digite a idade do jogador: '))
tipo = input('Digite o tipo de jogador (mago, guerreiro, monge ou ninja): ')

novoJogador = jogador(nome, idade, tipo)
print(f'O {novoJogador.tipo} atacou usando {novoJogador.ataque}')


