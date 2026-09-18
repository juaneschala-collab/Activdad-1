class Prueba_escritorio:
    def __init__(self):
        self.suma = 0
        self.x = 0
        self.y = 0
        
    def ejecucion(self):
        self.suma = 0
        self.x = 20
        self.suma = self.suma + self.x
        self.y = 40
        self.x = self.x + (self.y ** 2) 
        self.suma = self.suma + (self.x / self.y)
        
        return self.suma

prueba = Prueba_escritorio()
resultado = prueba.ejecucion()
print(f"EL VALOR DE LA SUMA ES: {resultado}")