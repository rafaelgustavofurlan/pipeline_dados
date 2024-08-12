# importando bibliotecas
# import json
# import csv
from processamento_dados import Dados

# leitura json
# def leitura_json(path_json):
#     dados_json = []
#     with open(path_json, 'r') as file:
#         dados_json = json.load(file)
#     return dados_json

# leitura csv
# def leitura_csv(path_csv):
#     dados_csv = []
#     with open(path_csv, 'r') as file:
#         spamreader = csv.DictReader(file, delimiter=',')
#         for row in spamreader:
#             dados_csv.append(row)
#     return dados_csv

# criando a funcao que irá juntar as duas demais funcoes
# def leitura_dados(path, tipo_arquivo):
#     dados = []
# 
#     if tipo_arquivo == 'csv':
#         dados = leitura_csv(path)
#     elif tipo_arquivo == 'json':
#         dados = leitura_json(path)
#     
#     return dados

# def get_columns (dados):
#     return list(dados[-1].keys())

# keymapping é o de/para das colunas

# funcao para renomear colunas do arquivo csv
# def rename_columns(dados, key_mapping):
#     new_dados_csv = []
#  
#     for old_dict in dados:
#         dict_temp = {}
#         for old_key, value in old_dict.items():
#             dict_temp[key_mapping[old_key]] = value
#         new_dados_csv.append(dict_temp)
#     
#     return new_dados_csv

# funcao para calculo do tamanho dos arquivos - quantidade de registros
# def size_data(dados):
#     return len(dados)

# funcao para unir os dois arquivos
# def join (dadosA, dadosB):
#     combined_list = []
#     combined_list.extend(dadosA)
#     combined_list.extend(dadosB)
#     return combined_list

# transformar dados em tabela
# def transformando_dados_tabela(dados, nomes_colunas):
#     dados_combinados_tabela = [nomes_colunas]
# 
#     for row in dados:
#         linha = [] 
#         for coluna in nomes_colunas:
#            linha.append(row.get(coluna, 'Indisponível'))
#         dados_combinados_tabela.append(linha)
#     
#     return dados_combinados_tabela

# funcao para salvar no arquivo csv
# def salvando_dados(dados, path):
#     with open(path, 'w') as file:
#         writer = csv.writer(file)
#         writer.writerows(dados)

# definindo diretorio dos arquivos
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'

# Extract
dados_empresaA = Dados(path_json, 'json')
print(f'O nome das colunas da empresa A são: {dados_empresaA.nome_colunas}.')
print(f'A quantidade de registros da empresa A é de {dados_empresaA.qtd_linhas} registros.')

dados_empresaB = Dados(path_csv, 'csv')
print(f'O nome das colunas da empresa B são: {dados_empresaB.nome_colunas}.')
print(f'A quantidade de registros da empresa B é de {dados_empresaB.qtd_linhas} registros.')

# renomeando as colunas de B
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)

# unindo os dados
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao.qtd_linhas)
print(dados_fusao.nome_colunas)

# load
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)

# iniciando a leitura
# dados_json = leitura_dados(path_json,'json')
# nome_colunas_json = get_columns(dados_json)
# tamanho_dados_json = size_data(dados_json)
# print(f'nomes colunas dados json: {nome_colunas_json}')
# print(f'total de registros json: {tamanho_dados_json}')

# dados_csv = leitura_dados(path_csv, 'csv')
# nome_colunas_csv = get_columns(dados_csv)
# dados_csv = rename_columns(dados_csv, key_mapping)
# tamanho_dados_csv = size_data(dados_csv)
# print(f'nome coluna dados csv: {nome_colunas_csv}')
# print(f'total de registros csv: {tamanho_dados_csv}')

# unindo os dados
# dados_fusao = join(dados_json, dados_csv)
# nomes_colunas_fusao = get_columns(dados_fusao)
# print(f'nome das colunas do novo arquivo: {nomes_colunas_fusao}')
# tamanho_dados_fusao = size_data(dados_fusao)
# print(f'total de colunas no arquivo: {tamanho_dados_fusao}')

# salvando os dados
# dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nomes_colunas_fusao)
# salvando_dados(dados_fusao_tabela, path_dados_combinados)
# print(path_dados_combinados