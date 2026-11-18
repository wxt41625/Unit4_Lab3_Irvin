"""Validador sencillo de correos - Irvin Misael Mejía Hernández.
Actividad U4ACT03: DevOps con Python y GitHub Actions.
"""


def es_correo_valido(correo):
    """Acepta una sola @, usuario no vacío y un punto en el dominio."""
    if not isinstance(correo, str) or correo.count("@") != 1:
        return False

    usuario, dominio = correo.split("@", 1)
    if usuario == "" or "." not in dominio:
        return False
    return True
