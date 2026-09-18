class familia:
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan
        
    def Calcular_edades(self):
        edad_alberto = (2/3) * self.edad_juan
        edad_ana = (4/3) * self.edad_juan
        edad_mama = self.edad_juan + edad_alberto + edad_ana
        
        return edad_alberto, edad_ana, edad_mama


mi_familia = familia(15) 
alberto, ana, mama = mi_familia.Calcular_edades()

print(f"Edad de Juan: {mi_familia.edad_juan}")
print(f"Edad de Alberto: {alberto}")
print(f"Edad de Ana: {ana}")
print(f"Edad de la mamá: {mama}")