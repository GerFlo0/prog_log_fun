#CONSTANTES
BLOCK_WIDTH = 0.39
BLOCK_HEIGHT = 0.2
JOINT_WIDTH = 0.01
JOINT_HEIGHT = 0.015
WIND_AMOUNT = 2

#CLASES
class Wall:
    def __init__(self, width = float, height = float, windows = list):
        self.width = width
        self.height = height
        self.windows = windows
    
    def calculate_area(self):
        total_area = self.width * self.height
        windows_area = sum(w.area for w in self.windows)
        return total_area - windows_area
    
    def blocks_needed(self):
        block_area = (BLOCK_WIDTH + JOINT_WIDTH) * (BLOCK_HEIGHT + JOINT_HEIGHT)
        return self.calculate_area() / block_area

class Window:
    def __init__(self, num):
        self.width = float(input(f"Ingrese el ancho de la ventana {num}: "))
        self.height = float(input(f"Ingrese el alto de la ventana {num}: "))
        self.area = self.width * self.height

# MAIN
wall_width = float(input("Ingrese el ancho del muro: "))
wall_height = float(input("Ingrese el alto del muro: "))

windows = [Window(num+1) for num in range(WIND_AMOUNT) ]

wall = Wall(wall_width, wall_height, windows)

print(f"Para este muro se ocupan {wall.blocks_needed():,.2f} blocks")