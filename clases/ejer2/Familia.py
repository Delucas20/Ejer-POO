from persona import persona

class familia(persona):
    def __init__(self, apellido, nombre, sexo, padre, madre, hijo, hija):
        super().__init__(apellido, sexo, nombre)
        self.padre = padre
        self.madre = madre
        self.hijo = hijo
        self.hija = hija

    def __str__(self):
        return f"Familia(padre={self.padre}, madre={self.madre}, hijo={self.hijo}, hija={self.hija})"
                    

