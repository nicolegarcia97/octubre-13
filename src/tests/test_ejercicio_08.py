import pytest

from src.ejercicio_08 import obtener_mayor


def test_mayor_enteros_positivos_desordenados():
    # Arrange
    lista = [4, 12, 8, 3]
    esperado = 12
    # Act
    resultado = obtener_mayor(lista)
    # Assert
    assert resultado == esperado


def test_mayor_con_negativos():
    # Arrange
    lista = [-15, -3, -8, -20]
    esperado = -3
    # Act
    resultado = obtener_mayor(lista)
    # Assert
    assert resultado == esperado


def test_mayor_un_solo_elemento():
    # Arrange
    lista = [42]
    esperado = 42
    # Act
    resultado = obtener_mayor(lista)
    # Assert
    assert resultado == esperado


def test_lista_vacia_lanza_value_error():
    # Arrange
    lista = []
    # Act & Assert
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        obtener_mayor(lista)


def test_elemento_no_numerico_lanza_type_error():
    # Arrange
    lista = [1, 2, "tres"]
    # Act & Assert
    with pytest.raises(TypeError):
        obtener_mayor(lista)
