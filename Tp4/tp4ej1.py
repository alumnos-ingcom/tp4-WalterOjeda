################
# Walter Ojeda - @walter_ojeda
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class error_ingreso(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 

def ingreso_entero(mensaje):

    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise error_ingreso("la entrada no es valida, reintentar") from err
    return entero


def ingreso_entero_restringido(mensaje, valor_minimo, valor_maximo):
    
    numero = ingreso_entero(mensaje)
    
    if(numero >= valor_minimo and numero <= valor_maximo):
        return numero
    else:
        print(f"El numero {numero} no se encuentra entre {valor_minimo} y {valor_maximo}, Intente nuevamente ^^")

def prueba():
    ValorMinimo = ingreso_entero("ingrese un minimo: ")
    ValorMaximo = ingreso_entero("ingrese un maximo: ")

    Ingrese_Numero = ingreso_entero_restringido("Ingrese un numero: ", ValorMinimo, ValorMaximo)

    if Ingrese_Numero != None:
        print(f"El {Ingrese_Numero} se encuentra entre {ValorMinimo} y {ValorMaximo}")
pass

if __name__ == "__main__":
    prueba()