from math import *
from tkinter import *

from colorama import Fore

raiz = Tk()
raiz.title(Fore.RED + "CALCULADORA")
raiz.geometry("+500+100")
raiz.config(bd=35)  # cambio del grosor del borde
raiz.config(relief="groove")  # borde especial

# Variables importantes
resetear_pantalla = False  # Bool, para borrar todo lo que haya en pantalla
operacion = StringVar()  # String, para guardar la operacion aritmetica (suma, resta, division)
variable_pantalla_operaciones = StringVar()  # String, la operacion enviada a la pantalla principal
variable_pantalla_resultados = StringVar()  # Solamente para mostrar los resultados en la pantalla de resultados

operador = ""  # String, para guardar el simbolo de la operacion aritmetica
numero_1 = 0
numero_2 = 0
resultado = 0  # Float, el resultado numerico de las operaciones aritmeticas

alto_boton = 1
color_boton = "GRAY"

miFrame = Frame(raiz)
miFrame.pack()
miFrame.config(bg="PINK")  # cambio el fondo de alrededor de donde se escribe
miFrame.config(width="950", height="650")
# miFrame.pack(fill="both",expand="True")#expande en las dos direcciones both # se me queda a la derecha
miFrame.config(bd=35)  # cambio del grosor del borde
miFrame.config(relief="groove")  # borde especial
miFrame.config(cursor="pirate")

pantalla_resultados = Entry(miFrame,
                            textvariable=variable_pantalla_resultados)  # esto es lo que hace que funcionen los botones
# columnspan me permite que se ubiquen los numeros a lo ancho de la caja
pantalla_resultados.grid(row=1, column=1, padx=5, pady=0, rowspan=1, columnspan=4)
pantalla_resultados.config(background="GREEN", highlightcolor="GREEN", fg="BLACK", justify="right", width=25)

# esto es lo que hace que funcionen los botones
pantalla_operaciones = Entry(miFrame, textvariable=variable_pantalla_operaciones)
# columnspan me permite que se ubiquen los numeros a lo ancho de la caja
pantalla_operaciones.grid(row=2, column=1, padx=5, pady=0, rowspan=1, columnspan=4)
pantalla_operaciones.config(background="GREEN", highlightcolor="GREEN", fg="BLACK", justify="right", width=25)


# FUNCIONES:......................................................................
def cambiar_contenidos_pantalla():
    variable_pantalla_resultados.set(variable_pantalla_operaciones.get())
    variable_pantalla_operaciones.set("")


def boton_presionado(caracter):
    # TODO: quitar la dependencia en variables global.

    global numero_1
    global numero_2
    global operador
    global resultado

    if caracter in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "(", ")"]:
        if variable_pantalla_operaciones.get() == "0":
            if caracter != ".":
                variable_pantalla_operaciones.set(caracter)
            else:
                variable_pantalla_operaciones.set(variable_pantalla_operaciones.get() + caracter)
        else:
            variable_pantalla_operaciones.set(variable_pantalla_operaciones.get() + caracter)
    elif caracter in ["/", "x", "+", "-", "√", ",", "%", "**", "(", ")"]:
        if numero_1:
            pass
        else:
            numero_1 = float(variable_pantalla_operaciones.get())
        operador = caracter
        variable_pantalla_resultados.set(str(numero_1) + operador)
        variable_pantalla_operaciones.set("")
    elif caracter in ["=", ]:
        if operador == "√":
            numero_2 = 0
        else:
            numero_2 = float(variable_pantalla_operaciones.get())


    elif caracter == "(" and caracter == ")":  ####
        variable_pantalla_operaciones.set(caracter)  #####

        resultado = calcular_operacion(numero_1=numero_1, numero_2=numero_2, operacion=operador)
        numero_1 = resultado
        variable_pantalla_resultados.set(str(resultado))
        variable_pantalla_operaciones.set("")
        operador = ""

    elif caracter == "⌫":
        borrar_digito()
    elif caracter == "=":
        cambiar_contenidos_pantalla()


# BORRAR DIGITO, DEL:
# Borra el digito mas a la derecha
def borrar_digito():
    variable_pantalla_operaciones.set(variable_pantalla_operaciones.get()[:-1])


# LIMPIAR PANTALLA:
def reset_pantalla_c():
    variable_pantalla_operaciones.set("0")


def reset_pantalla_ce():
    # TODO: quitar la dependencia en variables global.
    global operacion
    global numero_1
    global numero_2
    operacion = 0
    numero_1 = 0
    numero_2 = 0
    variable_pantalla_operaciones.set("0")
    variable_pantalla_resultados.set("0")


# Funcion para procesar una operacion dependiendo de los numeros que se le ingreses.
# Entradas: numero_1 y/o numero_2. Se necesitan ambos para operaciones de dos operandos. Operacion a realizar.
# Resultado: resultado de la operacion.
def calcular_operacion(numero_1, numero_2, operacion):
    resultado = 0
    # TODO: estamos recibiendo la variable "operacion", pero el if esta revisando la variable "operador".
    #  Arreglar para que se utilice la variable correcta (la que se envia en el llamado de la funcion).
    if operador == "+":
        resultado = numero_1 + numero_2
    elif operador == "-":
        resultado = numero_1 - numero_2
    elif operador in ["*", "x"]:
        resultado = numero_1 * numero_2
    elif operador == "/":
        resultado = numero_1 / numero_2
    elif operador == "**":
        resultado = numero_1 ** numero_2
    elif operador == "%":
        resultado = numero_1 % numero_2
    elif operador == "√":
        resultado = sqrt(numero_1)

    return resultado


# .......................................................................................................
# -BOTONES EN PANTALLA:
boton0 = Button(miFrame, text="0", width=3, height=alto_boton, command=lambda: boton_presionado("0"))
boton0.grid(row=7, column=2)
boton1 = Button(miFrame, text="1", width=3, height=alto_boton, command=lambda: boton_presionado("1"))
boton1.grid(row=6, column=1)
boton2 = Button(miFrame, text="2", width=3, height=alto_boton, command=lambda: boton_presionado("2"))
boton2.grid(row=6, column=2)
boton3 = Button(miFrame, text="3", width=3, height=alto_boton, command=lambda: boton_presionado("3"))
boton3.grid(row=6, column=3)
boton4 = Button(miFrame, text="4", width=3, height=alto_boton, command=lambda: boton_presionado("4"))
boton4.grid(row=5, column=1)
boton5 = Button(miFrame, text="5", width=3, height=alto_boton, command=lambda: boton_presionado("5"))
boton5.grid(row=5, column=2)
boton6 = Button(miFrame, text="6", width=3, height=alto_boton, command=lambda: boton_presionado("6"))
boton6.grid(row=5, column=3)
boton7 = Button(miFrame, text="7", width=3, height=alto_boton, command=lambda: boton_presionado("7"))
boton7.grid(row=4, column=1)  # row 2 fila 2 porque la anterior miFrame esta en fila auno
boton8 = Button(miFrame, text="8", width=3, height=alto_boton, command=lambda: boton_presionado("8"))
boton8.grid(row=4, column=2)
boton9 = Button(miFrame, text="9", width=3, height=alto_boton, command=lambda: boton_presionado("9", ))
boton9.grid(row=4, column=3)

boton_bor = Button(miFrame, text="C", width=3, height=alto_boton, command=lambda: reset_pantalla_c())
boton_bor.grid(row=3, column=1)
boton_Div = Button(miFrame, text="/", width=3, height=alto_boton, command=lambda: boton_presionado(caracter="/"))
boton_Div.grid(row=3, column=2)
boton_Mult = Button(miFrame, text="x", width=3, height=alto_boton, command=lambda: boton_presionado(caracter="x"))
boton_Mult.grid(row=3, column=3)
boton_sum = Button(miFrame, text="+", width=3, height=alto_boton, command=lambda: boton_presionado(caracter="+"))
boton_sum.grid(row=3, column=4)

# fila 4
botonRest = Button(miFrame, text="-", width=3, command=lambda: boton_presionado(caracter="-"))
botonRest.grid(row=4, column=4)

# fila 5__________________________________________________________________________________________
boton_root = Button(miFrame, text="√", width=3, height=alto_boton, command=lambda: boton_presionado(caracter="√"))
boton_root.grid(row=5, column=4)

# fila 6___________________________________________________________________________________________________________
boton_coma = Button(miFrame, text=",", width=3, height=alto_boton, command=lambda: boton_presionado("."))
boton_coma.grid(row=6, column=4)
# TODO: como se quiere usar este boton? Pensar.

# fila 7 __________________________________________________________________________________________________________________

boton_porc = Button(miFrame, text="%", width=3, height=alto_boton, command=lambda: boton_presionado(caracter="%"))
boton_porc.grid(row=7, column=1)
boton_bor = Button(miFrame, text="⌫", bg=color_boton, width=3, height=alto_boton,
                   command=lambda: boton_presionado(caracter="⌫"))
boton_bor.grid(row=7, column=4)
boton_exp = Button(miFrame, text="exp", width=3, height=alto_boton, command=lambda: boton_presionado(caracter="**"))
boton_exp.grid(row=7, column=3)

# fila 8___________________________________________________________________________________________________________________________

boton_parentesis_izq = Button(miFrame, text="(", width=3, height=alto_boton, command=lambda: boton_presionado("("))
boton_parentesis_izq.grid(row=8, column=1)
boton_parentesis_der = Button(miFrame, text=")", width=3, height=alto_boton, command=lambda: boton_presionado(")"))
boton_parentesis_der.grid(row=8, column=2)
boton_resultado = Button(miFrame, text="=", bg=color_boton, width=3, height=alto_boton,
                         command=lambda: boton_presionado(caracter="="))
boton_resultado.grid(row=8, column=3, columnspan=1)
boton_ce = Button(miFrame, text="CE", bg=color_boton, width=3, height=alto_boton,
                  command=lambda: reset_pantalla_ce())
boton_ce.grid(row=8, column=4, columnspan=1)

# fila 9 ___________________________________________________________________________________________________________
barraHorizontal = Scrollbar(miFrame, relief="raised", bg=color_boton, width=25, orient="horizontal",
                            command=pantalla_operaciones.xview)
barraHorizontal.grid(row=10, column=1, padx=6, pady=10, sticky="nsew", columnspan=4)

pantalla_operaciones["xscrollcommand"] = barraHorizontal.set

raiz.mainloop()
