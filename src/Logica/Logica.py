import math


class NoSePuedeCalcular(Exception):
    pass


class Conjunto:
    def __init__(self, elementos):
        self.elementos = elementos  # Store elements in an instance variable

    def desviacion_estandar(self):
        if len(self.elementos) == 0:
            raise NoSePuedeCalcular("No se puede calcular la desviación estándar de un conjunto vacío.")

        promedio = sum(self.elementos) / len(self.elementos)
        varianza = sum((x - promedio) ** 2 for x in self.elementos) / len(self.elementos)  # Population variance
        return varianza ** 0.5  # Return the standard deviation

