################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp4ej1 import ingreso_entero, error_ingreso

def es_palindromo(texto):
    textolimpio = []
    
    texto = texto.lower()
    palabras = texto.split()
    
    for i in palabras:
        letras = i.strip(".")
        letras = i.strip(",")
        textolimpio.append(letras)
        cadenalimpia = "".join(textolimpio)
    if str(cadenalimpia) == str(cadenalimpia)[::-1]:
        return True
    else:
        return False
pass

def prueba():
    mensaje = input("Ingrese ensaje: ")

    resultado = es_palindromo(mensaje)

    if resultado == True:
        print("Es palindromo")
    else:
        print("No es palindromo")
pass
        
if __name__ == "__main__":
    prueba()