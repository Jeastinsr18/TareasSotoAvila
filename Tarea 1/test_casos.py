"""
test_casos.py

Archivo de pruebas unitarias con pytest.

Objetivo:
- Verificar el comportamiento de las funciones definidas en tarea_1_example_solution.py
- Confirmar que:
  1) Los códigos de error son los esperados
  2) El resultado es None en caso de error
  3) En caso de éxito, el resultado coincide con el cálculo esperado

Nota:
- Se usan valores aleatorios en algunas pruebas para evitar "hardcodear" datos
  y comprobar que la función funciona con distintos valores.
"""

import random
import string

import tarea_1_example_solution

# ------------------------------------------------------------
# Códigos de retorno esperados por especificación
# ------------------------------------------------------------
# Caso de éxito => 0
#
# operation_selector:
# -50 => num1 o num2 no son enteros (y bool no se acepta como entero)
# -60 => op no es string
# -70 => op es string, pero no es uno de: +, -, *, &
#
# calculo_promedio:
# -80 => existe un elemento no numérico (incluye bool o strings)
# -90 => la lista tiene más de 10 elementos
# ------------------------------------------------------------


def test_casos_error_operation_selector():
    """
    Prueba 1:
    Verifica TODOS los casos de error esperados para operation_selector.
    La idea es forzar entradas inválidas y confirmar que:
      - el código de error es el correcto
      - el resultado es None
    """

    # ---- Caso error -50: num1/num2 no enteros ----
    estado, res1 = tarea_1_example_solution.operation_selector(7, 7.1, "+")
    assert estado == -50
    assert res1 is None

    estado, res1 = tarea_1_example_solution.operation_selector(12, "s", "*")
    assert estado == -50
    assert res1 is None

    # bool no se considera válido aunque en Python sea subclase de int
    estado, res1 = tarea_1_example_solution.operation_selector(True, 7, "-")
    assert estado == -50
    assert res1 is None

    estado, res1 = tarea_1_example_solution.operation_selector(None, 77, "&")
    assert estado == -50
    assert res1 is None

    # ---- Caso error -60: op no es string ----
    # op entero
    estado, res1 = tarea_1_example_solution.operation_selector(10, 10, 3)
    assert estado == -60
    assert res1 is None

    # op float
    estado, res1 = tarea_1_example_solution.operation_selector(10, 10, 3.7)
    assert estado == -60
    assert res1 is None

    # op bool
    estado, res1 = tarea_1_example_solution.operation_selector(10, 10, True)
    assert estado == -60
    assert res1 is None

    # ---- Caso error -70: op string, pero inválido ----
    # Se genera una letra aleatoria para garantizar que no sea uno de los operadores válidos
    random_letter = random.choice(string.ascii_letters)
    estado, res1 = tarea_1_example_solution.operation_selector(10, 10, random_letter)
    assert estado == -70
    assert res1 is None


def test_casos_exito_operation_selector():
    """
    Prueba 2:
    Verifica casos de éxito de operation_selector con entradas válidas.
    Se usan valores aleatorios para probar múltiples combinaciones.
    Se valida que:
      - el estado sea 0
      - el resultado coincida con la operación esperada
    """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # ---- Suma ----
    res_esperado = num1 + num2
    estado, res1 = tarea_1_example_solution.operation_selector(num1, num2, "+")
    assert estado == 0
    assert res1 == res_esperado

    # ---- Resta ----
    res_esperado = num1 - num2
    estado, res1 = tarea_1_example_solution.operation_selector(num1, num2, "-")
    assert estado == 0
    assert res1 == res_esperado

    # ---- Multiplicación ----
    res_esperado = num1 * num2
    estado, res1 = tarea_1_example_solution.operation_selector(num1, num2, "*")
    assert estado == 0
    assert res1 == res_esperado

    # ---- AND bit a bit ----
    res_esperado = num1 & num2
    estado, res1 = tarea_1_example_solution.operation_selector(num1, num2, "&")
    assert estado == 0
    assert res1 == res_esperado


def test_casos_error_calculo_promedio():
    """
    Prueba 3:
    Verifica los casos de error esperados para calculo_promedio.
    Casos:
      -80 si hay un elemento no numérico (string/bool/etc.)
      -90 si la lista tiene más de 10 elementos
    """

    # ---- Caso error -80: elemento no numérico (string) ----
    estado, result = tarea_1_example_solution.calculo_promedio([1, 2, 3, "4"])
    assert estado == -80
    assert result is None

    # ---- Caso error -80: elemento booleano no permitido ----
    estado, result = tarea_1_example_solution.calculo_promedio([1, True, 3, 4])
    assert estado == -80
    assert result is None

    # ---- Caso error -90: tamaño de lista > 10 ----
    estado, result = tarea_1_example_solution.calculo_promedio(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    )
    assert estado == -90
    assert result is None


def test_casos_calculo_promedio():
    """
    Prueba 4:
    Verifica caso de éxito de calculo_promedio.
    Se construye una lista de 10 elementos (máximo permitido).
    Se calcula el promedio esperado y se compara con el resultado del método.
    """
    lista_valores = []

    # Genera 10 números aleatorios (incluye negativos)
    for _ in range(10):
        lista_valores.append(random.randint(-100, 100))

    # Promedio esperado calculado directamente
    promedio = sum(lista_valores) / len(lista_valores)

    # Llamada al método bajo prueba
    estado, result = tarea_1_example_solution.calculo_promedio(lista_valores)

    # Validación de éxito
    assert estado == 0
    assert result == promedio

