from claseManejadorSabores import ManejadorSabores
from ClaseHelado import Helado
from ClaseSabor import Sabor
class ManejadorHelados:
    __lista=[]
    
    
    
    
    def __init__(self):
        self.__lista=[]
        
        
    def agregarHelado(self,helado):
        self.__lista.append(helado)
        
        
        
    def venta(self,sabores):
        gramos=input("ingrese gramos")
        precio=input("ingrese precio")
        cantidad=int(input("Ingrse la cantidad de sabores"))
        print("Mostrar sabores de helados")
        print(sabores)
        unHelado=Helado(gramos,precio)
        for i in range(cantidad):
            Id=input("ingrese id del sabor")
            sabor=sabores.getSabores()[int(Id)-1]
            unHelado.addSabor(sabor)
        self.agregarHelado(unHelado)
        
        
        
    def mostrarHeladosVendidos(self):
        for helado in self.__lista:
            print(helado)
    
            
            
        
        
        