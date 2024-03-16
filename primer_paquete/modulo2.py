class Productos:
    def __init__(self , nombre_producto , precio):
      self.nombre_producto = nombre_producto
      self.precio = precio

    def __str__(self):
       
       return f'{self.nombre_producto}' 
    
    
