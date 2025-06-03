empleados = []
empleados.append("Laura")
empleados.append("Carlos")

print("Lista de empleados")
for nombre in empleados:
    print(nombre)

class ListaEmpleados:
    def _init_(self):
        self.lista = []

    def agregar(self, nombre):
        if nombre not in self.lista:
            self.lista.append(nombre)
        else:
            print(f"{nombre} ya esta registrado")

    def mostrar(self):
        print("Lista de empleados:")
        for nombre in self.lista:
            print(nombre)
