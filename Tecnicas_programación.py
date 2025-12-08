

# --------------------------------------------
# 1. ABSTRACCIÓN (Aplicada en la clase Persona)
# --------------------------------------------


class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):

        # 2. ENCAPSULAMIENTO (Protección de los datos)

        self._marca = marca
        self._modelo = modelo
        self._velocidad_maxima =  velocidad_maxima
        self._velocidad_actual = 0


    def mostrar_info(self):
        return f"{self._marca} {self._modelo} ({self._velocidad_maxima})"

    # -------- MÉTODOS DE ENCAPSULAMIENTO --------
    def get_velocidad_maxima(self):
        return self._velocidad_maxima


    def get_velocidad_actual(self):
        return self._velocidad_actual

    def acelerar(self, incremento):
        if incremento < 0:
            print("El incremento debe ser positivo.")
            return
        nueva_velocidad = self._velocidad_actual + incremento
        if nueva_velocidad > self._velocidad_maxima:
            self.__velocidad_actual = self._velocidad_maxima
            print(f"¡Límite de velocidad alcanzado! ({self._velocidad_maxima} km/h)")
        else:
            self.__velocidad_actual = nueva_velocidad





# 3. HERENCIA (Estudiante y Docente heredan de Persona)

    class Vehiculo:
        def __init__(self, marca, modelo, velocidad_maxima):
            self.marca = marca
            self.modelo = modelo
            self.__velocidad_maxima = velocidad_maxima
            self.__velocidad_actual = 0

        # Métodos protegidos o públicos para acceso controlado
        def get_velocidad_maxima(self):
            return self.__velocidad_maxima

        def get_velocidad_actual(self):
            return self.__velocidad_actual

        def _set_velocidad_actual(self, velocidad):

            if 0 <= velocidad <= self.__velocidad_maxima:
                self.__velocidad_actual = velocidad
            else:
                raise ValueError("Velocidad fuera de rango permitido.")

        def acelerar(self, incremento):
            nueva_velocidad = self.__velocidad_actual + incremento
            self._set_velocidad_actual(min(nueva_velocidad, self.__velocidad_maxima))

        def frenar(self, decremento):
            nueva_velocidad = self.__velocidad_actual - decremento
            self._set_velocidad_actual(max(nueva_velocidad, 0))

        def mostrar_estado(self):
            print(f"{self.marca} {self.modelo} - Velocidad actual: {self.__velocidad_actual} km/h")

    # 4. POLIMORFISMO:


     vehiculos = [
         Auto("Toyota", "Corolla", 180, 4),
         Moto("Yamaha", "R1", 300, False),
         Moto("Honda", "Gold Wing", 200, True)
     ]


    for v in vehiculos:
        v.acelerar(40)


    for v in vehiculos:
        v.avanzar()





