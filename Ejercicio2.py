class CuentaBancaria:
    def __init__(self, titular=""):
        self.__titular = titular
        self.__saldo = 0

    @property
    def titular(self):
        return self.__titular  

    @property
    def saldo(self):
        return self.__saldo 

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Has depositado {cantidad} pesos. Tu saldo es {self.__saldo} pesos.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Has retirado {cantidad} pesos. Tu saldo es {self.__saldo} pesos.")
        else:
            print("No tienes los fondos suficientes")

    def estado(self):
        print(f"Saldo actual: {self.__saldo} pesos.")


def menu():
    titular = input("Ingrese el nombre del titular: ")
    cuenta = CuentaBancaria(titular)
    while True:
        print("1. Depositar")
        print("2. Retirar")
        print("3. Ver saldo")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "3":
            cuenta.estado()
            break
        else:
            print("Opción inválida")
menu()