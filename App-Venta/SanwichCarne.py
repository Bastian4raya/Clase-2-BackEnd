from Sandwich import Sandwichote

class sandwichitoCarne(Sandwichote):
    def __init__(self, pan, precio, queso):
        super().__init__(pan, precio)
        self.queso = queso
    
    def descripcion(self):
       return f"Soy un sandwich de carne con {self.pan} y tengo tambien {self.queso}"
    
