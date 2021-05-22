################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero, error_ingreso

def signo(numero_ingreso):
    numero= ingreso_entero(numero_ingreso)
    if numero < 0:
        print(f"{numero} es negativo")
    elif numero == 0:
        print(f"{numero} es cero")
    else:
        print(f"{numero} es positivo")

def prueba():
    signo("ingrese un numero: ")
pass

if __name__ == "__main__":
    prueba()