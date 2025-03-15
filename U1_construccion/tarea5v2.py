#CONSTANTES
ROOF_HEIGHT = 0.1
MATERIALS_PER_CUB_METER = {
    "cement": 7,
    "sand": 0.56,
    "gravel": 0.84,
    "water": 180
}

#CLASE
class Roof:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.floor_area = self.width * self.length
        self.floor_volume = self.floor_area * ROOF_HEIGHT
    
    def calculate_materials(self):
        return {k: v * self.floor_volume for k, v in MATERIALS_PER_CUB_METER.items()}
    
    def display_materials(self):
        materials_total = self.calculate_materials()
        print(f"""Para este techo de {self.length * self.width} metros cuadrados se necesitarán los siguientes materiales:
            Cemento: {materials_total['cement']:,.2f} bultos ({materials_total['cement'] * 50:,.2f} kg)
            Arena: {materials_total['sand']:,.2f} metros cúbicos
            Grava: {materials_total['gravel']:,.2f} metros cúbicos
            Agua: {materials_total['water']:,.2f} litros""")

#MAIN
length = float(input("Ingrese el ancho del cuarto: "))
width = float(input("Ingrese el frente del cuarto: "))

roof = Roof(length, width)
roof.display_materials()