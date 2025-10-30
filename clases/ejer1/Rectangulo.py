from Figuras import figura
class rectangulo(figura):
    def __init__(self, color, longitud, anchura):
        super().__init__(color)
        self.longitud = longitud
        self.anchura = anchura
    def __str__(self):
        return "Se ha creado un rectangulo de color {}".format(self.color)
    