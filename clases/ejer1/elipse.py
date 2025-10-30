from Figuras import figura
class elipse(figura):
    def __init__(self, color, eje_mayor, eje_menor):
        super().__init__(color)
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
    def __str__(self):
        return ("Se ha creado una elipse de color {}".format(self.color))