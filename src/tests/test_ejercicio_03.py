import pytest

from src.ejercicio_03 import celsius_a_fahrenheit


def test_punto_congelacion():
    # Arrange
    celsius = 0
    esperado = 32.0
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == pytest.approx(esperado)


def test_punto_ebullicion():
    # Arrange
    celsius = 100
    esperado = 212.0
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == pytest.approx(esperado)


def test_coincidencia_de_escalas():
    # Arrange
    celsius = -40
    esperado = -40.0
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == pytest.approx(esperado)


def test_precision_decimal_temperatura_corporal():
    # Arrange
    celsius = 37
    esperado = 98.6
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == pytest.approx(esperado, rel=1e-3)


def test_bajo_cero_absoluto_lanza_value_error():
    # Arrange
    celsius = -273.16
    # Act & Assert
    with pytest.raises(ValueError):
        celsius_a_fahrenheit(celsius)
