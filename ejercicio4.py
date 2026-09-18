class Numero:
    def __init__(self, valor):
        self.valor = valor
        
    def calc_cuadrado(self):
        return self.valor ** 2
        
    def calc_cubo(self):
        return self.valor ** 3

mi_numero = Numero(5) 
print(f"El cuadrado de {mi_numero.valor} es {mi_numero.calc_cuadrado()}")
print(f"El cubo de {mi_numero.valor} es {mi_numero.calc_cubo()}")