# Mesa de Partes

Sistema de consola en Python para registrar y dar seguimiento a trámites de estudiantes
(matrícula, solicitud de notas, registro de estudiante). Migrado desde un pseudocódigo en PSeInt
(`docs/MesaDePartes_base.psc`).

## Requisitos
- Python 3.8 o superior (no necesita librerías externas)

## Uso
```
python main.py
```
Los trámites se guardan automáticamente en `data/tramites.csv`.

## Pruebas
```
python -m unittest discover -s tests -v
```

## Estructura
| Archivo | Contenido |
|---|---|
| `main.py` | Menú e interacción con el usuario |
| `tramites.py` | Lógica: registrar, buscar, cambiar estado, estadísticas |
| `validaciones.py` | Validación de DNI, campos y estados |
| `persistencia.py` | Guardado y carga en CSV |
| `tests/` | Pruebas automáticas |
| `docs/diseno.md` | Etapa 4: diagramas, pseudocódigo y módulos |
| `docs/pruebas_y_reflexion.md` | Etapa 6: pruebas y reflexión |
