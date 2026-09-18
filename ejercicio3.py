class Trabajador:
    def __init__(self, horas_trab, pago_hora):
        self.horas_trab = horas_trab
        self.pago_hora = pago_hora
        self.retencion_fuente = 0.125 
        
    def calc_sal_bruto(self):
        return self.horas_trab * self.pago_hora
        
    def calc_retencion(self):
        salario_bruto = self.calc_sal_bruto()
        return salario_bruto * self.retencion_fuente
        
    def calc_sal_neto(self):
        salario_bruto = self.calc_sal_bruto()
        retencion = self.calc_retencion()
        return salario_bruto - retencion

empleado_actual = Trabajador(48, 5000)

print(f"Salario Bruto: ${empleado_actual.calc_sal_bruto()}")
print(f"Retención en la fuente: ${empleado_actual.calc_retencion()}")
print(f"Salario Neto: ${empleado_actual.calc_sal_neto()}")