"""
test_errores_corregidos.py

Propósito:
- Este archivo muestra el MISMO caso del archivo test_errores.py, pero
  corregido para cumplir con PEP8.
- Sirve como evidencia de que se pueden corregir los errores detectados por flake8.

Correcciones aplicadas:
- Se evita la línea demasiado larga (E501) dividiendo el string en varias líneas.
- Se utiliza una tupla de strings dentro de paréntesis para que Python los concatene.
"""


def suma(a, b):
    """
    Suma dos números e imprime un mensaje.

    Parámetros:
    - a: número (int/float)
    - b: número (int/float)

    Retorna:
    - resultado de a + b

    Nota:
    - El mensaje fue dividido en varias líneas para cumplir con el límite
      de longitud recomendado por PEP8 (evita E501).
    """
    # Mensaje dividido en varias líneas (Python concatena strings contiguos en paréntesis)
    mensaje = (
        "Esta es una línea larga, pero ahora está correctamente "
        "dividida para cumplir con el límite de caracteres de PEP 8."
    )

    # Cálculo de la suma
    resultado = a + b

    # Impresión del mensaje (solo para mostrar uso de la variable)
    print(mensaje)

    # Retorno del resultado final
    return resultado

