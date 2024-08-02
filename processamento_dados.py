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
    def get_columns (self):
        return list(self.dados[-1].keys())
    
    # funcao para renomear colunas do arquivo csv
    def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
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