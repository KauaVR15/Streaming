from Obra import Obra


class Documentario(Obra):

    def __init__(self, titulo, ano_lancamentom, duracao, class_indicativa,
                tema, narrador):
    
        super().__init__(titulo, ano_lancamentom, duracao, class_indicativa)
        self.__tema = tema
        self.__narrador = narrador

    def get_tema(self):
        return self.__tema

    def set_tema(self, tema):
        self.__tema = tema


    def get_narrador(self):
        return self.__narrador

    def set_narrador(self, narrador):
        self.__narrador = narrador

    def exibir_info(self):
        return f"""{super().exibir_info() }
|Tema: {self.__tema}
|Narrador: {self.__narrador}""" 
        