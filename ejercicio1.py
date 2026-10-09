class Persona:
    def __init__(self, nombre: str, apellidos: str, numero_documento: str, anio_nacimiento: int):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento = numero_documento
        self.anio_nacimiento = anio_nacimiento

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Número de documento de identidad: {self.numero_documento}")
        print(f"Año de nacimiento: {self.anio_nacimiento}\n")

if __name__ == "__main__":
    p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    p2 = Persona("Luis", "León", "1053223344", 2001)
    p1.imprimir()
    p2.imprimir()