class persona:
    def __init__(self, apellido, nombre , sexo):
        self.apellido = apellido
        self.nombre = nombre
        self.sexo = sexo
    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.sexo})"
