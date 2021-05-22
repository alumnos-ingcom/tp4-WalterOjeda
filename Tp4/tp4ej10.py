################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero, error_ingreso

def factores_primos(numero):
    primo = []
    
    for i in range(2, numero + 1):
        
        while numero % i == 0:
            primo.append(i)
            numero = numero / i
            
    return primo

def prueba():
    
    numero = ingreso_entero("ingrese un numero: ")
    
    primos = factores_primos(numero)
    
    print(primos)
pass

if __name__ == "__main__":
    
    prueba()