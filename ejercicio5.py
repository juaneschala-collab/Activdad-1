import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def calc_area(self):
        return math.pi * (self.radio ** 2)
        
    def calc_circunferencia(self):
        return 2 * math.pi * self.radio

mi_circulo = Circulo(10) 
print(f"El área del círculo es: {mi_circulo.calc_area():.2f}")
print(f"La circunferencia es: {mi_circulo.calc_circunferencia():.2f}")