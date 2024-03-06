from tkinter import *

root = Tk()

root.title("Calculadora")

myFrame = Frame(root)

myFrame.pack()

operacion = ""

resultado = 0

resetPantalla = False

# ---------------- INICIO PANTALLA --------------------------------

numeroPantalla = StringVar()

pantalla = Entry(myFrame, textvariable=numeroPantalla)

pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)

pantalla.config(background="black", fg="#03f943", justify="right")


# ------------------ PULSACIONES TECLADO --------------------------


def numeroPulsado(num):

    global operacion, resetPantalla

    if resetPantalla != False:

        numeroPantalla.set(num)

        resetPantalla = False

    else:

        numeroPantalla.set(numeroPantalla.get() + num)


# ----------------------- SUMA ------------------------


def suma(num):

    global operacion, resultado, resetPantalla

    resultado += int(num)

    operacion = "suma"

    resetPantalla = True

    numeroPantalla.set(resultado)


# ----------------------- RESTA ------------------------

num1 = 0

cont_resta = 0


def resta(num):

    global operacion, resultado, cont_resta, num1, resetPantalla

    if cont_resta == 0:

        num1 = int(num)

        resultado = num1

    else:

        if cont_resta == 1:

            resultado = num1 - int(num)

        else:

            resultado = int(resultado) - int(num)

        numeroPantalla.set(resultado)

        resultado = numeroPantalla.get()

    cont_resta += 1

    operacion = "resta"

    numeroPantalla.set(resultado)

    resetPantalla = True


# ----------------------- MULTIPLICACION ------------------------

cont_mult = 0


def multiplicacion(num):

    global cont_mult, resultado, resetPantalla, operacion, num1

    if cont_mult == 0:

        num1 = float(num)

        resultado = num1

    else:

        if cont_mult == 1:

            resultado = num1 * float(num)

        else:

            resultado = float(resultado) * float(num)

        numeroPantalla.set(resultado)

        resultado = numeroPantalla.get()

    cont_mult += 1

    operacion = "multiplicacion"

    resetPantalla = True


# ----------------------- DIVISION ------------------------

cont_divi = 0


def division(num):

    global cont_divi, operacion, resetPantalla, num1, resultado

    if cont_divi == 0:

        num1 = float(num)

        resultado = num1

    else:

        if cont_divi == 1:

            resultado = num1 / float(num)

        else:

            resultado = float(resultado) / float(num)

        numeroPantalla.set(resultado)

        resultado = numeroPantalla.get()

    cont_divi += 1

    operacion = "division"

    resetPantalla = True


def elResultado():

    global resultado, cont_divi, cont_mult, cont_resta, operacion

    if operacion=="suma":

        numeroPantalla.set(resultado+int(numeroPantalla.get()))

        resultado = 0

    elif operacion=="resta":

        numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))

        resultado=0

        cont_resta=0

    elif operacion=="multiplicacion":

        numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))

        resultado=0

        cont_mult=0

    elif operacion=="division":

        numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))

        resultado=0

        cont_divi=0


# ----------------------------------------- FILA UNO ---------------------------------------------

boton7 = Button(myFrame, text="7", width=3, command=lambda: numeroPulsado("7")).grid(
    row=2, column=1
)
boton8 = Button(myFrame, text="8", width=3, command=lambda: numeroPulsado("8")).grid(
    row=2, column=2
)
boton9 = Button(myFrame, text="9", width=3, command=lambda: numeroPulsado("9")).grid(
    row=2, column=3
)
botonMul = Button(myFrame, text="X", width=3, command=lambda: multiplicacion(numeroPantalla.get())).grid(
    row=2, column=4
)

# ----------------------------------------- FILA DOS ----------------------------------------------

boton4 = Button(myFrame, text="4", width=3, command=lambda: numeroPulsado("4")).grid(
    row=3, column=1
)
boton5 = Button(myFrame, text="5", width=3, command=lambda: numeroPulsado("5")).grid(
    row=3, column=2
)
boton6 = Button(myFrame, text="6", width=3, command=lambda: numeroPulsado("6")).grid(
    row=3, column=3
)
botonDiv = Button(
    myFrame, text="/", width=3, command=lambda:division(numeroPantalla.get())).grid( 
    row=3, column=4
)

# ----------------------------------------- FILA TRES ---------------------------------------------

boton1 = Button(myFrame, text="1", width=3, command=lambda: numeroPulsado("1")).grid(
    row=4, column=1
)
boton2 = Button(myFrame, text="2", width=3, command=lambda: numeroPulsado("2")).grid(
    row=4, column=2
)
boton3 = Button(myFrame, text="3", width=3, command=lambda: numeroPulsado("3")).grid(
    row=4, column=3
)
botonSum = Button(
    myFrame, text="+", width=3, command=lambda: suma(numeroPantalla.get())
).grid(row=4, column=4)

# ----------------------------------------- FILA CUATRO -------------------------------------------

botonCom = Button(myFrame, text=",", width=3, command=lambda: numeroPulsado(",")).grid(
    row=5, column=1
)
boton0 = Button(myFrame, text="0", width=3, command=lambda: numeroPulsado("0")).grid(
    row=5, column=2
)

botonIgu = Button(myFrame, text="=", width=3, command=lambda: elResultado()).grid(
    row=5, column=3
)

botonRes = Button(myFrame, text= "-", width=3, command=lambda: resta(numeroPantalla.get())).grid(
    row=5, column=4
)

root.mainloop()
