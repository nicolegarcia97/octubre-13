import pytest

from src.ejercicio_09 import es_palindromo


def test_palindromo_simple():
    # Arrange
    cadena = "radar"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is True


def test_palindromo_frase_con_espacios_y_mayusculas():
    # Arrange
    cadena = "Anita lava la tina"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is True


def test_no_palindromo():
    # Arrange
    cadena = "software"
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is False


def test_cadena_solo_espacios_retorna_false():
    # Arrange
    cadena = "   "
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is False


def test_cadena_vacia_retorna_false():
    # Arrange
    cadena = ""
    # Act
    resultado = es_palindromo(cadena)
    # Assert
    assert resultado is False


def test_numero_lanza_type_error():
    # Arrange
    cadena = 1001
    # Act & Assert
    with pytest.raises(TypeError):
        es_palindromo(cadena)
