"""Lógica de negocio de la Mesa de Partes (sin entrada/salida por consola)."""

from validaciones import validar_dni, campos_completos, validar_estado, ESTADOS_VALIDOS

TIPOS_TRAMITE = {
    1: "Matrícula",
    2: "Solicitud de notas",
    3: "Registro de estudiante",
}


def nombre_tipo(op):
    """Devuelve el nombre del tipo de trámite, o "" si la opción no existe."""
    return TIPOS_TRAMITE.get(op, "")


def generar_codigo(n):
    """Genera el código del trámite número n, por ejemplo TR-1."""
    return "TR-" + str(n)


def siguiente_numero(tramites):
    """Devuelve el próximo número de código (el mayor existente + 1)."""
    mayor = 0
    for t in tramites:
        try:
            mayor = max(mayor, int(t["codigo"].split("-")[1]))
        except (IndexError, ValueError):
            pass
    return mayor + 1


def registrar_tramite(tramites, dni, nombre, op):
    """Registra un trámite nuevo.

    Devuelve el código generado, o None si los datos son inválidos.
    """
    tipo = nombre_tipo(op)
    if validar_dni(dni) and campos_completos(nombre, tipo):
        codigo = generar_codigo(siguiente_numero(tramites))
        tramites.append({
            "codigo": codigo,
            "dni": dni,
            "nombre": nombre.strip(),
            "tipo": tipo,
            "estado": "Recibido",
        })
        return codigo
    return None

def buscar_por_codigo(tramites, codigo):
    """Devuelve el trámite con ese código, o None si no existe."""
    for t in tramites:
        if t["codigo"] == codigo.strip().upper():
            return t
    return None


def cambiar_estado(tramites, codigo, nuevo_estado):
    """Cambia el estado de un trámite.

    Devuelve "ok", "no_existe" (código inexistente) o "estado_invalido".
    """
    if not validar_estado(nuevo_estado):
        return "estado_invalido"
    t = buscar_por_codigo(tramites, codigo)
    if t is None:
        return "no_existe"
    t["estado"] = nuevo_estado
    return "ok"


def calcular_estadisticas(tramites):
    """Cuenta los trámites por estado. Devuelve un diccionario."""
    conteo = {"total": len(tramites)}
    for estado in ESTADOS_VALIDOS:
        conteo[estado] = 0
    for t in tramites:
        if t["estado"] in ESTADOS_VALIDOS:
            conteo[t["estado"]] += 1
    return conteo
