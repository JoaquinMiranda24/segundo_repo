class Cliente():
    def __init__(self , nombre , apellido , dni , mail):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail
        self.productos = []
        self.cantidad = []
       

    def __str__(self):
        return f"nombre: {self.nombre} mail: {self.mail}"

    
    def agregar_al_carrito(self , productos = []  , cantidad = [] ):
         self.productos = productos
         self.cantidad = cantidad
         suma_total = self.productos.precio * self.cantidad
         return f"{self.cantidad} productos: {self.productos} costo por unidad:{self.productos.precio} costo final: {suma_total}"
        
 
    def realizar_compra(self):
         return f"{self.nombre} , su compra es: {self.productos} costo:{self.productos.precio * self.cantidad }"

