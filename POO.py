
class Clima:
    def __init__(self):
        self.temperaturas = []


class ClimaSemanal(Clima):

    def ingresar_temperaturas(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        for dia in dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)


# Programa principal
print("PROMEDIO SEMANAL DEL CLIMA - PROGRAMACIÓN ORIENTADA A OBJETOS")

clima = ClimaSemanal()
clima.ingresar_temperaturas()
promedio = clima.calcular_promedio()

print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")
