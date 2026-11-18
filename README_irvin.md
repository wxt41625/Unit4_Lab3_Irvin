# Unit4_Lab4_Irvin — DevOps con Python y GitHub Actions

**Estudiante:** Irvin Misael Mejía Hernández  
**Fecha:** 17 de noviembre de 2026  
**Actividad:** U4ACT03 Fundamentos de DevOps con Python y GitHub Actions

## Archivos del proyecto

- `validador_irvin.py`: función `es_correo_valido`.
- `test_validador_irvin.py`: cinco pruebas automáticas (`pytest`).
- `requirements_irvin.txt`: dependencia de pytest.
- `.github/workflows/ci_irvin.yml`: CI/CD automática sobre la rama `main`.

## Ejecutar pruebas en GNU/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements_irvin.txt
python -m pytest -v test_validador_irvin.py
```

**No incluir** `.venv/`, `__pycache__/` ni `.pytest_cache/` al subir cambios.

## Ciclo de evidencia requerido

1. Primera ejecución correcta: `test` = success, `deploy` = success.
2. Fallo provocado: sustituir la aserción de `test_correo_valido` para esperar `False`; hacer commit y push a `main`. El job `test` debe fallar y `deploy` debe omitirse.
3. Corrección: restaurar la aserción para esperar `True`; hacer commit y push. Deben quedar los dos jobs en verde.

El job `deploy` es una simulación: no conecta a servidores reales ni requiere credenciales.
