from Figuras import figura 
class circulo(figura):
    def __init__(self, color, diametro):
        super().__init__(color)
        self.diametro = diametro

    def __str__(self):
        return "Se ha creado un círculo de color {}".format(self.color)

