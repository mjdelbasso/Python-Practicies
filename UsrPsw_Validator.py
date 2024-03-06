"""
Se te propone crear un módulo capaz de evaluar usuarios y contraseñas. Para ello el módulo tendrá dos funciones, una para validar usuarios y otra para validar contraseñas. (Pista: necesitarás utilizar la función “isalnum()” entre otras para realizar este ejercicio. Esta función evalúa si una cadena de texto es alfanumérica devolviendo True en caso de serlo o False en caso contrario).

La función de validación de usuarios debe cumplir las siguientes restricciones:

No debe tener menos de 5 caracteres ni más de 15. 
Si se incumple esta restricción, la función devolverá el mensaje 
“El usuario no puede tener menos de 5 caracteres” o “El usuario no puede tener más de 15 caracteres”.
Solo puede contener letras y números. Si se incumple esta restricción la función devolverá el mensaje 
“El usuario solo puede contener letras y números”
Si el usuario es correcto, la función devolverá True.
La función de validación de contraseñas debe cumplir las siguientes restricciones:

Debe tener más de 10 caracteres. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña debe tener más de 10 caracteres”
Debe contener al menos un carácter que no sea ni letra ni número. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña debe contener un carácter que no sea ni letra ni número”
Debe contener al menos una letra mayúscula y una letra minúscula. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña no es segura”
No puede tener espacios en blanco. Si se incumple esta restricción, la función devolverá el mensaje “La contraseña no puede contener espacios en blanco”
Si el usuario es correcto, la función devolverá True.
Prueba la eficacia del módulo desde un archivo diferente.
"""
# ------------------FUNCION DE VALIDACION DE PASSWORD ----------------

def validaPassword (password):
    
    if password == "":
        print ("La contraseña no puede ser una cadena vacia.")
        return False
    elif len(password) > 10:
        
        if password.isalnum():
            print ("La contraseña debe contener al menos un caracter especial.")
            return False
        else:    
            print ("La contraseña ha sido validada correctamente.")
            return True    
    print ("La contraseña debe contener al menos diez caracteres.")
    return False
    

# ------------------FUNCION DE VALIDACION DE USUARIO ----------------

def validaUsuario (user):
    usr = user.lower()
    
    if len(usr) == 0:
        print ("El usuario no puede ser una cadena vacia.")
        return False
    
    if len(usr) >= 5:
        if len(usr) <= 15:
            if usr.isalpha():
                print ("Usuario validado con exito.")
                return True
            else:
                print ("El usuario no puede contener caracteres especiales.")
                return False
        print ("El usuario debe contener un maximo de 15 caracteres.")
        return False
    print("El usuario debe contener al menos 5 caracteres.")
    return False
    
        
        
    
print(validaUsuario(input("Ingresa un usuario a validar :")))

print(".......................................")

print(validaPassword(input("Ingresa una contraseña a validar: ")))

print(".......................................")




    
   
    

       
