from Sandwich import Sandwichote

class sanwichitoVegano(Sandwichote):
    def __init__(self, pan, precio, lechuga):
        super().__init__(pan, precio )
        self.lechuga = lechuga
    
    def descripcion(self):
        return f"Sandiwch vegetariano con {self.pan} y la lechuga {self.lechuga}"