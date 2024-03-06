""" 
    
    Clase CuentaCorriente 
    
    Se trata de crear una clase que construya cuentas corrientes bancarias. Para ello deberás:

    Crear una clase con el nombre de CuentaCorriente con tres atributos que serán:
    
    El nº de la cuenta (un string numérico con el nº de cifras que quieras)
    El titular de la cuenta
    El saldo de la cuenta
    
    Crear un método getter que nos muestre la información de la cuenta:
    Debe mostrarnos el nº, el titular y el saldo. OK
    
    Crear un método que nos permita ingresar dinero en la cuenta
    Crear un método que nos permita retirar dinero de la cuenta
    Prueba el programa creando un objeto de tipo CuentaCorriente, 
    ingresa y retira dinero de la cuenta y finalmente muestra los datos de la cuenta.


"""

class CuentaCorriente():
        
    def __init__(self,nro_cuenta,titular_cuenta,saldo_cuenta):
        self.__nro_cuenta=nro_cuenta
        self.__titular_cuenta=titular_cuenta
        self.__saldo_cuenta=saldo_cuenta
        
    
    def getInformacion(self):
        return "N° Cuenta: " + str(self.__nro_cuenta) + " Titular: " + self.__titular_cuenta + \
            " Saldo: " + str(self.__saldo_cuenta) +"€."
            
    
    def setSaldo(self, monto):
        self.__saldo_cuenta += monto
        
    

    def transferir(self,cta_transf, monto):
        
        if self.__saldo_cuenta > 0:
            self.__saldo_cuenta -= monto
            cta_transf.__saldo_cuenta += monto
            return "Estimado/a "+ self.__titular_cuenta +", su transferencia de " + str(monto) + "€, con destino a la cuenta N° "+str(cta_transf.__nro_cuenta)+ \
                ", perteneciente a "+ str(cta_transf.__titular_cuenta)+ " ha sido realizada."
        return "Saldo insuficiente para realizar la transacción."
    
    def retirar(self,monto):
        
        if self.__saldo_cuenta >= monto:
            self.__saldo_cuenta -= monto
            return "Extraccion realizada. Su saldo actual es de: " + str(self.__saldo_cuenta) + "€."
        
        return "El monto ingresado " "("+ str(monto)+"€), " + "supera a su saldo actual. Su saldo es de " + str(self.__saldo_cuenta) + "€."
            
    

cta1=CuentaCorriente(17814,"Marcos Del Basso", 5000)

cta2=CuentaCorriente(12324,"Angela Santivañez",5000)

print("ESTADO INICIAL")
print("")

print(cta1.getInformacion())

print(cta2.getInformacion())

print("")
print("INICIO DE TRANSERENCIAS DE DINERO")
print("")

print(cta1.transferir(cta2,2000))

#print(cta2.transferir(cta1,3000))

print("")
print("CONSULTA INFORMACION")
print("")
print(cta1.getInformacion())

print(cta2.getInformacion())

print("")
print("INICIO DE RETIRO DE DINERO")
print("")

print(cta1.retirar(10000))

print(cta2.retirar(4000))

print("")
print("CONSULTA INFORMACION")
print("")
print(cta1.getInformacion())

print(cta2.getInformacion())


"""
Clase CuentaJoven:

Se trata de crear una clase con el nombre CuentaJoven 
que construya cuentas corrientes bancarias heredando 
de la clase CuentaCorriente creada en el ejercicio anterior. 


La clase CuentaJoven tendrá un atributo o propiedad propia 
con el nombre de bonus_promocion. El atributo bonus_promocion permitirá, 
de forma opcional, añadir un bonus que se añadirá al saldo de la cuenta. 
El establecimiento del bonus y el incremento del saldo se harán desde el constructor.

Además, la clase CuentaJoven contará con los siguientes métodos:

getBonus() encargado de devolver el importe del bonus
ingresar() que permitirá ingresar dinero a la cuenta. Este método se heredará de CuentaCorriente
retirar() que permitirá retirar dinero de la cuenta. Este método se heredará de CuentaCorriente
getDatos() que permitirá ver los datos de la Cuenta Joven: nº de cuenta, titular, saldo y bonus. 
Este método se heredará de CuentaCorriente
Prueba el programa creando un objeto de tipo CuentaJoven, 
ingresa y retira dinero de la cuenta y finalmente muestra los datos de la cuenta.
"""


class CuentaJoven(CuentaCorriente):
    
    def __init__(self,nro_cuenta,titular_cuenta,saldo_cuenta,bonus_promo):
        super().__init__(nro_cuenta,titular_cuenta,saldo_cuenta)
        
        self.__bonus_promo = bonus_promo
        
        self.setSaldo(self.__bonus_promo)
        

    
    def getBonus(self):
        return "El bonus para esta Cuenta Joven es de " + str(self.__bonus_promo) + "€."



cta3 = CuentaJoven(748, "Joan Cruceira", 3000,500)

print("")
print("CONSULTA INFORMACION")
print("")
print(cta3.getInformacion())
print("")
print(cta3.getBonus())
print("")

print("")
print("INICIO DE TRANSERENCIAS DE DINERO")
print("")

print(cta1.transferir(cta3,2000))
print("")

print(cta3.retirar(2000))
print("")
print(cta3.transferir(cta2,200))

print("")
print("CONSULTA INFORMACION")
print("")

print(cta1.getInformacion())

print(cta2.getInformacion())

print(cta3.getInformacion())    
    
    
