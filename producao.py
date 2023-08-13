from datetime import datetime


class Producao:
    def __init__(self):
        self.registros = []

    def registrar_producao(self, produtos):
        print("Registro de Produção:")
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade produzida: "))

        for produto in produtos:
            if produto.nome == nome:
                produto.unidades_produzidas.append(quantidade)
                self.registros.append((produto.nome, quantidade, datetime.now()))
                print("Produção registrada com sucesso.")
                return

        print("Produto não encontrado.")
