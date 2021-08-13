import Metodos
from math import factorial
import random
# Llamado de las librerías a usar.
# Importación de librerías para el factorial


def right_ans_m1(dato):
    # Función para determinar la respuesta correcta del métdo 1
    resultados_metodo_1 = []
    # se inicia el arreglo vacío
    if isinstance(dato, int) and dato >= 0:
        # solo si cumple las condiciones de ser numero entero positivo procede
        # Se crean los resultados que se van a agregar al arreglo
        resultados_metodo_1.append(dato*dato)
        resultados_metodo_1.append(pow(2, dato))
        resultados_metodo_1.append(factorial(dato))
        return resultados_metodo_1
        # Devuelve el arreglo con los resultados
    else:
        return "Código de error 3312."


def right_ans_m2(arreglo):
    # Fución para determinar la respuesta correcta del método 2 (Array)
    resultados_metodo_2 = []
    # Arreglo vacío para almacenar los resultados
    largo = len(arreglo)
    i = 0
    while i < largo:
        # ciclo que recorre cada elemento del arreglo
        # y llama a la funcion uno enviandolo el dato del arreglo

        if isinstance(arreglo[i], int) and arreglo[i] >= 0:
            resultados_metodo_2.append(right_ans_m1(arreglo[i]))
        else:
            return "Código de error 3141."
        i += 1
    return resultados_metodo_2


def test_multiple_op():
    wrong_array = [-1, "a", 0.2, -5.99, "palabra"]
    wrong_elem = wrong_array[random.randrange(0, 4)]
    assert Metodos.multiple_op(wrong_elem) == right_ans_m1(wrong_elem)

    # Arreglo de posibles errores a probar
    # función para realizar el test haciendo uso de número random

    right_list = [0, 3, 8]
    right_elem = right_list[random.randrange(0, 2)]
    assert Metodos.multiple_op(right_elem) == right_ans_m1(right_elem)


def test_verify_array_op():
    # función para realizar el test haciendo uso de número random
    wrong_array_array = [[1, "a", 5], [4, 0.2, -5]]
    # Arreglo de posibles errores a probar
    wrong_elem = wrong_array_array[random.randrange(0, 1)]
    # a
    assert Metodos.verify_array_op(wrong_elem) == right_ans_m2(wrong_elem)

    right_array_array = [[0, 2, 5], [4, 2, 5]]
    right_elem = right_array_array[random.randrange(0, 1)]
    assert Metodos.verify_array_op(right_elem) == right_ans_m2(right_elem)
