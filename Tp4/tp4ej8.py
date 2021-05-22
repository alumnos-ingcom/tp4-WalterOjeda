################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero, error_ingreso

def ordenar_menor_a_mayor(uno, dos, tres):
    if uno < dos:
        if dos < tres:
            print(f"{uno}, {dos}, {tres}")
        elif uno < tres:
            print(f"{uno}, {tres}, {dos}")
        else:
            print(f"{tres}, {uno}, {dos}")
    else:
        if uno < tres:
            print(f"{dos}, {uno}, {tres}")
        elif dos < tres:
            print(f"{dos}, {tres}, {uno}")
        else:
            print(f"{tres}, {dos}, {uno}")
            
def ordenar_mayor_a_menor(uno, dos, tres):
    if uno > dos:
        if dos > tres:
            print(f"{uno}, {dos}, {tres}")
        elif uno > tres:
            print(f"{uno}, {tres}, {dos}")
        else:
            print(f"{tres}, {uno}, {dos}")
    else:
        if uno > tres:
            print(f"{dos}, {uno}, {tres}")
        elif dos > tres:
            print(f"{dos}, {tres}, {uno}")
        else:
            print(f"{tres}, {dos}, {uno}")
            
def prueba():
    uno1 = ingreso_entero("ingrese numero: ")
    dos2 = ingreso_entero("ingrese numero: ")
    tres3 = ingreso_entero("ingrese numero: ")
    
    ordenar_mayor_a_menor(uno1, dos2, tres3)
    ordenar_menor_a_mayor(uno1, dos2, tres3)
pass

if __name__ == "__main__":
    prueba()