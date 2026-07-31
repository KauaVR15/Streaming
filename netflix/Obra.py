class Obra:

    def __init__(self, titulo, ano_lancamento, duracao, class_indicativa):

        self.__titulo = titulo
        self.__ano_lancamento = ano_lancamento
        self.__duracao = duracao
        self.__class_indicativa = class_indicativa


    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo


    def get_ano_lancamento(self):
        return self.__ano_lancamento

    def set_ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento


    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
        self.__duracao = duracao


    def get_class_indicativa(self):
        return self.__class_indicativa

    def set_class_indicativa(self, class_indicativa):
        self.__class_indicativa = class_indicativa    


    def exibir_info(self):
        return f"""|Titulo: {self.__titulo} 
|Ano de Lançamento: {self.__ano_lancamento} 
|Duração: {self.__duracao}
|Classificação Indicativa: {self.__class_indicativa}"""