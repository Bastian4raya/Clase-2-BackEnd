class Sandwichote:
    def __init__(self, pan , precio ):
        self.pan = pan
        self.__precio = precio
    # def mostrarInformacion(self):
    #    return f"Soy un sanguichito de : {self.pan} con {self.tomate}"
    #Getter
    def get_precio(self):
        return self.__precio
    #Setter
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor 0")
    #metodo que sera sobreescrito con Polimorfismo
    def descripcion(self):
        return f"sandwich con {self.pan}"