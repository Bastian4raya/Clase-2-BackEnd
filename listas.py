
# miLista = ["Eric", "Profesor", 39 , 1.80, "curso de prog" ]
# print(miLista[2])
# numeros = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# print("Lista 1 : ", numeros)
# numeros.append(11)
# numeros.remove(5)
# print("Lista 2 : ", numeros)

# numero1=  float(input ("Ingrese el primer numero: "))
# numero2= float(input ("Ingrese el segundo numero: "))
   
# sumnum = numero1 + numero2
# print("La suma de los numeros es ", sumnum)

# restarnum = numero1 - numero2 
# print("La resta de los numeros es : ", restarnum)

# multiplicarnum = numero1 * numero2 
# print("La multiplicacion es : ", multiplicarnum)

#Diferentes de crear una lista 

# lista_vacia = []
# numeros = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# lista_string = ["manzana", "uva", "pera"]
# lista_mixta = [1, "hola", 3.14]
   
# for i in range(5):
#     print(i)

#Append para agregar
# frutas = ["manzana", "pera", "cereza"]
# frutas.append("naranjajaja")
# print ("Despues de append paso la fruta :", frutas)

# #insert para insertar en lugar especifico
# frutas.insert(1, "uva")
# print("Se insertaron las uvas", frutas)

# #remove

# frutas.remove("manzana")
# print("Se elimino la manzana:", frutas)

# numeros = [64 , 35 , 14 , 61, 88]
# numeros.sort()
# print(numeros)

# lista_a = [1 ,2 ,3 ,4 ,5 , 6]
# lista_b = [4, 5 , 6 ,7 ,8 ,9]

# #Para buscar elementos que coinciden.
# coincidencias= []

# for i in range(len(lista_a)):
#     for j in range(len(lista_b)):
#         if lista_a[i] == lista_b[j]:
#             coincidencias.append(lista_a[i])

# print ("Elementos comunes ", coincidencias)           
     
# conjunto1 = set(lista_a)
# conjunto2 = set(lista_b)
# lista_con_duplicados = list(conjunto1 & conjunto2)
# print(lista_con_duplicados)

productos = ["laptot", "mouse", "teclado", "monitor"]
precios = [1200, 250 , 80 , 300]
existencias = [15, 50 , 30 , 20]


#Se debe listar todos los productos por orden y finalmente 
#mostrar el total del inventario multiplicar precio y existencias 
print ("Inventario de productos")
print ("-"* 40)

for i in range(len(productos)):
    valor_total = precios[i]* existencias[i]
    print(f"Producto: {productos[i]}")
    print(f"Precio:  {precios[i]}")
    print(f"Existencias: {existencias[i]}")
    print(f"Valor total {valor_total}")
    print("-"*40) 


# Calcular el valor total de inventario

# lista_a = sum(precios)
# lista_b = sum(existencias)
# total_inventario = lista_a + lista_b
# print(total_inventario)


valor_inventario = 0
for i in range(len(productos)):
    valor_inventario += precios[i] * existencias[i]
print(f"El precio total es : {valor_inventario}")



# atributo = caracteristicas

