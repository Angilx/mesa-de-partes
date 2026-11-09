# Etapa 6: Pruebas con datos reales y reflexión

## 1. Pruebas automáticas (ya ejecutadas)

Comando: `python -m unittest discover -s tests -v`

Resultado: **20 pruebas ejecutadas, 20 correctas, 0 fallos.**

Cubren: validación de DNI (longitud, letras, símbolos, espacios), campos vacíos, tipos y estados
inválidos, códigos consecutivos, búsqueda (con mayúsculas/espacios), cambio de estado,
estadísticas con lista vacía y con datos, y guardado/carga del CSV (incluye nombres con
tildes, ñ y comas, y filas corruptas).

## 2. Pruebas con datos reales de la observación de campo

| N.º | Dato observado (entrada) | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| 1 | DNI : ( 64821001 ) , "Ana Pérez", Matrículado | Se registra con código TR-01, estado Recibido | "Recibido" |
| 2 | DNI de 7 dígitos | "Datos inválidos" | "Datos invalidos" |
| 3 | Código inexistente en búsqueda:(TR-99) | "Código no existe" | "Codigo no existe" |
| 4 | DNI : ( 63711047 ) , "Piero Huaman", Mariculado | Código: TR-2 y estado Recibido en la lista | Recibido |
| 5 | Código: TR-1, Nuevo estado:Entregado | Mensaje: "Estado actualizado" | TR-1 ... Entregado . |

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


## 3. Reflexión técnica y ética

**Reflexión técnica**

 - ¿Qué fue lo más difícil o lo que aprendí?

   -Pasar de 5 arreglos separados a una lista de diccionarios.

   -Trabajar con varios archivos (módulos) y hacer que se importen     entre  sí.

 - ¿Qué ventaja tuvo separar el código en módulos?

   -Cada archivo tiene una sola responsabilidad (validar, guardar, mostrar menú).

   -Poder probar la lógica sin escribir datos a mano, con las pruebas automáticas.
   
   -Si hay un error de DNI, sé que debo buscarlo en (validaciones.py).

**Reflexión ética**

 * Al diseñar este sistema se tuvo presente que detrás de cada fila de tramites.csv hay una persona que espera un trámite importante para ella. Por eso se buscó que el programa fuera cuidadoso desde el inicio. Se guardaron solo los datos necesarios (código, DNI, nombre, tipo y estado), de modo que cada estudiante entrega lo mínimo para ser atendido. Se incluyeron validaciones para evitar que se registren datos incorrectos, y los trámites quedan guardados en el archivo, por lo que ninguno se pierde al cerrar el programa y cada estudiante puede consultar el estado del suyo con su código. 
 

**Conocimiento nuevo que incorporé**

 * Con este proyecto se aprendió a trasladar un algoritmo de PSeInt a Python y a organizarlo en módulos, donde cada archivo cumple una función clara. Se incorporó el uso de listas y diccionarios para que cada trámite conserve sus datos juntos, y el trabajo con archivos CSV para que la información no se pierda al cerrar el programa. También se aprendió a validar datos y a escribir pruebas automáticas, que permiten comprobar que el sistema funciona y detectar errores a tiempo. Finalmente, con Git y GitHub se aprendió a registrar el avance mediante commits, de modo que el historial muestra el camino recorrido desde un algoritmo inicial hasta un proyecto completo y verificable. 
