class Produto:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.unidades_produzidas = []
        self.unidades_vendidas = []

    @staticmethod
    def cadastrar_produto():
        print("Cadastro de Produto:")
        nome = input("Nome do produto: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        return Produto(nome, descricao, preco)

    @staticmethod
    def exibir_estoque(produtos):
        print("Estoque:")
        for produto in produtos:
            total_produzido = sum(produto.unidades_produzidas)
            total_vendido = sum(produto.unidades_vendidas)
            estoque_atual = total_produzido - total_vendido
            print(f"{produto.nome}: Estoque: {estoque_atual}")

    @staticmethod
    def rastrear_produto(produtos):
        nome = input("Nome do produto: ")
        for produto in produtos:
            if produto.nome == nome:
                print(f"Histórico de produção de {produto.nome}: {produto.unidades_produzidas}")
                return
        print("Produto não encontrado.")
