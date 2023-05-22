from ClaseSabor import Sabor
class Helado:
    __gramos=0
    __precio=0
    __sabores=[]
    
    def addSabor(self,sabor):
        self.__sabores.append(sabor)
        
    def __init__(self, gramos, precio, sabor=None):
        self.__gramos=gramos
        self.__precio=precio
        self.addSabor(sabor)
        
        
        
    def __str__(self):
        s=("Gramos {}, precio {}\n".format(self.__gramos,self.__precio))
        for sabore in self.__sabores:
            s+=str(sabore)+"\n"
            
        return s
    
    
    

        
        
        
    
        