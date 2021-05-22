################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero, error_ingreso

def minimo(lista):
    min=999999
    for i in lista:
        if i <= min:
            min = i
    return min
    
def maximo(lista):
    max=-9999
    
    for i in lista:
        if i > max:
            max = i
    return max

def prueba():
    lista = [-5, 50, 1000, 63, 23, -62, -8]

    minimo1 = minimo(lista)
    print(f"el numero mas chico es {minimo1}")

    maximo1 = maximo(lista)
    print(f"el numero mas grande es {maximo1}")
pass 

if __name__ == "__main__":
    prueba()