from produto import Produto
from producao import Producao
from relatorios import GeradorRelatorios

def main():
    produtos = []
    producao = Producao()

    while True:
        print("Sistema de Gerenciamento de Produção")
        print("1. Cadastrar Produto")
        print("2. Registrar Produção")
        print("3. Ver Estoque")
        print("4. Rastrear Produto")
        print("5. Gerar Relatório")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = Produto.cadastrar_produto()
            produtos.append(produto)
        elif opcao == "2":
            producao.registrar_producao(produtos)
        elif opcao == "3":
            Produto.exibir_estoque(produtos)
        elif opcao == "4":
            Produto.rastrear_produto(produtos)
        elif opcao == "5":
            GeradorRelatorios.gerar_relatorio(produtos)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
