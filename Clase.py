class TarifaEstacionamiento:
    __horas = 0.0
    __minutos = 0.0
    __total = 0.0
    __tarifa_por_hora = 50.0

    def __init__(self, tarifa_por_hora=50.0):
        self.__tarifa_por_hora = tarifa_por_hora

    def calcularTarifaHora(self, horas, minutos):
        """
        Calcula el tiempo total en minutos.

        Precondiciones:
            - horas >= 0
            - minutos >= 0 y < 60
        """
        self.__horas = horas
        self.__minutos = minutos
        self.__total = (self.__horas * 60) + self.__minutos
        return self.__total

    def calcularCosto(self):
        """
        Calcula el costo total con base en la tarifa por hora.

        Postcondiciones:
            - Devuelve el costo total, considerando que los minutos adicionales
              se redondean a la tarifa de una hora completa.
        """
        horas_completas = self.__total // 60
        minutos_restantes = self.__total % 60
        if minutos_restantes > 0:
            horas_completas += 1
        return horas_completas * self.__tarifa_por_hora
