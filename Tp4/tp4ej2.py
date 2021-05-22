################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero, error_ingreso

def suma_lenta(primer_numero, segundo_numero):
    i = 1
    while i <= segundo_numero:
        suma = primer_numero + i
        print(f"{primer_numero} + {i} = {suma}")
        i = i+1

def prueba():
    primer_numero = ingreso_entero("ingrese primer numero: ")
    segundo_numero = ingreso_entero("ingrese segundo numero: ")

    suma_lenta(primer_numero, segundo_numero)
pass

if __name__ == "__main__":
    prueba()