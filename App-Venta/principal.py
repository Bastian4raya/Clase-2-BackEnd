from Sandwich import Sandwichote
from SandwichVegetariano import sanwichitoVegano
from SanwichCarne import sandwichitoCarne
from Venta import Venta

mi_sandich = Sandwichote("Marraqueta", 1200)
venta = Venta()
vegetariano = sanwichitoVegano ("Integral", 2000 , "Lechuga nueva")
carne = sandwichitoCarne("Hallulla", 3000 ,"Cheddar")

carne.set_precio(4500)

venta.agregar_sandwich(vegetariano)
venta.agregar_sandwich(carne)