#Entradas largo (16) y alto de la pared(1.9)
#medidas de las ventanas (cada una de diferente tamaño)
#v1 1.5 * 1.2  v2 2.1 * 1.4

#Constantes
BLOCK_WIDTH = 0.39
BLOCK_HEIGHT = 0.2
JOINT_WIDTH = 0.01
JOINT_HEIGHT = 0.015

#Variables

vars = [
    {
        "width" : float(input("Ingrese el ancho del muro: ")),
        "height" : float(input("Ingrese el alto del muro: "))
    },
    {
        "width" : float(input("Ingrese el ancho de la ventana 1: ")),
        "height" : float(input("Ingrese el alto de la ventana 1: "))
    },
    {
        "width" : float(input("Ingrese el ancho de la ventana 2: ")),
        "height" : float(input("Ingrese el alto de la ventana 2: "))
    }
]

#funciones

def reducir(list = list):
    resultado = list[0]
    
    for item in list[1:]: 
        resultado -= item
    
    return  resultado

def area_final(areas = list):
    
    return reducir(areas)/( (BLOCK_WIDTH+JOINT_WIDTH) * (BLOCK_HEIGHT+JOINT_HEIGHT) )

#main

areas = [item["width"] * item["height"] for item in vars]

resultado = area_final(areas)

print(f"Para este muro se ocupan {resultado:,.2f} blocks")

#datos de ejemplo 18 M de ancho por 2.7 de alto