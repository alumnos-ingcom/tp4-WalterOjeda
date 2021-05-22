################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero, error_ingreso

def compara(numero, numero2):
    if numero < numero2:
        return -1
    elif numero == numero2:
        return 0
    else:
        return 1
def prueba():   
    numero = ingreso_entero("ingrese un numero: ")
    numero2 = ingreso_entero("ingrese un numero: ")

    retorno = compara(numero, numero2)

    print(f"{retorno}")
pass

if __name__ == "__main__":
    prueba()