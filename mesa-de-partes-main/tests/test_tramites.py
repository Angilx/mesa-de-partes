"""Pruebas automáticas. Ejecutar con:  python -m unittest discover -s tests -v"""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from persistencia import cargar_tramites, guardar_tramites
from tramites import (
    buscar_por_codigo,
    calcular_estadisticas,
    cambiar_estado,
    generar_codigo,
    nombre_tipo,
    registrar_tramite,
)
from validaciones import campos_completos, es_digito, validar_dni, validar_estado


class PruebasValidaciones(unittest.TestCase):
    def test_es_digito(self):
        self.assertTrue(es_digito("7"))
        self.assertFalse(es_digito("a"))
        self.assertFalse(es_digito(""))

    def test_dni_valido(self):
        self.assertTrue(validar_dni("12345678"))

    def test_dni_longitud_incorrecta(self):
        self.assertFalse(validar_dni("1234567"))
        self.assertFalse(validar_dni("123456789"))
        self.assertFalse(validar_dni(""))

    def test_dni_con_letras_o_simbolos(self):
        self.assertFalse(validar_dni("1234567a"))
        self.assertFalse(validar_dni("1234-678"))
        self.assertFalse(validar_dni("1234 678"))

    def test_campos_completos(self):
        self.assertTrue(campos_completos("Ana", "Matrícula"))
        self.assertFalse(campos_completos("", "Matrícula"))
        self.assertFalse(campos_completos("   ", "Matrícula"))
        self.assertFalse(campos_completos("Ana", ""))

    def test_validar_estado(self):
        self.assertTrue(validar_estado("En revisión"))
        self.assertFalse(validar_estado("en revision"))
        self.assertFalse(validar_estado(""))


class PruebasTramites(unittest.TestCase):
    def test_nombre_tipo(self):
        self.assertEqual(nombre_tipo(1), "Matrícula")
        self.assertEqual(nombre_tipo(2), "Solicitud de notas")
        self.assertEqual(nombre_tipo(3), "Registro de estudiante")
        self.assertEqual(nombre_tipo(0), "")
        self.assertEqual(nombre_tipo(9), "")

    def test_generar_codigo(self):
        self.assertEqual(generar_codigo(1), "TR-1")
        self.assertEqual(generar_codigo(25), "TR-25")

    def test_registrar_valido(self):
        lista = []
        codigo = registrar_tramite(lista, "12345678", "Ana Pérez", 1)
        self.assertEqual(codigo, "TR-1")
        self.assertEqual(len(lista), 1)
        self.assertEqual(lista[0]["estado"], "Recibido")
        self.assertEqual(lista[0]["tipo"], "Matrícula")

    def test_registrar_codigos_consecutivos(self):
        lista = []
        registrar_tramite(lista, "12345678", "Ana", 1)
        codigo = registrar_tramite(lista, "87654321", "Luis", 2)
        self.assertEqual(codigo, "TR-2")

    def test_registrar_dni_invalido(self):
        lista = []
        self.assertIsNone(registrar_tramite(lista, "123", "Ana", 1))
        self.assertEqual(lista, [])

    def test_registrar_nombre_vacio(self):
        lista = []
        self.assertIsNone(registrar_tramite(lista, "12345678", "  ", 1))
        self.assertEqual(lista, [])

    def test_registrar_tipo_invalido(self):
        lista = []
        self.assertIsNone(registrar_tramite(lista, "12345678", "Ana", 7))
        self.assertEqual(lista, [])

    def test_buscar(self):
        lista = []
        registrar_tramite(lista, "12345678", "Ana", 1)
        self.assertEqual(buscar_por_codigo(lista, "TR-1")["nombre"], "Ana")
        self.assertEqual(buscar_por_codigo(lista, " tr-1 ")["nombre"], "Ana")
        self.assertIsNone(buscar_por_codigo(lista, "TR-99"))

    def test_cambiar_estado(self):
        lista = []
        registrar_tramite(lista, "12345678", "Ana", 1)
        self.assertEqual(cambiar_estado(lista, "TR-1", "En revisión"), "ok")
        self.assertEqual(lista[0]["estado"], "En revisión")
        self.assertEqual(cambiar_estado(lista, "TR-9", "Entregado"), "no_existe")
        self.assertEqual(cambiar_estado(lista, "TR-1", "cualquier cosa"), "estado_invalido")
        self.assertEqual(lista[0]["estado"], "En revisión")

    def test_estadisticas(self):
        lista = []
        registrar_tramite(lista, "12345678", "Ana", 1)
        registrar_tramite(lista, "87654321", "Luis", 2)
        registrar_tramite(lista, "11112222", "Eva", 3)
        cambiar_estado(lista, "TR-2", "En revisión")
        cambiar_estado(lista, "TR-3", "Entregado")
        est = calcular_estadisticas(lista)
        self.assertEqual(est["total"], 3)
        self.assertEqual(est["Recibido"], 1)
        self.assertEqual(est["En revisión"], 1)
        self.assertEqual(est["Entregado"], 1)

    def test_estadisticas_vacio(self):
        est = calcular_estadisticas([])
        self.assertEqual(est["total"], 0)
        self.assertEqual(est["Recibido"], 0)


class PruebasPersistencia(unittest.TestCase):
    def test_guardar_y_cargar(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "sub", "t.csv")
            lista = []
            registrar_tramite(lista, "12345678", "Ñandú Pérez, Jr.", 2)
            cambiar_estado(lista, "TR-1", "Entregado")
            guardar_tramites(lista, ruta)
            self.assertEqual(cargar_tramites(ruta), lista)

    def test_cargar_archivo_inexistente(self):
        self.assertEqual(cargar_tramites("no_existe_xyz.csv"), [])

    def test_cargar_omite_filas_corruptas(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "t.csv")
            with open(ruta, "w", encoding="utf-8") as f:
                f.write("codigo,dni,nombre,tipo,estado\n")
                f.write("TR-1,12345678,Ana,Matrícula,Recibido\n")
                f.write("TR-2,abc,Luis,Matrícula,Recibido\n")
                f.write("TR-3,87654321,Eva,Matrícula,Inventado\n")
            self.assertEqual(len(cargar_tramites(ruta)), 1)


if __name__ == "__main__":
    unittest.main()
