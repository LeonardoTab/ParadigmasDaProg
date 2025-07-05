# Gerenciamento básico de estoque - Paradigma Orientado a Objetos / Imperativo
# Este programa permite controlar a entrada e saída de produtos em um estoque,
# utilizando classes para representar produtos e o estoque em si.

import csv  # Importa o módulo csv para salvar os dados

class Produto:
    def __init__(self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    def __str__(self):
        return f"Código: {self.codigo} | Nome: {self.nome} | Quantidade: {self.quantidade}"

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, codigo, nome, quantidade):
        if codigo in self.produtos:
            self.produtos[codigo].quantidade += quantidade
        else:
            self.produtos[codigo] = Produto(codigo, nome, quantidade)

    def remover_produto(self, codigo, quantidade):
        if codigo in self.produtos:
            if self.produtos[codigo].quantidade >= quantidade:
                self.produtos[codigo].quantidade -= quantidade
                if self.produtos[codigo].quantidade == 0:
                    del self.produtos[codigo]
                return True
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado.")
        return False

    def listar_produtos(self):
        if not self.produtos:
            print("Estoque vazio.")
        else:
            for produto in self.produtos.values():
                print(produto)

    def buscar_produto(self, codigo):
        return self.produtos.get(codigo, None)

    def salvar_csv(self, nome_arquivo):
        # Salva os produtos do estoque em um arquivo CSV
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(['codigo', 'nome', 'quantidade'])  # Cabeçalho
            for produto in self.produtos.values():
                escritor.writerow([produto.codigo, produto.nome, produto.quantidade])
        print(f'Estoque salvo em {nome_arquivo}')

def menu():
    estoque = Estoque()
    while True:
        print("\n--- Menu de Gerenciamento de Estoque ---")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Buscar produto")
        print("5. Salvar estoque em CSV")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            codigo = input("Código do produto: ")
            nome = input("Nome do produto: ")
            try:
                quantidade = int(input("Quantidade: "))
                estoque.adicionar_produto(codigo, nome, quantidade)
                print("Produto adicionado com sucesso!")
            except ValueError:
                print("Quantidade inválida.")
        elif opcao == '2':
            codigo = input("Código do produto: ")
            try:
                quantidade = int(input("Quantidade a remover: "))
                if estoque.remover_produto(codigo, quantidade):
                    print("Produto removido com sucesso!")
            except ValueError:
                print("Quantidade inválida.")
        elif opcao == '3':
            estoque.listar_produtos()
        elif opcao == '4':
            codigo = input("Código do produto: ")
            produto = estoque.buscar_produto(codigo)
            if produto:
                print(produto)
            else:
                print("Produto não encontrado.")
        elif opcao == '5':
            nome_arquivo = input("Digite o nome do arquivo CSV para salvar (ex: estoque.csv): ")
            estoque.salvar_csv(nome_arquivo)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
