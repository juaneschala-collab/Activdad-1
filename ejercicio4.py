import math

class Circulo:
    def __init__(self, radio: int):
        self.radio = radio
    def calcular_area(self) -> float:
        return math.pi * math.pow(self.radio, 2)
    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura
    def calcular_area(self) -> float:
        return self.base * self.altura
    def calcular_perimetro(self) -> float:
        return (2 * self.base) + (2 * self.altura)

class Cuadrado:
    def __init__(self, lado: int):
        self.lado = lado
    def calcular_area(self) -> float:
        return self.lado * self.lado
    def calcular_perimetro(self) -> float:
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura
    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2
    def calcular_hipotenusa(self) -> float:
        return math.pow(self.base**2 + self.altura**2, 0.5)
    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()
    def determinar_tipo_triangulo(self):
        hipo = self.calcular_hipotenusa()
        if self.base == self.altura and self.base == hipo:
            print("Es un triángulo equilátero")
        elif self.base != self.altura and self.base != hipo and self.altura != hipo:
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")

if __name__ == "__main__":
    figura4 = TrianguloRectangulo(3, 5)
    print(f"El área del triángulo es = {figura4.calcular_area()}")
    print(f"El perímetro del triángulo es = {figura4.calcular_perimetro()}")
    figura4.determinar_tipo_triangulo()