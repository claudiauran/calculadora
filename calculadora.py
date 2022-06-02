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
operador = StringVar()  # String, para guardar el simbolo de la operacion aritmetica
resultado = 0  # Float, el resultado numerico de las operaciones aritmeticas
numero_pulsado = StringVar()  # String, la operacion enviada a la pantalla principal

input_text = StringVar()  # String, entrada de texto
alto_boton = 1
color_boton = "GRAY"

## Funciones importantes
# OK enrutar_operacion

# suma(numero1, numero2) # numero_n
# resta(numero1, numero2)
# multiplicacion(numero1, numero2)
# division(divisor, dividendo)
# porcentaje(numero)
# OK raiz cuadrada(numero)
# potencia(base, exponente)

# coma
# OK borrar digito
# OK reset pantalla
# parentesis
# resultado
# OK boton presionado(caracter) # numero, operacion


miFrame = Frame(raiz)
miFrame.pack()
miFrame.config(bg="PINK")  # cambio el fondo de alrededor de donde se escribe
miFrame.config(width="950", height="650")
# miFrame.pack(fill="both",expand="True")#expande en las dos direcciones both # se me queda a la derecha
miFrame.config(bd=35)  # cambio del grosor del borde
miFrame.config(relief="groove")  # borde especial
miFrame.config(cursor="pirate")

pantalla = Entry(miFrame, textvariable=numero_pulsado)  # esto es lo que hace que funcionen los botones
# columnspan me permite que se ubiquen los numeros a lo ancho de la caja
pantalla.grid(row=0, column=1, padx=5, pady=5, rowspan=2, columnspan=4)
pantalla.config(background="GREEN", fg="BLACK", justify="right", width=25, )  # colores

# PANTALLA______________________________________________________________________
print("Interface ok")
print("miframe,perfeto ,teclado pulsado perfecto")


# FUNCIONES:......................................................................

def boton_presionado(caracter):
    global operador
    operador = operador + str(caracter)
    input_text.set(operador)
    numero_pulsado.set(numero_pulsado.get() + caracter)


print("numero pulsado perfecto")


# BORRAR DIGITO, DEL:
# Borra el digito mas a la derecha
def borrar_digito():
    global boton_presionado
    numero_pulsado.set(numero_pulsado.get()[:-1])


# LIMPIAR PANTALLA:
def reset_pantalla():
    global operacion
    global boton_presionado
    global resultado
    boton_presionado = ""
    operacion = 0
    numero_pulsado.set("0")


print("funcion clear ok ")


# FUNCION RAIZ CUADRADA
def raiz_cuadrada(numero):
    global numero_pulsado
    global resultado
    try:  # si no se efectua la operacion se reestablceran las variables y mostrara error
        if numero_pulsado != "" and abs(float(numero_pulsado.get())) == abs(float(numero_pulsado)):
            numero_pulsado = sqrt(float(numero_pulsado))
            numero_pulsado.set(numero_pulsado)
        else:
            resultado = sqrt(resultado)
            numero_pulsado.set(resultado)
    except:
        resetear_pantalla()
        numero_pulsado.set("error")
        numero_pulsado.set(resultado)


# command=lambda:nu(num="=",operacion="resultado"(nu.get()))) IGUAL
def enrutar_operacion():
    global resultado
    global operacion
    global numero_pulsado
    global valor_rest
    numero_pulsado.set(resultado + float(numero_pulsado.get()))

    valor = float(numero_pulsado.get())
    if operador == "+":
        resultado = resultado + valor

    elif operador == "-":
        resultado = resultado - valor

    elif operador == "*":
        resultado = resultado * valor

    elif operador == "/":
        resultado = resultado / valor

    elif operador == "**":
        resultado = resultado ** valor

    elif operador == "%":
        resultado = resultado % valor

        try:
            resultado = valor
        except:
            numero_pulsado.set(numero_pulsado.get())
        try:
            operacion = valor_rest
            if numero_pulsado == "":
                numero_pulsado = resultado
                calculo = (operacion)
                numero_pulsado.set(resultado)
        except:
            numero_pulsado.set("error")
            numero_pulsado = 0
            resultado = 0
            valor_rest = ""
            operacion = ""
            numero_pulsado.set(resultado)


# .......................................................................................................
# -BOTONES EN PANTALLA:
# FILA 3
boton_bor = Button(miFrame, text="C", width=3, height=alto_boton, command=lambda: reset_pantalla())
boton_bor.grid(row=3, column=1)
boton_Div = Button(miFrame, text="/", width=3, height=alto_boton,
                   command=lambda: boton_presionado(caracter=numero_pulsado.get(), operacion="divide"))
boton_Div.grid(row=3, column=2)
boton_Mult = Button(miFrame, text="x", width=3, height=alto_boton,
                    command=lambda: boton_presionado(caracter="x",
                                                     enrutar_operacion="multiplica"(numero_pulsado.get())))
boton_Mult.grid(row=3, column=3)
boton_sum = Button(miFrame, text="+", width=3, height=alto_boton,
                   command=lambda: boton_presionado(caracter="+", enrutar_operacion="suma"(numero_pulsado.get)))
boton_sum.grid(row=3, column=4)

# fila 4
boton7 = Button(miFrame, text="7", width=3, height=alto_boton, command=lambda: boton_presionado("7"))
boton7.grid(row=4, column=1)  # row 2 fila 2 porque la anterior miFrame esta en fila auno
boton8 = Button(miFrame, text="8", width=3, height=alto_boton, command=lambda: boton_presionado("8"))
boton8.grid(row=4, column=2)
boton9 = Button(miFrame, text="9", width=3, height=alto_boton, command=lambda: boton_presionado("9", ))
boton9.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3,
                   command=lambda: boton_presionado(caracter="-", enrutar_operacion="resta"(numero_pulsado.get())))
botonRest.grid(row=4, column=4)

# fila 5__________________________________________________________________________________________

boton4 = Button(miFrame, text=4, width=3, height=alto_boton, command=lambda: boton_presionado("4"))
boton4.grid(row=5, column=1)
boton5 = Button(miFrame, text="5", width=3, height=alto_boton, command=lambda: boton_presionado("5"))
boton5.grid(row=5, column=2)
boton6 = Button(miFrame, text="6", width=3, height=alto_boton, command=lambda: boton_presionado("6"))
boton6.grid(row=5, column=3)

boton_root = Button(miFrame, text="√", width=3, height=alto_boton,
                    command=lambda: boton_presionado(caracter="√", enrutar_operacion="sqrt"(numero_pulsado.get)))
boton_root.grid(row=5, column=4)

# fila 6___________________________________________________________________________________________________________

boton1 = Button(miFrame, text="1", width=3, height=alto_boton, command=lambda: boton_presionado("1"))
boton1.grid(row=6, column=1)
boton2 = Button(miFrame, text="2", width=3, height=alto_boton, command=lambda: boton_presionado("2"))
boton2.grid(row=6, column=2)
boton3 = Button(miFrame, text="3", width=3, height=alto_boton, command=lambda: boton_presionado("3"))
boton3.grid(row=6, column=3)
boton_coma = Button(miFrame, text=",", width=3, height=alto_boton, command=lambda: boton_presionado("."))
boton_coma.grid(row=6, column=4)

# fila 7 __________________________________________________________________________________________________________________

boton_porc = Button(miFrame, text="%", width=3, height=alto_boton,
                    command=lambda: boton_presionado(caracter="%",
                                                     enrutar_operacion="porcentage"(numero_pulsado.get())))
boton_porc.grid(row=7, column=1)
boton0 = Button(miFrame, text="0", width=3, height=alto_boton, command=lambda: boton_presionado("0"))
boton0.grid(row=7, column=2)
boton_bor = Button(miFrame, text="⌫", bg=color_boton, width=3, height=alto_boton,
                   command=lambda: boton_presionado("⌫", enrutar_operacion="borrar_digito"(numero_pulsado.get())))
boton_bor.grid(row=7, column=4)
boton_exp = Button(miFrame, text="exp", width=3, height=alto_boton,
                   command=lambda: boton_presionado(caracter="**", enrutar_operacion="potencia"(numero_pulsado.get)))
boton_exp.grid(row=7, column=3)

# fila 8___________________________________________________________________________________________________________________________

boton_parent = Button(miFrame, text="(", width=3, height=alto_boton, command=lambda: boton_presionado("("))
boton_parent.grid(row=8, column=1)
boton0 = Button(miFrame, text=")", width=3, height=alto_boton, command=lambda: boton_presionado(")"))
boton0.grid(row=8, column=2)
boton_resultado = Button(miFrame, text="=", bg=color_boton, width=10, height=alto_boton,
                         command=lambda: boton_presionado(caracter="=",
                                                          enrutar_operacion="resultado"(numero_pulsado.get())))
boton_resultado.grid(row=8, column=3, columnspan=2)

# fila 9 ___________________________________________________________________________________________________________

barraHorizontal = Scrollbar(miFrame, relief="raised", bg=color_boton, width=25, orient="horizontal",
                            command=pantalla.xview)
barraHorizontal.grid(row=9, column=1, padx=6, pady=10, sticky="nsew", columnspan=4)
pantalla["xscrollcommand"] = barraHorizontal.set

print("teclado perfecto")

raiz.mainloop()
# numeroPulsado representa en la pantalla la operacion mediante input_text.set(aqui cadena de caracteres )
