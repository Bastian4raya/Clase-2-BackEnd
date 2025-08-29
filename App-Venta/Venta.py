from Sandwich import Sandwichote

class Venta:
    def __init__(self):
        self.pedidos = []

    def agregar_sandwich(self, Sandwichote):
        print(f"Agregado {Sandwichote.descripcion()}, Precio $: {Sandwichote.get_precio()}")
        self.pedidos.append(Sandwichote)

    def mostrar_venta(self):
        print(" ---Resumen de la venta --- ")
        total = 0
        for i in self.pedidos:
            print(f"{i.descripcion} | {i.get_precio}")
            total += i.get_precio()
        print(f"Total a pagar : {i.total}")
