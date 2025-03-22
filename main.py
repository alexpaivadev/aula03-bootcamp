import csv

caminho_arquivo = "Base Vendas Premier - Base.csv"

with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo, delimiter=',')
    arquivo = []
    for linha in leitor_csv:
        arquivo.append(linha)

print(arquivo)