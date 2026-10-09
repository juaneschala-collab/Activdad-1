from enum import Enum

class TipoCom(Enum):
    GASOLINA = 1; BIOETANOL = 2; DIESEL = 3; BIODIESEL = 4; GAS_NATURAL = 5

class TipoA(Enum):
    CIUDAD = 1; SUBCOMPACTO = 2; COMPACTO = 3; FAMILIAR = 4; EJECUTIVO = 5; SUV = 6

class TipoColor(Enum):
    BLANCO = 1; NEGRO = 2; ROJO = 3; NARANJA = 4; AMARILLO = 5; VERDE = 6; AZUL = 7; VIOLETA = 8

class Automovil:
    def __init__(self, marca: str, modelo: int, motor: int, tipo_combustible: TipoCom, tipo_auto: TipoA, num_puertas: int, cant_asientos: int, vel_maxima: int, color: TipoColor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_auto = tipo_auto
        self.num_puertas = num_puertas
        self.cant_asientos = cant_asientos
        self.vel_maxima = vel_maxima
        self.color = color
        self.velocidad_actual = 0

    def acelerar(self, incremento: int):
        if self.velocidad_actual + incremento < self.vel_maxima:
            self.velocidad_actual += incremento
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")

    def desacelerar(self, decremento: int):
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia: int) -> float:
        return distancia / self.velocidad_actual if self.velocidad_actual > 0 else 0

    def imprimir(self):
        print(f"Marca = {self.marca}, Modelo = {self.modelo}, Motor = {self.motor}")
        print(f"Velocidad máxima = {self.vel_maxima}, Velocidad actual = {self.velocidad_actual}")

if __name__ == "__main__":
    auto1 = Automovil("Ford", 2018, 3, TipoCom.DIESEL, TipoA.EJECUTIVO, 5, 6, 250, TipoColor.NEGRO)
    auto1.imprimir()
    auto1.velocidad_actual = 100
    auto1.acelerar(20)
    auto1.desacelerar(50)
    auto1.frenar()
    auto1.desacelerar(20)