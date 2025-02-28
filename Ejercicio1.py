class Coche:
    def __init__(self, marca="", modelo=""):
        self.__marca = marca
        self.__modelo = modelo
        self.__combustible = 100 

    @property
    def marca(self):
        return self.__marca 

    @property
    def modelo(self):
        return self.__modelo  

    @property
    def combustible(self):
        return self.__combustible

    def conducir(self, km):
        consumo = km // 10  
        if consumo > self.__combustible:
            print("Combustible bajo")
        else:
            self.__combustible -= consumo
            print(f"Has conducido {km} km. El combustible restante es: {self.__combustible} litros")

    def repostar(self, litros):
        if self.__combustible + litros > 100:
            self.__combustible = 100 
            print("El tanque está lleno")
        else:
            self.__combustible += litros
            print(f"Agregaste {litros} litros. El combustible actual es: {self.__combustible} litros")

    def estado(self): 
        print(f"El combustible restante es: {self.__combustible} litros")

def menu():
    marca = input("Ingrese la marca del coche: ")
    modelo = input("Ingrese el modelo del coche: ")
    resultado = Coche(marca, modelo)
    while True:
        print("1. Conducir")
        print("2. Repostar")
        print("3. Ver estado")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            km = int(input("Ingrese los kilómetros a conducir: "))
            resultado.conducir(km)
        elif opcion == "2":
            litros = int(input("Ingrese los litros a repostar: "))
            resultado.repostar(litros)
        elif opcion == "3":
            resultado.estado()
            break
        else:
            print("Opción inválida")
menu()