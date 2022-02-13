class Comodo:
    __largura: float
    __profundidade: float
    __altura: float

    def __init__(self,largura,profundidade):
        self.largura = largura ## apenas quem acessa estas propriedades são os setters e getters
        self.profundidade = profundidade
        self.__altura = 2.9

    @property ## indica que o método é uma propriedade de privada um atributo, no caso largura
    def largura(self):
        return self.__largura

    @property
    def profundidade(self):
        return self.__profundidade
    @property
    def altura(self):
        return self.__altura

    @largura.setter
    def largura(self,largura):
        try:
            self.__largura = float(largura)     ##caso for verificado que não é float
        except Exception:
            print('O valor da largura informado é inválido') ## msg de erro
            exit()

    @profundidade.setter
    def profundidade(self,profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
            print('O valor da profundidade informado é inválido.')
            exit()

    ## o tipo Except permitirá a captura de qualquer tipo de erro.


