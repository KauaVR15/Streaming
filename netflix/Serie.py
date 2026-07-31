from Obra import Obra


class Serie(Obra):

    def __init__(self, titulo, ano_lancamentom, duracao, class_indicativa,
                qtde_temp, qtde_eps):
    
        super().__init__(titulo, ano_lancamentom, duracao, class_indicativa)
        self.__qtde_temp = qtde_temp
        self.__qtde_eps = qtde_eps
        
    
    def get_qted_temp(self):
        return self.__qted_temp

    def set_qted_temp(self, qted_temp):
        self.__qted_temp = qted_temp


    def get_qted_eps(self):
        return self.__qted_eps

    def set_qted_eps(self, qted_eps):
        self.__qted_eps = qted_eps


    def exibir_info(self):
        return f"""{super().exibir_info() } 
|Quantidade de temporadas: {self.__qtde_temp} 
|Quantidade de episodios: {self.__qtde_eps}"""

