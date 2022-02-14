##O input interpreta como string, mesmo sendo numeros, usamos float() para converter
##:float = usamos para typar a variavel, no caso ela irá apresentar erro e não aceitar outro tipo de entrada, apenas float

from calculadora import Calculadora
from comodo import Comodo
## criamos o objeto da classe calculadora, instanciando
calc = Calculadora()

comodo = Comodo(
    input('Qual a largura do cômodo? '),
    input('Qual a profundidade do cômodo? ')
)
"""largura: float = float(input('Qual a largura do cômodo? '))
profundidade: float = float(input('Qual a profundidade do cômodo? '))
altura: float = 2.9 # pé direito padrão"""


##calc.area_paredes= (2*(largura + profundidade)* altura)
print('A area das paredes tem ',"{:.2f}".format(calc.calcular_area_paredes(comodo)),'m²')

##calc.area_teto = (largura * profundidade)
print('A área do teto tem ', "{:.2f}".format(calc.calcular_area_teto(comodo)),'m²')

##rend_tinta: float = (calc.area_paredes+calc.area_teto)/10
print('A quantidade de tinta necessária é de',"{:.2f}".format(calc.litragem_necessaria()), 'litros.')
