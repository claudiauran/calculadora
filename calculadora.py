from math import *
from tkinter import *
from turtle import clear

from colorama import init, Fore

raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()
# operacion=""
reset_pantalla = False
resultado = 0
alto_boton = 1
color_boton = ("GRAY")  ######################
operacion = ()
operador = ()
elResultado = 0
imput_tex = StringVar()

# PANTALLA______________________________________________________________________
print(Fore.RED + "__________________________________________________")
init
nu = StringVar()
numeroPulsado = StringVar()
raiz.title(Fore.RED + "CALCULADORA")
raiz.geometry("+500+100")

operacion = StringVar()
input_text = StringVar()
operador = ""
nu = StringVar()  # (nu por nu)
pantalla = Entry(miFrame)
pantalla = Entry(miFrame, textvariable=nu)  # esto es lo que hace que funcionen los botones
print("ok")
# pantalla=Entry(miFrame, textvariable=nu)
pantalla.grid(row=0, column=1, padx=5, pady=5, rowspan=2,
              columnspan=4)  # columnspan me permite que se ubiquen los numeros a lo ancho de la caja
pantalla.config(background="GREEN", fg="BLACK", justify="right", width=25, )  # colores
print("ok ok ")
miFrame.config(bg="PINK")  # cambio el fondo de al rededor de donde se escribe
height = alto_boton  # HEINGHT=ALTURA
print("ok")

miFrame.config(width="950", height="650")
# miFrame.pack(fill="both",expand="True")#expande en las dos direcciones both # se me queda a al aderecha
miFrame.config(bd=35)  # cambio del grosor del borde
miFrame.config(relief="groove")  # borde especial
miFrame.config(cursor="pirate")

raiz.config(bd=35)  # cambio del grosor del borde
raiz.config(relief="groove")  # borde especial

print("miframe,perfeto ,teclado pulsado perfecto")


# FUNCIONES:......................................................................

def numeroPulsado(num):
    global operador
    operador = operador + str(num)
    input_text.set(operador)
    nu.set(nu.get() + num)


print("numero pulsado perfecto")


# BORRAR DIGITO, DEL:
# command=lambda:numeroPulsado("⌫",operacion="borrar_digito"(nu.get)))
def borrar_digito():
    global numeroPulsado
    nu.set(nu.get()[:-1])


"""def borrar_digito():
global numero
numero=""
nu.set("0")"""


# LIMPIAR PANTALLA:
# boton_bor=Button(miFrame,text="C",width=3,height=alto_boton,command=reset_pantalla)
def reset_pantalla():
    global operacion
    global numeroPulsado
    global resultado
    numeroPulsado = ""
    operacion = 0
    nu.set("0")


print("funcion clear ok ")


# FUNCIONES DE CALCULO____________________________________________________________________________

def calculo(operador):
    global resultado
    if operador == "+":
        resultado = resultado + float(nu)

    elif operador == "-":
        resultado = resultado - float(nu)

    elif operador == "*":
        resultado = resultado * float(nu)

    elif operador == "/":
        resultado = resultado / float(nu)

    elif operador == "**":
        resultado = resultado ** float(nu)

    elif operador == "%":
        resultado = resultado % float(nu)


# FUNCION RAIZ CUADRADA
def raiz_cuadrada():
    global nu
    global resultado
    try:  # si no se efectua la operacion se reestablceran las variables y mostrara error
        if nu != "" and abs(float(nu.get())) == abs(float(nu)):
            nu = sqrt(float(nu))
            nu.set(nu)
        else:
            resultado = sqrt(resultado)
            nu.set(resultado)
    except:
        reset_pantalla()
        nu.set("error")
        nu.set(resultado)


# command=lambda:nu(num="=",operacion="resultado"(nu.get()))) IGUAL
def resultado():
    global resultado
    global operacion
    global nu
    global valor_rest
    nu.set(resultado + float(nu.get()))

    if operador == "+":
        resultado = resultado + float(nu)

    elif operador == "-":
        resultado = resultado - float(nu)

    elif operador == "*":
        resultado = resultado * float(nu)

    elif operador == "/":
        resultado = resultado / float(nu)

    elif operador == "**":
        resultado = resultado ** float(nu)

    elif operador == "%":
        resultado = resultado % float(nu)

        try:
            resultado = float(nu.get())
        except:
            nu.set(nu.get())
        try:
            operacion = valor_rest
            if nu == "":
                nu = resultado
                calculo = (operacion)
                nu.set(resultado)
        except:
            nu.set("error")
            nu = 0
            resultado = 0
            valor_rest = ""
            operacion = ""
            nu.set(resultado)


# .......................................................................................................
# input_text=StringVar()
# perador=""
# -BOTONES EN PANTALLA:
# FILA 3
boton_bor = Button(miFrame, text="C", width=3, height=alto_boton,
                   command=reset_pantalla)  # lambda:nu(num="c",operacion="reset_pantalla"(nu.get)))
boton_bor.grid(row=3, column=1)
boton_Div = Button(miFrame, text="/", width=3, height=alto_boton,
                   command=lambda: nu(num="/", operacion="divide"(nu.get())))
boton_Div.grid(row=3, column=2)
boton_Mult = Button(miFrame, text="x", width=3, height=alto_boton,
                    command=lambda: nu(num="x", operacion="multiplica"(nu.get())))
boton_Mult.grid(row=3, column=3)
boton_sum = Button(miFrame, text="+", width=3, height=alto_boton, command=lambda: nu(num="+", operacion="suma"(nu.get)))
boton_sum.grid(row=3, column=4)

# fila 4
boton7 = Button(miFrame, text="7", width=3, height=alto_boton, command=lambda: numeroPulsado("7"))
boton7.grid(row=4, column=1)  # row 2 fila 2 porque la anterior miFrame esta en fila auno
boton8 = Button(miFrame, text="8", width=3, height=alto_boton, command=lambda: numeroPulsado("8"))
boton8.grid(row=4, column=2)
boton9 = Button(miFrame, text="9", width=3, height=alto_boton, command=lambda: numeroPulsado("9", ))
boton9.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3, command=lambda: nu(num="-", operacion="resta"(nu.get())))
botonRest.grid(row=4, column=4)

# fila 5__________________________________________________________________________________________

boton4 = Button(miFrame, text=4, width=3, height=alto_boton, command=lambda: numeroPulsado("4"))
boton4.grid(row=5, column=1)
boton5 = Button(miFrame, text="5", width=3, height=alto_boton, command=lambda: numeroPulsado("5"))
boton5.grid(row=5, column=2)
boton6 = Button(miFrame, text="6", width=3, height=alto_boton, command=lambda: numeroPulsado("6"))
boton6.grid(row=5, column=3)

boton_root = Button(miFrame, text="√", width=3, height=alto_boton,
                    command=lambda: nu(num="√", operacion="sqrt"(nu.get)))
boton_root.grid(row=5, column=4)

# fila 6___________________________________________________________________________________________________________

boton1 = Button(miFrame, text="1", width=3, height=alto_boton, command=lambda: numeroPulsado("1"))
boton1.grid(row=6, column=1)
boton2 = Button(miFrame, text="2", width=3, height=alto_boton, command=lambda: numeroPulsado("2"))
boton2.grid(row=6, column=2)
boton3 = Button(miFrame, text="3", width=3, height=alto_boton, command=lambda: numeroPulsado("3"))
boton3.grid(row=6, column=3)
boton_coma = Button(miFrame, text=",", width=3, height=alto_boton, command=lambda: numeroPulsado("."))
boton_coma.grid(row=6, column=4)

# fila 7 __________________________________________________________________________________________________________________

boton_porc = Button(miFrame, text="%", width=3, height=alto_boton,
                    command=lambda: nu(num="%", operacion="porcentage"(nu.get())))
boton_porc.grid(row=7, column=1)
# tton(ventana,text="%",width=6,fg="white",bg="gray6",height=1,command=lambda:operacion("%"))
boton0 = Button(miFrame, text="0", width=3, height=alto_boton, command=lambda: numeroPulsado("0"))
boton0.grid(row=7, column=2)
boton_bor = Button(miFrame, text="⌫", bg=color_boton, width=3, height=alto_boton,
                   command=lambda: numeroPulsado("⌫", operacion="borrar_digito"(nu.get())))
boton_bor.grid(row=7, column=4)
boton_exp = Button(miFrame, text="exp", width=3, height=alto_boton, command=lambda: nu(num="**", operacion="potencia"(
    nu.get)))  # nu(num="**",operacion="potencia"(nu.get())))#numeroPulsado("**"))
boton_exp.grid(row=7, column=3)

# fila 8___________________________________________________________________________________________________________________________

boton_parent = Button(miFrame, text="(", width=3, height=alto_boton, command=lambda: numeroPulsado("("))
boton_parent.grid(row=8, column=1)
boton0 = Button(miFrame, text=")", width=3, height=alto_boton, command=lambda: numeroPulsado(")"))
boton0.grid(row=8, column=2)
boton_resultado = Button(miFrame, text="=", bg=color_boton, width=10, height=alto_boton, command=lambda: nu(num="=",
                                                                                                            operacion="resultado"(
                                                                                                                nu.get())))  # lambda:numeroPulsado("=",operacion="total_resultado"(nu.get)))
boton_resultado.grid(row=8, column=3, columnspan=2)

# fila 9 ___________________________________________________________________________________________________________

barraHorizontal = Scrollbar(miFrame, relief="raised", bg=color_boton, width=25, orient="horizontal",
                            command=pantalla.xview)
barraHorizontal.grid(row=9, column=1, padx=6, pady=10, sticky="nsew", columnspan=4)
pantalla["xscrollcommand"] = barraHorizontal.set

clear()

print("teclado perfecto")

raiz.mainloop()

# numeroPulsado representa en la pantalla la operacion mediante input_tex.set(aqui cadena de caracteres )


"""def operacion():
    global numeroPulsado
    opera=eval(operacion)#eval calculo con cadena 
    input_text.set(opera)
    nu.set(str(resultado))"""

"""def operacion():
global numeroPulsado
operador=float(nu.get())"""

# coma
"""def coma():
    global numeroPulsado
    if numeroPulsado!="" and not "." in  str (nu) and exc==False:
        nu=nu+","
        nu.set(nu)"""

# def calculo():
