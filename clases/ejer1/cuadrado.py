from Figuras import figura
class cuadrado(figura):
    def __init__(self, color,  longitud):
        super().__init__(color)
        self.longitud = longitud
    def __str__(self):
        return "Se ha creado un cuadrado de color {}".format(self.color)
    
    