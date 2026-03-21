import unittest

import sys
sys.path.append('src')

from model import logica_liquidador

class TestCalculoSalario(unittest.TestCase):



    # CASOS NORMALES ---------------------------------------------------------------------------

    def test_normal1_salario(self):
        """
        test normal de la aplicación
        """
        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= 5000000,
            horas_extra= 150000,
            bonificaciones= 50000,
            comisiones= 100000,
            auxilios= 0,
            salud= 4,
            pension= 4,
            impuesto_dinero = 50000)

        # proceso
        salario_calculado = logica_liquidador.calcular_salario(liquidacion)

        # datos de salida esperados
        salario_esperado = 4850000

        # verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    def test_normal2_salario(self):
        """
        test normal de la aplicación
        """
        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= 6200000,
            horas_extra= 100000,
            bonificaciones= 100000,
            comisiones= 20000,
            auxilios= 0,
            salud= 4,
            pension= 4,
            impuesto_dinero = 62000)

        # proceso
        salario_calculado = logica_liquidador.calcular_salario(liquidacion )

        # datos de salida esperados
        salario_esperado = 5862000

        # verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    def test_normal3_salario(self):
        """
        test normal de la aplicación
        """
        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= 4500000,
            horas_extra= 50000,
            bonificaciones= 50000,
            comisiones= 20000,
            auxilios= 0,
            salud= 4,
            pension= 4,
            impuesto_dinero = 45000)

        # proceso
        salario_calculado = logica_liquidador.calcular_salario( liquidacion )

        # datos de salida esperados
        salario_esperado = 4215000

        # verificar la salida
        self.assertEqual( salario_calculado, salario_esperado )

    def test_normal4_salario( self ):
        """
        test normal de la aplicación
        """
        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= 4000000,
            horas_extra= 200000,
            bonificaciones= 60000,
            comisiones= 10000,
            auxilios= 0,
            salud= 4,
            pension= 4,
            impuesto_dinero = 40000)

        # proceso
        salario_calculado = logica_liquidador.calcular_salario(liquidacion)

        # datos de salida esperados
        salario_esperado = 3910000

        # verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)


    # CASOS EXTRAORDINARIOS ------------------------------------------------------------------------

    def test_empleado_no_trabajo(self):
        """
        test extraordinario que aunque el empleado no haya trabajado, sigue calculando con normalidad.
        """

        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= 0,
            horas_extra= 0,
            bonificaciones= 0,
            comisiones= 0,
            auxilios= 0,
            salud= 4,
            pension= 4,
            impuesto_dinero = 0)

        # proceso
        salario_calculado = logica_liquidador.calcular_salario(liquidacion)

        # datos de salida esperados
        salario_esperado = 0

        # verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    def test_salario_en_limite_de_impuestos(self):
        """
        test extraordinario que aunque los impuestos estén en el límite, sigue calculando con normalidad.
        """

        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= 3500000,
            horas_extra= 0,
            bonificaciones= 0,
            comisiones= 0,
            auxilios= 0,
            salud= 4,
            pension= 4,
            impuesto_dinero = 35000)

        # proceso
        salario_calculado = logica_liquidador.calcular_salario(liquidacion)

        # datos de salida esperados
        salario_esperado = 3185000

        # verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    def test_salario_muy_alto(self):
        """
        test extraordinario que permite ingresar salarios altos y intervenir en el funcionamiento.
        """


        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= 25000000,
            horas_extra= 200000,
            bonificaciones= 100000,
            comisiones= 30000,
            auxilios= 0,
            salud= 4,
            pension= 4,
            impuesto_dinero = 250000)

        # proceso
        salario_calculado = logica_liquidador.calcular_salario(liquidacion)

        # datos de salida esperados
        salario_esperado = 23080000

        # verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)

    def test_ingresos_solo_por_auxilios(self):
        """
        test extraordinario que aunque solo se reciban auxilios, sigue calculando con normalidad.
        """
        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= 0,
            horas_extra= 0,
            bonificaciones= 0,
            comisiones= 0,
            auxilios= 249095,
            salud= 4,
            pension= 4,
            impuesto_dinero = 0)

        # proceso
        salario_calculado = logica_liquidador.calcular_salario(liquidacion)

        # datos de salida esperados
        salario_esperado = 249095

        # verificar la salida
        self.assertEqual(salario_calculado, salario_esperado)


    # CASOS DE ERROR ----------------------------------------------------------------------------

    def test_salario_obligatorio(self):
        """
        test que genera una excepción en caso de que no se ingrese un valor en el campo de salario.
        """
        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= "",
            horas_extra= 0,
            bonificaciones= 0,
            comisiones= 0,
            auxilios= 0,
            salud= 4,
            pension= 4,
            impuesto_dinero = 0)

        # verificar la salida
        with self.assertRaises(logica_liquidador.errores.ErrorCampoObligatorio):
            logica_liquidador.calcular_salario(liquidacion)

    def test_salario_tipo_invalido(self):
        """
        test que genera una excepción en caso de que se ingrese un campo inválido en el campo de salario.
        """
        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= "5000000",
            horas_extra= 0,
            bonificaciones= 0,
            comisiones= 0,
            auxilios= 0,
            salud= 4,
            pension= 4,
            impuesto_dinero= 0)

        # verificar la salida
        with self.assertRaises(logica_liquidador.errores.ErrorTipoInvalido):
            logica_liquidador.calcular_salario( liquidacion )

    def test_valor_negativo(self):
        """
        test que genera una excepción en caso de que se ingrese un valor negativo en algún campo.
        """
        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= -1000,
            horas_extra= -1000,
            bonificaciones= -1000,
            comisiones= -1000,
            auxilios= -1000,
            salud= -4,
            pension= -4,
            impuesto_dinero = -4)

        # verificar la salida
        with self.assertRaises(logica_liquidador.errores.ErrorValorNegativo):
            logica_liquidador.calcular_salario( liquidacion )

    def test_salario_fuera_rango(self):
        """
        test que genera una excepción en caso de el salario este fuera del rango permitido.
        """
        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= 2_000_000_000,
            horas_extra= 0,
            bonificaciones= 0,
            comisiones= 0,
            auxilios= 0,
            salud= 4,
            pension= 4,
            impuesto_dinero = 0)

        # verificar la salida
        with self.assertRaises( logica_liquidador.errores.ErrorSalarioGrande ):
            logica_liquidador.calcular_salario( liquidacion )

    def test_porcentaje_fuera_rango(self):
        """
        test que genera una excepción en caso de los porcentajes estén fuera de los rangos legales.
        """
        # entradas
        liquidacion = logica_liquidador.LiquidacionSalario(
            salario= 5000000,
            horas_extra= 0,
            bonificaciones= 0,
            comisiones= 0,
            auxilios= 0,
            salud= 30,
            pension= 4,
            impuesto_dinero= 0)

        # verificar la salida
        with self.assertRaises( logica_liquidador.errores.ErrorPorcentajesFueraRango ):
            logica_liquidador.calcular_salario( liquidacion )


if __name__ == '__main__':
    unittest.main()