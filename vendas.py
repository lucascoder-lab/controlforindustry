class Vendas:
    def __init__(self):
        self.registros = []

    def registrar_venda(self, produtos):
        print("Registro de Venda:")
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade vendida: "))

        for produto in produtos:
            if produto.nome == nome:
                if produto.unidades_produzidas - produto.unidades_vendidas >= quantidade:
                    produto.unidades_vendidas.append(quantidade)
                    self.registros.append((produto.nome, quantidade, datetime.now()))
                    print("Venda registrada com sucesso.")
                    return
                else:
                    print("Estoque insuficiente para realizar a venda.")
                    return

        print("Produto não encontrado.")
