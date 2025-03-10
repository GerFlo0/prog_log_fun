#material para el techo de una casa

#CONSTANTES

ROOF_HEIGHT = 0.1

MATERIALS_PER_CUB_METER = {
    "cement" : 7,
    "sand" : 0.56,
    "gravel" : 0.84,
    "water" : 180
}

#MAIN
roof = {
    "length" : float(input("Ingrese el ancho del cuarto: ")),
    "width" : float(input("Ingrese el frente del cuarto: "))
}

floor_area = roof["length"] * roof["width"]

floor_volume = floor_area * ROOF_HEIGHT

materials_total = {k: v * floor_volume for k, v in list(MATERIALS_PER_CUB_METER.items())}

print(f"""Para este techo de {floor_area} metros cuadrados se necesitaran los siguientes materiales
    Cemento: {materials_total['cement']:,.2f} bultos ({materials_total['cement']*50:,.2f} kg)
    Arena: {materials_total['sand']:,.2f} metros cubicos
    Grava: {materials_total['gravel']:,.2f} metros cubicos
    Agua: {materials_total['water']:,.2f} litros""")