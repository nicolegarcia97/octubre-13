import pytest

from src.ejercicio_06 import validar_longitud_password


def test_longitud_7_es_invalida():
    # Arrange
    password = "a" * 7
    # Act
    resultado = validar_longitud_password(password)
    # Assert
    assert resultado is False


def test_longitud_8_es_valida():
    # Arrange
    password = "a" * 8
    # Act
    resultado = validar_longitud_password(password)
    # Assert
    assert resultado is True


def test_longitud_20_es_valida():
    # Arrange
    password = "a" * 20
    # Act
    resultado = validar_longitud_password(password)
    # Assert
    assert resultado is True


def test_longitud_21_es_invalida():
    # Arrange
    password = "a" * 21
    # Act
    resultado = validar_longitud_password(password)
    # Assert
    assert resultado is False


def test_none_lanza_type_error():
    # Arrange
    password = None
    # Act & Assert
    with pytest.raises(TypeError):
        validar_longitud_password(password)


def test_numero_lanza_type_error():
    # Arrange
    password = 12345678
    # Act & Assert
    with pytest.raises(TypeError):
        validar_longitud_password(password)
