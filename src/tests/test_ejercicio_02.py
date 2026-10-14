import pytest

from src.ejercicio_02 import es_par


def test_par_positivo():
    # Arrange
    numero = 8
    # Act
    resultado = es_par(numero)
    # Assert
    assert resultado is True


def test_impar_positivo():
    # Arrange
    numero = 7
    # Act
    resultado = es_par(numero)
    # Assert
    assert resultado is False


def test_cero_es_par():
    # Arrange
    numero = 0
    # Act
    resultado = es_par(numero)
    # Assert
    assert resultado is True


def test_negativo_par():
    # Arrange
    numero = -4
    # Act
    resultado = es_par(numero)
    # Assert
    assert resultado is True


def test_negativo_impar():
    # Arrange
    numero = -9
    # Act
    resultado = es_par(numero)
    # Assert
    assert resultado is False


def test_decimal_lanza_type_error():
    # Arrange
    numero = 4.0
    # Act & Assert
    with pytest.raises(TypeError):
        es_par(numero)
