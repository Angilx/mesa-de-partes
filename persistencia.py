"""Lectura y escritura de trámites en un archivo CSV."""

import csv
import os

from validaciones import validar_dni, validar_estado

RUTA_POR_DEFECTO = os.path.join("data", "tramites.csv")
CAMPOS = ["codigo", "dni", "nombre", "tipo", "estado"]


def guardar_tramites(tramites, ruta=RUTA_POR_DEFECTO):
    """Guarda la lista de trámites en un archivo CSV."""
    carpeta = os.path.dirname(ruta)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        for t in tramites:
            escritor.writerow(t)


def cargar_tramites(ruta=RUTA_POR_DEFECTO):
    """Carga los trámites desde el CSV. Si no existe, devuelve una lista vacía.

    Las filas con DNI o estado inválidos se omiten para no cargar datos corruptos.
    """
    tramites = []
    if not os.path.exists(ruta):
        return tramites
    with open(ruta, newline="", encoding="utf-8-sig") as archivo:
        for fila in csv.DictReader(archivo):
            if validar_dni(fila.get("dni", "")) and validar_estado(fila.get("estado", "")):
                tramites.append({campo: fila[campo] for campo in CAMPOS})
    return tramites
