import pytest

from src.ejercicio_11 import division_segura


def test_division_exacta():
    # Arrange
    dividendo, divisor = 10, 2
    esperado = 5.0
    # Act
    resultado = division_segura(dividendo, divisor)
    # Assert
    assert resultado == esperado


def test_division_periodica_con_approx():
    # Arrange
    dividendo, divisor = 10, 3
    esperado = 3.3333333333
    # Act
    resultado = division_segura(dividendo, divisor)
    # Assert
    assert resultado == pytest.approx(esperado)


def test_cero_en_el_dividendo():
    # Arrange
    dividendo, divisor = 0, 5
    esperado = 0.0
    # Act
    resultado = division_segura(dividendo, divisor)
    # Assert
    assert resultado == esperado


def test_division_por_cero_lanza_zero_division_error():
    # Arrange
    dividendo, divisor = 8, 0
    # Act & Assert
    with pytest.raises(ZeroDivisionError, match="No es posible dividir entre cero"):
        division_segura(dividendo, divisor)
