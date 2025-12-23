# ------------------------------------------------------------
# Archivo: tarea_1_example_solution.py
#
# Este archivo contiene la implementación de los métodos
# solicitados en la tarea para ser evaluados mediante pytest.
# Ambos métodos retornan SIEMPRE una tupla:
# (codigo_estado, resultado)
# ------------------------------------------------------------


def operation_selector(num1, num2, op):
    # Método que selecciona y ejecuta una operación matemática
    # entre dos números enteros según el operador recibido.

    # num1: primer número entero de entrada
    # num2: segundo número entero de entrada
    # op: operador en forma de string ("+", "-", "*", "&")

    # Inicialización del resultado (None en caso de error)
    resultado = None

    # --------------------------------------------------------
    # Validación 1: num1 debe ser entero y NO booleano
    # --------------------------------------------------------
    # En Python, bool hereda de int, por lo que se valida
    # explícitamente que no sea True o False
    if not isinstance(num1, int) or isinstance(num1, bool):
        return -50, resultado

    # --------------------------------------------------------
    # Validación 2: num2 debe ser entero y NO booleano
    # --------------------------------------------------------
    if not isinstance(num2, int) or isinstance(num2, bool):
        return -50, resultado

    # --------------------------------------------------------
    # Validación 3: el operador debe ser un string
    # --------------------------------------------------------
    if not isinstance(op, str):
        return -60, resultado

    # --------------------------------------------------------
    # Validación 4: el operador debe ser uno permitido
    # --------------------------------------------------------
    if op not in ["+", "-", "*", "&"]:
        return -70, resultado

    # --------------------------------------------------------
    # Ejecución de la operación según el operador recibido
    # --------------------------------------------------------
    if op == "+":
        # Suma de los dos operandos
        resultado = num1 + num2
    elif op == "-":
        # Resta de los dos operandos
        resultado = num1 - num2
    elif op == "*":
        # Multiplicación de los dos operandos
        resultado = num1 * num2
    else:
        # Operación AND bit a bit entre enteros
        resultado = num1 & num2

    # Retorno exitoso con código 0 y el resultado calculado
    return 0, resultado


def calculo_promedio(lista_valores):
    # Método que calcula el promedio aritmético de una lista
    # de valores numéricos.

    # lista_valores: lista de números (int o float)
    # True y False no son considerados valores numéricos válidos

    # Inicialización del resultado (None en caso de error)
    resultado = None

    # --------------------------------------------------------
    # Validación 1: la lista no puede tener más de 10 elementos
    # --------------------------------------------------------
    if len(lista_valores) > 10:
        return -90, resultado

    # --------------------------------------------------------
    # Validación 2: todos los elementos deben ser numéricos
    # --------------------------------------------------------
    for valor in lista_valores:
        # Verifica que el elemento sea int o float
        if not isinstance(valor, (int, float)):
            return -80, resultado

        # Verifica explícitamente que no sea booleano
        if isinstance(valor, bool):
            return -80, resultado

    # --------------------------------------------------------
    # Cálculo del promedio aritmético
    # --------------------------------------------------------
    resultado = sum(lista_valores) / len(lista_valores)

    # Retorno exitoso con código 0 y el promedio calculado
    return 0, resultado

