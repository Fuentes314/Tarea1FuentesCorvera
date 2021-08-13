import Metodos
from math import factorial
import random
# Importar el archivo .py Metodos
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
        # En caso de no cumplir retorna un código de error


def right_ans_m2(arreglo):
    # Fución para determinar la respuesta correcta del método 2 (Array)
    # Y comparar con el assert
    resultados_metodo_2 = []
    # Arreglo vacío para almacenar los resultados
    largo = len(arreglo)
    i = 0
    while i < largo:
        # ciclo que recorre cada elemento del arreglo
        # y llama a la funcion uno enviandolo el dato del arreglo

        if isinstance(arreglo[i], int) and arreglo[i] >= 0:
        # Comprueba que los elementos del array sean todos enteros positivos
            resultados_metodo_2.append(right_ans_m1(arreglo[i]))
        else:
        # En caso contrario devuelve un código de error único
            return "Código de error 3141."
        i += 1
    return resultados_metodo_2
    # Da el array resultados_metodo_2 completo y con las respuestas
    # correctas

def test_multiple_op():
    # Función para realizar el test del método 1
    wrong_array = [-1, "a", 0.2, -5.99, "palabra"]
    # Se crea un array con respuestas incorrectas que se pueden seleccionar
    wrong_elem = wrong_array[random.randrange(0, 4)]
    # Se selecciona un elemento del array de manera aleatoria
    assert Metodos.multiple_op(wrong_elem) == right_ans_m1(wrong_elem)
    # Se comprueba con el assert si la respuesta del elemento seleccionado
    # al azar del array es correcta, en caso de ingresar un parámetro
    # inválido se va a brindar el código de error correspondiente

    right_list = [0, 3, 8]
    # Arreglo con varios elementos correctos para la prueba
    right_elem = right_list[random.randrange(0, 2)]
    # Se selecciona un elemento del array de manera aleatoria
    # para evaluar
    assert Metodos.multiple_op(right_elem) == right_ans_m1(right_elem)
    # Se comprueba con el assert si la respuesta del elemento seleccionado
    # al azar del array es correcta

def test_verify_array_op():
    # función para realizar el test en el array haciendo uso de número random
    wrong_array_array = [[1, "a", 5], [4, 0.2, -5]]
    # Arreglo de posibles errores a probar
    wrong_elem = wrong_array_array[random.randrange(0, 1)]
    # Se selecciona uno de los arreglos del arreglo para evaluar
    assert Metodos.verify_array_op(wrong_elem) == right_ans_m2(wrong_elem)
    # Se comprueba con el assert si la respuesta del arreglo seleccionado
    # al azar del array es correcta, pero como es el caso negativo se debe
    # de brindar el código de error único sin problemas
    right_array_array = [[0, 2, 5], [4, 2, 5]]
    # Arreglo de arreglos válidos para evaluar
    right_elem = right_array_array[random.randrange(0, 1)]
    # Se selecciona un arreglo del array de manera aleatoria que
    # que se va a evaluar
    assert Metodos.verify_array_op(right_elem) == right_ans_m2(right_elem)
    # Se comprueba con el assert si la respuesta del arreglo seleccionado
    # al azar del array es correcta
    