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