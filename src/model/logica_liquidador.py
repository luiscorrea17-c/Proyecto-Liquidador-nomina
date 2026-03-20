MAX_SALARIO = 1_000_000_000  
MAX_PORCENTAJE_SALUD = 4             
MAX_PORCENTAJE_PENSION = 4              


class ErrorCampoObligatorio( Exception ):
    """
    Excepción personalizada para indicar que el salario es un campo obligatorio.
    """
    def __init__( self ):
        super().__init__(
            f"[Campo obligatorio faltante] "
            f"El salario es requerido y no puede estar vacío. "
            f"Ingrese un valor numérico para el salario.")


class ErrorTipoInvalido( Exception ):
    """
    Excepción personalizada para indicar que el salario no es de tipo int o float.

    Para usar esta excepción, indique el valor recibido:
        ErrorTipoInvalido( valor )
    """
    def __init__( self, valor ):
        super().__init__(
            f"[Tipo de dato inválido] "
            f"El valor '{valor}' es de tipo {type(valor).__name__}. "
            f"Se esperaba un número entero o decimal (int o float).")


class ErrorValorNegativo(Exception):
    """
    Excepción personalizada para indicar que un campo tiene valor negativo.

    Para usar esta excepción, indique el / los campos que recibieron valores negativos
        ErrorValorNegativo("salario", -500)
    """
    def __init__(self, campo: str, valor: float):
        super().__init__(
            f"[Valor negativo] "
            f"El campo '{campo}' tiene un valor negativo ({valor}). "
            f"Ingrese un valor mayor o igual a 0.")


class ErrorSalarioGrande( Exception ):
    """
    Excepción personalizada para indicar que el salario supera el límite máximo permitido.

    Para usar esta excepción, indique el salario recibido:
        ErrorSalarioGrande( salario )
    """
    def __init__( self, salario: float ):
        super().__init__(
            f"[Salario fuera de rango] "
            f"El salario ({salario:,}) supera el máximo permitido de {MAX_SALARIO:,}. "
            f"Ingrese un salario entre 0 y {MAX_SALARIO:,}.")


class ErrorPorcentajesFueraRango( Exception ):
    """
    Excepción personalizada para indicar que el porcentaje de salud o pensión
    supera el límite legal colombiano.

    Para usar esta excepción, indique los porcentajes recibidos:
        ErrorPorcentajesFueraRango( salud, pension )
    """
    def __init__( self, salud: float, pension: float ):
        super().__init__(
            f"[Porcentaje fuera del rango legal] "
            f"El porcentaje de salud ({salud}%) o pensión ({pension}%) supera el máximo "
            f"legal permitido en Colombia ({MAX_PORCENTAJE_SALUD}%). "
            f"Ingrese porcentajes entre 0 y {MAX_PORCENTAJE_SALUD}%.")



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
        raise ErrorCampoObligatorio()


def _validar_tipo(liquidacion):
    if not isinstance(liquidacion.salario, (int, float)):
        raise ErrorTipoInvalido(liquidacion.salario)


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
            raise ErrorValorNegativo(campo, valor)


def _validar_salario_en_rango(liquidacion):
    if liquidacion.salario > MAX_SALARIO:
        raise ErrorSalarioGrande(liquidacion.salario)


def _validar_porcentajes(liquidacion):
    if (liquidacion.salud > MAX_PORCENTAJE_SALUD or 
        liquidacion.pension > MAX_PORCENTAJE_PENSION):
        raise ErrorPorcentajesFueraRango(
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