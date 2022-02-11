class Calculadora:
    __area_paredes: float ## __UNDERSCORE X2 tem seu acesso limitado , só pode ser acessado por atributos e métodos dentro da sua propria classe.
    __area_teto: float ## são declarados como privados

    def calcular_area_paredes(self, comodo):
        self.__area_paredes = 2*(comodo.largura + comodo.profundidade)* comodo.altura
        return self.__area_paredes

    def calcular_area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade
        return self.__area_teto
    
    def litragem_necessaria(self):
        return (self.__area_paredes * self.__area_teto)/10