class Triangulo:
    def _init_(self):
        
        self.base = 0
        self.altura = 0

    def leer_datos(self):
        
        self.base = float(input("Ingresa la base del triángulo: "))
        self.altura = float(input("Ingresa la altura del triángulo: "))

    def calcular_area(self): 
        
        return (self.base * self.altura) / 2

t = Triangulo()

t.leer_datos()

print("El área del triángulo es:", t.calcular_area())
