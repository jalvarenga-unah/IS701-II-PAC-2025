

def suma(a, b):
    """
    Suma dos números y devuelve el resultado.

    :param a: Primer número
    :param b: Segundo número
    :return: Suma de a y b
    """
    return a + b


def resta(a, b):
    """
    Resta dos números y devuelve el resultado.

    :param a: Primer número
    :param b: Segundo número
    :return: Resta de a y b
    """
    return a - b


def multiplicacion(a, b):
    """
    Multiplica dos números y devuelve el resultado.

    :param a: Primer número
    :param b: Segundo número
    :return: Producto de a y b
    """
    return a * b


def division(a, b):
    """
    Divide dos números y devuelve el resultado.
    :param a: Numerador
    :param b: Denominador
    :return: Cociente de a y b
    :raises ZeroDivisionError: Si b es cero
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


if __name__ == "__main__":
    print(__name__)
    print(suma(2, 3))  # Ejemplo de uso de la función suma

    print(multiplicacion(4, 5))  # Ejemplo de uso de la función multiplicacion
