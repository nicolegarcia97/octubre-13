import pytest

from src.ejercicio_12 import procesar_usuario


def test_usuario_valido_retorna_registro_validado():
    # Arrange
    datos = {"id": 1, "nombre": "Nicole", "activo": True}
    esperado = {"id": 1, "nombre": "Nicole", "activo": True, "estado_registro": "VALIDADO"}
    # Act
    resultado = procesar_usuario(datos)
    # Assert
    assert resultado == esperado


def test_clave_faltante_lanza_value_error():
    # Arrange
    datos = {"id": 1, "nombre": "Nicole"}  # falta "activo"
    # Act & Assert
    with pytest.raises(ValueError, match="Faltan campos requeridos"):
        procesar_usuario(datos)


@pytest.mark.parametrize("id_invalido", [0, -5])
def test_id_invalido_lanza_value_error(id_invalido):
    # Arrange
    datos = {"id": id_invalido, "nombre": "Nicole", "activo": True}
    # Act & Assert
    with pytest.raises(ValueError, match="El id debe ser un entero positivo"):
        procesar_usuario(datos)


@pytest.mark.parametrize("nombre_invalido", ["", "   "])
def test_nombre_vacio_o_espacios_lanza_value_error(nombre_invalido):
    # Arrange
    datos = {"id": 1, "nombre": nombre_invalido, "activo": True}
    # Act & Assert
    with pytest.raises(ValueError, match="El nombre debe ser una cadena no vacía"):
        procesar_usuario(datos)


def test_argumento_no_diccionario_lanza_type_error():
    # Arrange
    datos = [1, "Nicole", True]
    # Act & Assert
    with pytest.raises(TypeError):
        procesar_usuario(datos)


def test_no_modifica_el_diccionario_original():
    # Arrange
    datos = {"id": 1, "nombre": "Nicole", "activo": False}
    # Act
    procesar_usuario(datos)
    # Assert
    assert "estado_registro" not in datos
