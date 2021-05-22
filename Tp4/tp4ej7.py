################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero, error_ingreso

def division_lenta(dividendo, divisor):
    cosiente = 0
    if dividendo != 0:
        while dividendo >= divisor:
            dividendo = dividendo - divisor
            cosiente = cosiente + 1
        
        print(f"El cosiente es {cosiente}")
        print(f"El resto es {dividendo}")
    
    else:
        print("El numero no se puede dividir")

def prueba():
    dividendo = ingreso_entero("ingrese un dividendo: ")

    divisor = ingreso_entero("ingrese un divisor: ")

    division_lenta(dividendo, divisor)
pass

if __name__ == "__main__":
    prueba()