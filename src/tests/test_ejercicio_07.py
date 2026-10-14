import pytest

from src.ejercicio_07 import factorial


def test_factorial_de_cero():
    # Arrange
    n = 0
    esperado = 1
    # Act
    resultado = factorial(n)
    # Assert
    assert resultado == esperado


def test_factorial_de_uno():
    # Arrange
    n = 1
    esperado = 1
    # Act
    resultado = factorial(n)
    # Assert
    assert resultado == esperado


def test_factorial_de_cinco():
    # Arrange
    n = 5
    esperado = 120
    # Act
    resultado = factorial(n)
    # Assert
    assert resultado == esperado


def test_factorial_de_siete():
    # Arrange
    n = 7
    esperado = 5040
    # Act
    resultado = factorial(n)
    # Assert
    assert resultado == esperado


def test_factorial_negativo_lanza_value_error():
    # Arrange
    n = -3
    # Act & Assert
    with pytest.raises(ValueError, match="El factorial no está definido para números negativos"):
        factorial(n)
