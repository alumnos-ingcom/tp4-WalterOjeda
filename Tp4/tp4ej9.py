################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero, error_ingreso

def es_primo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

def prueba():

    numero = ingreso_entero("ingrese numero: ")

    resultado = es_primo(numero)

    if resultado is True:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")
pass

if __name__ == "__main__":
    prueba()