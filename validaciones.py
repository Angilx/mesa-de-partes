"""Validaciones de datos para el sistema de Mesa de Partes."""

ESTADOS_VALIDOS = ("Recibido", "En revisión", "Entregado")


def es_digito(c):
    """Devuelve True si el carácter c es un dígito del 0 al 9."""
    digitos = "0123456789"
    for d in digitos:
        if d == c:
            return True
    return False


def validar_dni(dni):
    """Un DNI es válido si tiene exactamente 8 caracteres y todos son dígitos."""
    if len(dni) != 8:
        return False
    for c in dni:
        if not es_digito(c):
            return False
    return True


def campos_completos(nombre, tipo):
    """Verifica que nombre y tipo no estén vacíos (ignorando espacios)."""
    return len(nombre.strip()) > 0 and len(tipo.strip()) > 0


def validar_estado(estado):
    """Verifica que el estado sea uno de los estados permitidos."""
    return estado in ESTADOS_VALIDOS
