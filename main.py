from ClaseHelado import Helado
from ClaseSabor import Sabor
from claseManejadorHelados import ManejadorHelados
from claseManejadorSabores import ManejadorSabores
if __name__=="__main__":
    #unSabor=Sabor(123,"leche y cacao","chocolate")
    #otroSabor=Sabor(234,"leche y almendra","almendra")
    #unHelado=Helado(150,500,unSabor)
    #unHelado.addSabor(otroSabor)
    #print(unHelado)
    sabores=ManejadorSabores()
    sabores.inicializar()
    print(sabores)
    heladosVandidos=ManejadorHelados()
    heladosVandidos.venta(sabores)
    heladosVandidos.venta(sabores)
    heladosVandidos.venta(sabores)
    heladosVandidos.venta(sabores)
    heladosVandidos.venta(sabores)
    heladosVandidos.mostrarHeladosVendidos()