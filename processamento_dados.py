import json
import csv

class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_data()

        # leitura json
    def leitura_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    # leitura csv
    def leitura_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    # criando a funcao que irá juntar as duas demais funcoes
    def leitura_dados(self):
        dados = []

        if self.tipo_dados == 'csv':
            dados = self.leitura_csv()
        elif self.tipo_dados == 'json':
            dados = self.leitura_json()
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memoria'
        
        return dados
    
    # criando a funcao para listar as colunas
    # def get_columns (self):
    #     return list(self.dados[-1].keys())
    
    def get_columns(self):
        colunas = set()
        for item in self.dados:
            colunas.update(item.keys())
        return list(colunas)

    # funcao para renomear colunas do arquivo csv
    # def rename_columns(self, key_mapping):
    #     new_dados = []
    # 
    #     for old_dict in self.dados:
    #         dict_temp = {}
    #         for old_key, value in old_dict.items():
    #             dict_temp[key_mapping[old_key]] = value
    #    new_dados.append(dict_temp)
    # 
    #    self.dados = new_dados
    #    self.nome_colunas = self.get_columns()

    def rename_columns(self, key_mapping):
        new_dados = []
 
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                new_key = key_mapping.get(old_key, old_key)
                dict_temp[new_key] = value
            new_dados.append(dict_temp)
        
        self.dados = new_dados
        self.nome_colunas = self.get_columns()

    # funcao para calculo do tamanho dos arquivos - quantidade de registros
    def size_data(self):
        return len(self.dados)
    
    # funcao para unir os dois arquivos
    @staticmethod
    def join (dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        
        return Dados(combined_list,'list')
    
    # transformar dados em tabela
    def transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = [] 
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponível'))
            dados_combinados_tabela.append(linha)
        
        return dados_combinados_tabela
    
    # funcao para salvar no arquivo csv
    def salvando_dados(self, path):
        
        dados_combinados_tabela = self.transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
