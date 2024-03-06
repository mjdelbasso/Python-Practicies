# ---------------------------------VEHICULO CLASE PADRE -------------------------------
class Vehiculo ():
    
    def __init__ (self,ruedas,ancho,alto):
        self.__ruedas = ruedas
        self.__ancho = ancho
        self.__alto = alto
    
    def arrancar(self):
        return ("Arranca.")
    
    def frenar(self):
        return ("Frena.")
       
# --------------------------------- COCHE HEREDA DE VEHICULO --------------------------------
class Coche(Vehiculo):
    
    def __init__(self,ruedas,ancho,alto,color,marchas,asientos,aire):
        Vehiculo.__init__(self,ruedas,ancho,alto)
        self.__color = color
        self.__marchas = marchas
        self.__asientos = asientos
        self.__aire = aire
    
    def acelerar(self):
        return ("Acelera.")
    
    def girar(self):
        return ("Gira.")
    
    def irMarchaAtras(self):
        retunr ("Marcha atras.")
       
# --------------------------------- FURGONETA HEREDA DE COCHE Y VEHICULO--------------------------------

class Furgoneta(Coche):
    
    def __init__(self,ruedas,ancho,alto,color,marchas,asientos,aire,carga):
        Vehiculo.__init__(self,ruedas,ancho,alto)
        Coche.__init__(self,ruedas,ancho,alto,color,marchas,asientos,aire)
        self.__carga = carga

    def cargar (self):
        return "Carga."

       
# --------------------------------- BICICLETA HEREDA DE VEHICULO --------------------------------

class Bicicleta(Vehiculo):
    
    def __init__(self, ruedas,ancho,alto,color):
        Vehiculo.__init__(self,ruedas,ancho,alto)
        self.__color = color
    
    def saltar(self):
        return "Salta."
    
# --------------------------------- MOTO HEREDA DE BICICLETA Y VEHICULO -------------------------
class Motocicleta (Bicicleta):
    
    def __init__ (self,ruedas,ancho,alto,color,cilindradas):
        Bicicleta.__init__(self,ruedas,ancho,alto,color)
        self.__cilindradas = cilindradas
        
    def derrapar(self):
        return "Derrapa."
    


miCoche = Coche(4,1.30,1,"Rojo",5,4,True)

miFurgoneta = Furgoneta(4,2,1.30,"Blanco",6,4,True,250)

miBici = Bicicleta(2,.5,.45,"Negro")

miMoto = Motocicleta(2,.45,1,"Verde",250)


miCoche.arrancar()