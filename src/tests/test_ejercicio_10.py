import pytest

from src.ejercicio_10 import clasificar_nota


def test_limite_superior_excelente():
    # Arrange
    nota = 5.0
    esperado = "Excelente"
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == esperado


def test_borde_inferior_excelente():
    # Arrange
    nota = 4.5
    esperado = "Excelente"
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == esperado


def test_borde_superior_bueno():
    # Arrange
    nota = 4.4
    esperado = "Bueno"
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == esperado


def test_borde_inferior_aceptable():
    # Arrange
    nota = 3.0
    esperado = "Aceptable"
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == esperado


def test_borde_reprobatorio_deficiente():
    # Arrange
    nota = 2.9
    esperado = "Deficiente"
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == esperado


def test_limite_inferior_absoluto_deficiente():
    # Arrange
    nota = 0.0
    esperado = "Deficiente"
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == esperado


@pytest.mark.parametrize("nota_invalida", [-0.1, 5.1])
def test_nota_fuera_de_escala_lanza_value_error(nota_invalida):
    # Arrange
    nota = nota_invalida
    # Act & Assert
    with pytest.raises(ValueError, match="Nota fuera de la escala"):
        clasificar_nota(nota)
