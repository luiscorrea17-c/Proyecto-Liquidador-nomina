from model import errores

class LiquidacionSalario():
    """
    Clase que encapsula los datos necesarios para liquidar el salario de un trabajador.
    """
    salario: float
    horas_extra: float
    bonificaciones: float
    comisiones: float
    auxilios: float
    salud: float
    pension: float
    impuesto_dinero: float

    def __init__( self, salario, horas_extra: float, bonificaciones: float,
                  comisiones: float, auxilios: float, salud: float,
                  pension: float, impuesto_dinero: float ):
        self.salario= salario
        self.horas_extra= horas_extra
        self.bonificaciones= bonificaciones
        self.comisiones= comisiones
        self.auxilios= auxilios
        self.salud= salud
        self.pension= pension
        self.impuesto_dinero= impuesto_dinero


def _validar_campo_obligatorio(liquidacion):
    if liquidacion.salario == "":
        raise errores.ErrorCampoObligatorio()


def _validar_tipo(liquidacion):
    if not isinstance(liquidacion.salario, (int, float)):
        raise errores.ErrorTipoInvalido(liquidacion.salario)


def _validar_sin_negativos(liquidacion):
    campos = {
        "salario":liquidacion.salario,
        "horas_extra":liquidacion.horas_extra,
        "bonificaciones":liquidacion.bonificaciones,
        "comisiones":liquidacion.comisiones,
        "auxilios":liquidacion.auxilios,
        "salud":liquidacion.salud,
        "pension":liquidacion.pension,
        "impuesto_dinero":liquidacion.impuesto_dinero,}
    
    for campo, valor in campos.items():
        if valor < 0:
            raise errores.ErrorValorNegativo(campo, valor)


def _validar_salario_en_rango(liquidacion):
    if liquidacion.salario > errores.MAX_SALARIO:
        raise errores.ErrorSalarioGrande(liquidacion.salario)


def _validar_porcentajes(liquidacion):
    if (liquidacion.salud > errores.MAX_PORCENTAJE_SALUD or 
        liquidacion.pension > errores.MAX_PORCENTAJE_PENSION):
        raise errores.ErrorPorcentajesFueraRango(
            liquidacion.salud, liquidacion.pension)


def calcular_salario( liquidacion: LiquidacionSalario ) -> float:
    """
    Calcula el salario neto de un trabajador descontando deducciones de ley.

    Parámetros
    liquidacion : LiquidacionSalario
        Objeto con todos los datos necesarios para el cálculo:
        salario, horas_extra, bonificaciones, comisiones, auxilios,
        salud, pension, impuesto_dinero.

    """
    _validar_campo_obligatorio(liquidacion)
    _validar_tipo(liquidacion)
    _validar_sin_negativos(liquidacion)
    _validar_salario_en_rango(liquidacion)
    _validar_porcentajes(liquidacion)

    valores_devengados = sum([ liquidacion.salario, liquidacion.horas_extra,
                               liquidacion.bonificaciones, liquidacion.comisiones,
                               liquidacion.auxilios ])

    descuento_salud= ( liquidacion.salud / 100 ) * liquidacion.salario
    descuento_pension= ( liquidacion.pension / 100 ) * liquidacion.salario
    deducciones_de_ley= sum([ descuento_salud, descuento_pension, liquidacion.impuesto_dinero ])

    return valores_devengados - deducciones_de_ley