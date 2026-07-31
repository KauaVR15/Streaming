from Obra import Obra


class Filme(Obra):

    def __init__(self, titulo, ano_lancamentom, duracao, class_indicativa,
                diretor, genero, bilheteria):

        super().__init__(titulo, ano_lancamentom, duracao, class_indicativa)
        self.__diretor = diretor
        self.__genero = genero
        self.__bilheteria = bilheteria


    def get_diretor(self):
        return self.__diretor

    def set_diretor(self, diretor):
        self.__diretor = diretor


    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero


    def get_bilheteria(self):
        return self.__bilheteria

    def set_bilheteria(self, bilheteria):
        self.__bilheteria = bilheteria


    def exibir_info(self):
        return f"""{super().exibir_info() } 
|Diretor: {self.__diretor} 
|Genero: {self.__genero} 
|Bilheteria: {self.__bilheteria}"""

    