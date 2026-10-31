"""Aula 11 - Lógica de Programação | Desafio Garagem Inteligente

Complete apenas os trechos TODO. Execute em um compilador Python online.
"""

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibirInfo(self):
        # TODO 1: substitua pass por um print() que mostre marca, modelo e ano.
        print(f"Marca: {self.marca} |  Modelo: {self.modelo} | Ano: {self.ano}")

# TODO 2: crie DOIS objetos usando a classe Carro.
carro1 = Carro("Toyota", "Hylux", 2016)
carro2 = Carro("volkswagen", "Polo ", 2024)

# TODO 3: chame exibirInfo() para os DOIS objetos criados.
carro1.exibirInfo()
carro2.exibirInfo()
