import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ivan Ignacio Marrero
Division 1G

Ejercicio 01:

Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar
en la bolsa de valores:
A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:
* Nombre
* Monto en pesos de la operación (no menor a $10000)
* Cantidad de instrumentos
* Tipo (CEDEAR, BONOS, MEP)
B) Luego del ingreso mostrar en pantalla todos los datos.
C) Realizar los siguientes informes:
1. Tipo de instrumento que más se operó.
2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron
más de $50000.
3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP,
que menos dinero invirtió. Puede ser más de uno.
4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el
monto promedio
5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto
no supere los $50000.
'''

listaNombre = []
listaMonto = []
listaCantidad = []
listaTipo = []
contador = 0
CEDEARCantidad = 0
BONOSCantidad = 0
MEPCantidad = 0
usuariosBonos = 0


pregunta = question("Bienvenido", "¿Desea empezar?")

while pregunta != False: 

    nombre = prompt("Nombre", "Ingrese su nombre: ")
    while nombre == None or not nombre.isalpha():
        nombre = prompt("Error", "Ingrese su nombre correctamente: ")

    listaNombre.append(nombre)

    montoPesos_str = prompt("Monto", "Ingrese su monto en pesos (No menor a $10000)")
    montoPesos = int(montoPesos_str)
    while montoPesos_str == None or not montoPesos_str.isdigit() or montoPesos < 10000:
        montoPesos_str = prompt("Error", "Ingrese su monto en pesos correctamente")
        montoPesos = int(montoPesos_str)

    listaMonto.append(montoPesos_str)

    cantidadInstrumentos_str = prompt("Instrumentos", "Cantidad de instrumentos a usar")
    cantidadInstrumentos = int(cantidadInstrumentos_str)
    while cantidadInstrumentos_str == None or not cantidadInstrumentos_str.isdigit():
        cantidadInstrumentos_str = prompt("Error", "Ingrese la cantidad de instrumentos correctamente")
        cantidadInstrumentos = int(cantidadInstrumentos_str)

    listaCantidad.append(cantidadInstrumentos_str)

    tipoInstrumento = prompt("Tipo", "Tipo de instrumento (CEDEAR, BONOS, MEP)")
    while tipoInstrumento == None or tipoInstrumento != "CEDEAR" and tipoInstrumento != "BONOS" and tipoInstrumento != "MEP":
        tipoInstrumento = prompt("Error", "Ingrese correctamente el tipo de instrumento (CEDEAR, BONOS, MEP)")

    listaTipo.append(tipoInstrumento)

    match tipoInstrumento:
        case "CEDEAR":

            CEDEARCantidad += 1

        case "BONOS":

            BONOSCantidad += 1

            if cantidadInstrumentos >= 150 and cantidadInstrumentos <= 200 and montoPesos > 50000:
                usuariosBonos =+ 1

        case "MEP":

            MEPCantidad += 1

    


    pregunta = question("Pregunta", "¿Desea ingresar otro usuario?")

for nombre in listaNombre:
    print("Nombre: " + nombre + " | Monto en pesos: $" + listaMonto[contador] + " | Cant. de instrumentos: " + listaCantidad[contador] + " | Tipo: " + listaTipo[contador])
    contador += 1

if CEDEARCantidad > BONOSCantidad and CEDEARCantidad > MEPCantidad:

    tipoMasUsado = "CEDEAR"
    
elif BONOSCantidad > CEDEARCantidad and BONOSCantidad > MEPCantidad:

    tipoMasUsado = "BONOS"

elif MEPCantidad > CEDEARCantidad and MEPCantidad > BONOSCantidad:

    tipoMasUsado = "MEP"

else:

    tipoMasUsado = "Ninguno"



print("\nEl intrumento mas usado es: " + tipoMasUsado)
print("Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000: " + str(usuariosBonos))

