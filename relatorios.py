class GeradorRelatorios:
    @staticmethod
    def gerar_relatorio(produtos):
        print("Relatório de Produção e Vendas")
        for produto in produtos:
            total_produzido = sum(produto.unidades_produzidas)
            total_vendido = sum(produto.unidades_vendidas)
            estoque_atual = total_produzido - total_vendido
            print(f"{produto.nome}:")
            print(f"  Total produzido: {total_produzido}")
            print(f"  Total vendido: {total_vendido}")
            print(f"  Estoque atual: {estoque_atual}")
