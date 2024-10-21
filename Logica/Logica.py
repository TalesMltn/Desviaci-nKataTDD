class Calcular(Exception):
    """Excepción personalizada para manejar casos donde no se puede calcular."""
    pass


class Conjunto:
    def __init__(self, conjunto):
        # Validación al inicializar para asegurar que los elementos sean numéricos
        if not all(isinstance(i, (int, float)) for i in conjunto):
            raise TypeError("Todos los elementos del conjunto deben ser numéricos")
        self.__conjunto = conjunto

    def promedio(self):
        """Calcula el promedio del conjunto."""
        if len(self.__conjunto) == 0:
            raise Calcular("No se puede calcular el promedio de un conjunto vacío")

        return sum(self.__conjunto) / len(self.__conjunto)