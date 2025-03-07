# Archivo de constantes
FACTOR_C_F = 1.8   # Factor para convertir Celsius a Fahrenheit
FACTOR_K_C = 273.15  # Kelvin a Celsius

class Temperaturas:
    @staticmethod
    def conversion1(celsius):
        return celsius * FACTOR_C_F + 32

    @staticmethod
    def conversion2(fahrenheit):
        return (fahrenheit - 32) / FACTOR_C_F

    @staticmethod
    def conversion3(celsius):
        return celsius + FACTOR_K_C

    @staticmethod
    def conversion4(kelvin):
        return kelvin - FACTOR_K_C

def menu():
    conversor = Temperaturas()
    
    while True:
        print("\nMenú de Conversión de Temperaturas:")
        print("1) Celsius a Fahrenheit")
        print("2) Fahrenheit a Celsius")
        print("3) Celsius a Kelvin")
        print("4) Kelvin a Celsius")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            celsius = float(input("Ingrese la temperatura en Celsius: "))
            print(f"{celsius}°C = {conversor.conversion1(celsius)}°F")
        elif opcion == "2":
            fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
            print(f"{fahrenheit}°F = {conversor.conversion2(fahrenheit)}°C")
        elif opcion == "3":
            celsius = float(input("Ingrese la temperatura en Celsius: "))
            print(f"{celsius}°C = {conversor.conversion3(celsius)}K")
        elif opcion == "4":
            kelvin = float(input("Ingrese la temperatura en Kelvin: "))
            print(f"{kelvin}K = {conversor.conversion4(kelvin)}°C")
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()
