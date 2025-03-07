""" Crear un programa que te permita ingresar una lista de 10 numeros 
    al final del programa te devolvera la lsita ordenada de menor a mayor, 
    te debe de generar un error en caso de que ingreses un numero 
    negativo o decimal, o repetido
 """
from ErrorPersonalizado import ErrorPersonalizado

try:
    
    def ordenar_lista():
        numeros = []
        
        while len(numeros) < 10:
            numero = input(f"Ingresa el numero {len(numeros) + 1}:")
            
            if "." in numero:
                raise ErrorPersonalizado("No se permiten decimales")
            
            numero = int(numero)
            
            if numero < 0:
                raise ErrorPersonalizado("No se permiten numeros negativos")
            if numero in numeros:
                raise ErrorPersonalizado("No se permiten numeros repetidos")
            
            numeros.append(numero)
            
        ordenados = sorted(numeros)
        print(f"La lista ordenada es: {ordenados}")
        
    ordenar_lista()
    
except Exception as e:
    print(f"Se ha generado un error: {e}")
else:
    print("No se ha generado ningun error")
finally:
    print("El programa ha finalizado")
  