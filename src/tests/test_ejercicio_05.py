import pytest

from src.ejercicio_05 import es_mayor_de_edad


def test_17_anios_no_es_mayor():
    # Arrange
    edad = 17
    # Act
    resultado = es_mayor_de_edad(edad)
    # Assert
    assert resultado is False


def test_18_anios_frontera_es_mayor():
    # Arrange
    edad = 18
    # Act
    resultado = es_mayor_de_edad(edad)
    # Assert
    assert resultado is True


def test_19_anios_es_mayor():
    # Arrange
    edad = 19
    # Act
    resultado = es_mayor_de_edad(edad)
    # Assert
    assert resultado is True


def test_edad_negativa_lanza_value_error():
    # Arrange
    edad = -1
    # Act & Assert
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad)


def test_edad_126_lanza_value_error():
    # Arrange
    edad = 126
    # Act & Assert
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad)
