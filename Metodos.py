from math import factorial
# importacion de libreria para factorial.


def numero_int(entrada):
    # función que verifica que el numero sea entero.
    return isinstance(entrada, int)
    # si es entero regresa True


def numero_float(entrada):
    return isinstance(entrada, float)


def multiple_op(X):
    # metodo uno, verifica que recibe un numero,
    # realiza operaciones y retorna un arreglo con el resultado.
    # El parametro de entrada es un numero.

    resultados_metodo_1 = []
    # se inicia el arreglo

    if numero_int(X) and int(X) >= 0:
        # solo si cumple las condiciones de ser
        # numero entero positivo procede

        resultados_metodo_1.append(X*X)
        resultados_metodo_1.append(pow(2, X))
        resultados_metodo_1.append(factorial(X))
        return resultados_metodo_1
        # retorno del arreglo final

    else:
        print("Código de error 3312.")
        return "Código de error 3312."


def verify_array_op(arreglo):
    # Metodo dos, verifica que recibe solo numeros,
    # llama al metodo 1 y retorna un arreglo con el
    # resultado. El parametro de entrada es un arreglo.

    resultados_metodo_2 = []
    largo = len(arreglo)
    # cantidad de elementos del arreglo.

    i = 0
    while i < largo:
        # ciclo que recorre cada elemento del arreglo
        # y llama a la funcion uno enviandolo el dato del arreglo.

        if numero_int(arreglo[i]) and int(arreglo[i]) >= 0:
            resultados_metodo_2.append(multiple_op(arreglo[i]))

        else:
            print("Código de error 3141.")
            return "Código de error 3141."
        i += 1

    return resultados_metodo_2
    # una vez que termina la lista imprime
    # el resultado como un arreglo de arreglos.

# Codigos de error:
# 3141 #codigo de error arreglo que
# no cumple con tener numeros enteros positivos.
# 3312 #codigo de error para elemento que
# no cumple con ser numero entero positivo.
