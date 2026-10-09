from enum import Enum

class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2

class CuentaBancaria:
    def __init__(self, nombres_titular: str, apellidos_titular: str, numero_cuenta: int, tipo_cuenta: TipoCuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0

    def imprimir(self):
        print(f"Titular = {self.nombres_titular} {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}, Tipo = {self.tipo_cuenta.name}, Saldo = {self.saldo}")

    def consultar_saldo(self):
        print(f"El saldo actual es = {self.saldo}")

    def consignar(self, valor: int) -> bool:
        if valor > 0:
            self.saldo += valor
            print(f"Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        print("El valor a consignar debe ser mayor que cero.")
        return False

    def retirar(self, valor: int) -> bool:
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Se ha retirado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        print("El valor a retirar debe ser menor que el saldo actual.")
        return False

if __name__ == "__main__":
    cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.AHORROS)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)