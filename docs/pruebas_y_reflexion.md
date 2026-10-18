# Etapa 6: Pruebas con datos reales y reflexión

## 1. Pruebas automáticas (ya ejecutadas)

Comando: `python -m unittest discover -s tests -v`

Resultado: **20 pruebas ejecutadas, 20 correctas, 0 fallos.**

Cubren: validación de DNI (longitud, letras, símbolos, espacios), campos vacíos, tipos y estados
inválidos, códigos consecutivos, búsqueda (con mayúsculas/espacios), cambio de estado,
estadísticas con lista vacía y con datos, y guardado/carga del CSV (incluye nombres con
tildes, ñ y comas, y filas corruptas).

## 2. Pruebas con datos reales de la observación de campo

> **COMPLETAR:** reemplaza las filas de ejemplo con los datos que recogiste en tu observación
> de campo (trámites reales de una mesa de partes, sin usar DNI verdaderos de personas: usa
> números ficticios de 8 dígitos o anonimízalos).

| N.º | Dato observado (entrada) | Resultado esperado | Resultado obtenido | ¿Correcto? |
|---|---|---|---|---|
| 1 | *(ej.)* DNI `12345678`, "Ana Pérez", Matrícula | Se registra con código TR-1, estado Recibido | | |
| 2 | *(ej.)* DNI de 7 dígitos | "Datos inválidos" | | |
| 3 | *(ej.)* Código inexistente en búsqueda | "Código no existe" | | |
| 4 | | | | |
| 5 | | | | |

### Errores detectados y corregidos

Durante la migración de PSeInt a Python se detectaron y corrigieron estos puntos del algoritmo
original:

| # | Error en el original | Corrección en Python |
|---|---|---|
| 1 | Una opción de tipo inválida (ej. 9) se registraba como "Registro de estudiante" | Se rechaza y muestra "Datos inválidos" |
| 2 | `cambiar_estado` aceptaba cualquier texto, y las estadísticas no lo contaban | Solo se aceptan los 3 estados definidos |
| 3 | Los datos se perdían al cerrar el programa | Se guardan en `data/tramites.csv` |
| 4 | Máximo 100 trámites (arreglos de tamaño fijo) | Lista dinámica |
| 5 | Un nombre con solo espacios pasaba como "completo" | Se usa `strip()` antes de validar |

> **COMPLETAR:** agrega aquí los errores que encuentres tú al probar con tus datos reales.

## 3. Reflexión técnica y ética

> **COMPLETAR con tus propias palabras.** Preguntas guía:

**Reflexión técnica**
- ¿Qué fue lo más difícil al pasar el algoritmo de PSeInt a Python?
- ¿Qué ventaja tuvo separar el código en módulos? ¿Qué prueba pudiste hacer gracias a eso?
- ¿Qué limitaciones tiene la solución actual (por ejemplo, un archivo CSV en lugar de una base
  de datos, un solo usuario a la vez, códigos que dependen de la cantidad de trámites)?

**Reflexión ética**
- El sistema guarda DNI y nombres de estudiantes: ¿quién debería tener acceso al archivo?
  ¿Cómo se protegen estos datos personales? (Considera la Ley N.º 29733, de Protección de
  Datos Personales del Perú.)
- ¿Qué pasa con una persona que no tiene DNI peruano (extranjeros, menores)? ¿El sistema la excluye?
- ¿Qué riesgos hay si se modifica un estado por error o sin autorización? ¿Debería haber un registro de quién hizo el cambio?

**Conocimiento nuevo que incorporé**
- *(escribe aquí qué aprendiste: listas y diccionarios, archivos CSV, Git, pruebas
  automáticas, etc.)*
