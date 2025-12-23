"""
test_errores.py

Propósito:
- Este archivo existe como EJEMPLO de código con errores de estilo (PEP8),
  para que flake8 los detecte.
- Sirve como evidencia de que flake8 está funcionando correctamente.

Errores de estilo intencionales en este archivo:
- Línea demasiado larga (E501): excede el límite recomendado (79 caracteres).
- Espacios incorrectos en la definición de funciones y asignaciones (E231/E225).
- Import no utilizado (F401) si se corre flake8 sobre este archivo.
"""

import math  # Import intencionalmente innecesario para demostrar F401 (unused import)


def suma(a, b):
    """
    Suma dos números.

    Parámetros:
    - a: número (int/float)
    - b: número (int/float)

    Retorna:
    - resultado de a + b

    Nota:
    - Esta función en sí es simple; el objetivo del archivo es mostrar
      cómo flake8 detecta problemas de estilo en el código.
    """
    # Asignación del resultado de la suma
    resultado = a + b

    # Línea intencionalmente MUY larga para disparar E501 en flake8:
    # (Esto demuestra que flake8 detecta límites de longitud de línea)
    mensaje = "Esta es una línea extremadamente larga que viola claramente el límite de setenta y nueve caracteres definido por la guía PEP8"

    # Retorna el resultado (mensaje no se usa, a propósito, para mantener el ejemplo)
    return resultado

