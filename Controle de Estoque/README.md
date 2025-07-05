# Gerenciamento Básico de Estoque

Este projeto é um sistema simples de gerenciamento de estoque desenvolvido em Python, utilizando o paradigma orientado a objetos e imperativo.

## Funcionalidades
- **Adicionar produto:** Insere um novo produto ou incrementa a quantidade de um produto já existente.
- **Remover produto:** Remove uma quantidade específica de um produto do estoque.
- **Listar produtos:** Exibe todos os produtos cadastrados no estoque.
- **Buscar produto:** Permite consultar um produto pelo seu código.
- **Salvar estoque em CSV:** Exporta todos os produtos cadastrados para um arquivo CSV.

## Como usar
1. Execute o arquivo `estoque.py` com Python 3:
   ```bash
   python estoque.py
   ```
2. Utilize o menu interativo para gerenciar o estoque conforme as opções apresentadas.
3. Para salvar o estoque em um arquivo CSV, escolha a opção correspondente no menu e informe o nome do arquivo desejado (exemplo: `estoque.csv`).

## Estrutura do Código
- **Classe Produto:** Representa cada produto do estoque, com código, nome e quantidade.
- **Classe Estoque:** Gerencia todos os produtos, permitindo adicionar, remover, listar, buscar e salvar em CSV.
- **Função menu:** Exibe o menu e gerencia as operações do usuário.

## Requisitos
- Python 3.x

## Observações
- O programa não carrega dados de arquivos CSV automaticamente ao iniciar. Apenas salva o estoque atual em um arquivo CSV quando solicitado.
- O código é comentado para facilitar o entendimento e a manutenção.

---
Desenvolvido para fins didáticos.
