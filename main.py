import primer_paquete

from primer_paquete.modulo1 import Cliente
from primer_paquete.modulo2 import Productos



cliente_uno = Cliente("Alejandro" , "Castro" , 37099876 , "calejandro@tienda.com")
cliente_dos = Cliente("Mario" , "Suarez" , 3345453 , "msuarez@tienda.com")
cliente_tres = Cliente("Lucia" , "Gomez" , 3938383 , "lgomez@tienda.com")
cliente_cuatro = Cliente("Miguel Ariel" , "Torres" , 40393839 , "matorres@tienda.com")

lista_clientes = [cliente_uno ,cliente_dos ,cliente_tres , cliente_cuatro]

producto_uno = Productos("Licuadora" , 1800)
producto_dos = Productos("Compu Gamer rx3000" , 130000)
producto_tres = Productos("Television smart" , 19000)
producto_cuatro = Productos("Celula samsumng" , 28000)


lista_productos = [producto_uno ,producto_dos , producto_tres , producto_cuatro,]

print("LISTADO PRODUCTOS DISPONIBLES!")

for i in lista_productos:
    
    print(i , i.precio)



print("_______________________AGREGAR AL CARRITO______________________________________")

#Probemos armar el carrito

print("Armemos su pedido:")

lista_productos_seleccionados = []

while True:
 
 seleccion = input("escoja un producto o presione S para salir:")

 if seleccion == "S":
   break
 else:
   for producto in lista_productos:
  
    if seleccion.lower() == producto.nombre_producto.lower():
     lista_productos_seleccionados.append(seleccion)
     #print(lista_productos_seleccionados)
     break
     
    else:
     print("no existe producto elegido")

print(lista_productos_seleccionados)

"""

print(Cliente.agregar_al_carrito(cliente_uno , producto_tres , 3))
print(Cliente.agregar_al_carrito(cliente_uno , producto_dos , 2))
print(Cliente.agregar_al_carrito(cliente_uno , producto_uno , 4))
print(Cliente.agregar_al_carrito(cliente_uno , producto_cuatro , 1))



print("______________________EMISION ORDEN DE COMPRA________________________________")

print(Cliente.realizar_compra(cliente_uno))
"""