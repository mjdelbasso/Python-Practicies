class Persona(): 
    
    def __init__(self, nombre, apellido, edad):
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        
    
    def __str__(self):
        return "Datos de la persona: " + "\nNombre: " + self.__nombre \
            +"\nApellido: " + self.__apellido + "\nEdad: " + str(self.__edad)
    
    # COSAS BASICAS QUE HACEN LAS PERSONAS
    
    def habla(self):
        return "Estoy hablando."
    
    def piensa(self):
        return "Estoy pensando."
    
    def camina(self):
        return "Estoy caminando." 
    
    def come(self):
        return "Estoy comiendo."
    
    def duerme(self):
        return "Estoy durmiendo."
    
    # RECUPERANDO DATOS PERSONALES

    def getDatosPersonales(self):
        return "Nombre: " + self.__nombre + " Apellido: " +self.__apellido + \
            " Edad: " + str(self.__edad)
    
# CLASE ESTUDIANTE

class Estudiante(Persona):
    
    def __init__(self, nombre, apellido, edad, escuela):
        Persona.__init__(self,nombre, apellido, edad)
        self.__escuela = escuela  
    
    
    def getDatosPersonales(self):
        
        return super().getDatosPersonales() + " Escuela: " + self.__escuela
    
    def estudia(self):
        return "Estoy estudiando."



# CLASE TRABAJADOR


class Trabajador(Persona):
    
    def __init__(self,nombre,apellido,edad,empresa):
        Persona.__init__(self,nombre,apellido,edad)
        self.__empresa = empresa
        
    def getDatosPersonales(self):
        
        return super().getDatosPersonales() + " Empresa: " + self.__empresa
    
    def trabaja(self):
        return "Estoy trabajando."



class Director(Trabajador, Estudiante):
    
    def __init__(self, nombre, apellido, edad, empresa, escuela, departamento):
        
        Trabajador.__init__(self,nombre,apellido,edad,empresa)
        
        Estudiante.__init__(self,nombre,apellido,edad,escuela)
        
        self.__departamento = departamento
        
        
    def getDatosPersonales(self):
        
        return super().getDatosPersonales() + " Departamento: " + self.__departamento
    
    def dirige(self):
        return "Estoy dirigiendo"
        
    





persona1 = Director("Marcos","Del Basso",32,"BlackStar","Pildoras Online","Informatica")

estudiante = Estudiante("Joan","Cruceira", 33, "IES Siglo XXI")

print(persona1.getDatosPersonales())

print(estudiante.getDatosPersonales())

print(persona1)

print(estudiante)

