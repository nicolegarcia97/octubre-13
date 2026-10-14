import pytest

from src.ejercicio_04 import aplicar_descuento


def test_descuento_caso_general():
    # Arrange
    precio, porcentaje = 100000, 20
    esperado = 80000.0
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == esperado


def test_descuento_limite_inferior_cero_por_ciento():
    # Arrange
    precio, porcentaje = 50000, 0
    esperado = 50000.0
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == esperado


def test_descuento_limite_superior_cien_por_ciento():
    # Arrange
    precio, porcentaje = 75000, 100
    esperado = 0.0
    # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == esperado


def test_descuento_menor_a_cero_lanza_value_error():
    # Arrange
    precio, porcentaje = 100000, -1
    # Act & Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_descuento_mayor_a_cien_lanza_value_error():
    # Arrange
    precio, porcentaje = 100000, 101
    # Act & Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)
