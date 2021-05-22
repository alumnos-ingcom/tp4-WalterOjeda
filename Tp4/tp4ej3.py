################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero, error_ingreso

def convertir_a_fahrrenheit(centigrados):
    centigrados = ingreso_entero(centigrados)
    fahrrenheit = (centigrados * 1.8) + 32
    return fahrrenheit
    
def convertir_a_centigrados(fahrenheit):
    fahrenheit = ingreso_entero(fahrenheit)
    centigrados = (fahrenheit - 32) / 1.8
    return centigrados

def prueba():
    opcion = input("Convertir fahrenheit/centigrados(F) o centigrados/fahrenheit (C): ")

    if opcion == 'F' or opcion == 'f':
        Gfahrenheit = convertir_a_centigrados("ingrese grados fahrenheit: ")
        print(f"{Gfahrenheit}")
        
    elif opcion == 'C' or opcion == 'c':
        Gcentigrados = convertir_a_fahrrenheit("ingrese grados centigrados: ")
        print(f"{Gcentigrados}")
        
    else:
        print("Opcion no valida, intente de nuevo")
pass

if __name__ == "__main__":
    prueba()