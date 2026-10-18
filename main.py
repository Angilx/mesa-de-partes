"""Mesa de Partes: interfaz de consola."""

from persistencia import cargar_tramites, guardar_tramites
from tramites import (
    buscar_por_codigo,
    calcular_estadisticas,
    cambiar_estado,
    registrar_tramite,
)
from validaciones import ESTADOS_VALIDOS


def mostrar_menu():
    print("\n===== MESA DE PARTES =====")
    print("1. Registrar trámite")
    print("2. Buscar por código")
    print("3. Listar trámites")
    print("4. Cambiar estado")
    print("5. Ver estadísticas")
    print("6. Salir")


def leer_entero(mensaje):
    """Lee un número entero; devuelve 0 si el usuario escribe algo que no es número."""
    texto = input(mensaje).strip()
    if texto.isdigit():
        return int(texto)
    return 0


def opcion_registrar(tramites):
    dni = input("Ingrese DNI: ").strip()
    nombre = input("Ingrese nombre del estudiante: ")
    print("Tipo de trámite: 1. Matrícula  2. Notas  3. Registro de estudiante")
    op = leer_entero("Opción: ")
    codigo = registrar_tramite(tramites, dni, nombre, op)
    if codigo is None:
        print("Datos inválidos")
    else:
        print("Trámite registrado. Código:", codigo)
        guardar_tramites(tramites)


def opcion_buscar(tramites):
    codigo = input("Ingrese el código: ")
    t = buscar_por_codigo(tramites, codigo)
    if t is None:
        print("Código no existe")
    else:
        print("Estado:", t["estado"])


def opcion_listar(tramites):
    if len(tramites) == 0:
        print("No hay trámites registrados")
        return
    for t in tramites:
        print(t["codigo"], "|", t["nombre"], "|", t["tipo"], "|", t["estado"])


def opcion_cambiar_estado(tramites):
    codigo = input("Ingrese el código: ")
    nuevo = input("Nuevo estado (En revisión / Entregado): ").strip()
    resultado = cambiar_estado(tramites, codigo, nuevo)
    if resultado == "ok":
        print("Estado actualizado")
        guardar_tramites(tramites)
    elif resultado == "no_existe":
        print("Código no existe")
    else:
        print("Estado inválido. Use uno de:", ", ".join(ESTADOS_VALIDOS))


def opcion_estadisticas(tramites):
    est = calcular_estadisticas(tramites)
    print("Total de trámites:", est["total"])
    print("Recibidos:", est["Recibido"])
    print("En revisión:", est["En revisión"])
    print("Entregados:", est["Entregado"])


def main():
    tramites = cargar_tramites()
    opcion = 0
    while opcion != 6:
        mostrar_menu()
        opcion = leer_entero("Opción: ")
        if opcion == 1:
            opcion_registrar(tramites)
        elif opcion == 2:
            opcion_buscar(tramites)
        elif opcion == 3:
            opcion_listar(tramites)
        elif opcion == 4:
            opcion_cambiar_estado(tramites)
        elif opcion == 5:
            opcion_estadisticas(tramites)
        elif opcion == 6:
            guardar_tramites(tramites)
            print("Saliendo del sistema")
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
