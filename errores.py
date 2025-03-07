from ErrorPersonalizado import ErrorPersonalizado

try:
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    
    if numero1 == numero2:
        raise ErrorPersonalizado("Los numeros ingresados son identicos")
    else:
        suma = numero1 + numero2
        print(f"El valor de la suma es: {suma}")
        
except Exception as e:
    print(f"Se ha generado un error: {e}")
else:
    print(f"No se ha generado un error")
finally:
    print("Se ha terminado la ejecución")
    
