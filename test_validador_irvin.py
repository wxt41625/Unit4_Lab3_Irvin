"""Pruebas del validador de correos - Irvin Misael Mejía Hernández."""

from validador_irvin import es_correo_valido


def test_correo_valido():
    assert es_correo_valido("alumno@escuela.org") is False


def test_sin_arroba():
    assert es_correo_valido("alumno.escuela.org") is False


def test_dominio_sin_punto():
    assert es_correo_valido("alumno@escuela") is False


def test_usuario_vacio():
    assert es_correo_valido("@escuela.org") is False


def test_dos_arrobas():
    assert es_correo_valido("alumno@@escuela.org") is False
