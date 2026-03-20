import sys
sys.path.append( 'src')

from model import logica_liquidador

try:
    entrada_salario = input("Ingrese el valor del salario mensual: ")
    entrada_horas_extra = input("Ingrese el valor (dinero mensual) de las horas extra: ")
    entrada_bonificaciones = input("Ingrese el valor (dinero mensual) de las bonificaciones: ")
    entrada_comisiones = input("Ingrese el valor (dinero mensual) de las comisiones: ")
    entrada_auxilios = input("Ingrese el valor (dinero mensual) de los auxilios: ")

    entrada_salud = input("Ingrese el valor del porcentaje de la salud que usted paga (ademas no mayor a 4%): ")
    entrada_pension = input("Ingrese el valor del porcentaje de la pensión que usted paga (ademas no mayor a 4%): ")
    entrada_impuesto_dinero = input("Ingrese el valor (dinero mensual) de los impuestos que usted paga: ")

    campos = [
        entrada_salario,
        entrada_horas_extra,
        entrada_bonificaciones,
        entrada_comisiones,
        entrada_auxilios,
        entrada_salud,
        entrada_pension,
        entrada_impuesto_dinero]

    indices_vacios = [i for i, valor in enumerate(campos) if valor == ""]
    
    if indices_vacios:
        nombres_campos = [
            "salario", 
            "horas extra", 
            "bonificaciones", 
            "comisiones", 
            "auxilios", 
            "salud", 
            "pensión", 
            "impuesto" ]
        
        campos_faltantes = [nombres_campos[i] for i in indices_vacios]
        raise ValueError(f"ERROR: Campos obligatorios vacíos: {', '.join(campos_faltantes)}")

    salario = float(entrada_salario)
    horas_extra = float(entrada_horas_extra)
    bonificaciones = float(entrada_bonificaciones)
    comisiones = float(entrada_comisiones)
    auxilios = float(entrada_auxilios)

    salud = float(entrada_salud)
    pension = float(entrada_pension)
    impuesto_dinero = float(entrada_impuesto_dinero)

    liquidacion = logica_liquidador.LiquidacionSalario(
        salario= float( entrada_salario ),
        horas_extra= float( entrada_horas_extra ),
        bonificaciones= float( entrada_bonificaciones ),
        comisiones= float( entrada_comisiones ),
        auxilios= float( entrada_auxilios ),
        salud= float( entrada_salud ),
        pension= float( entrada_pension ),
        impuesto_dinero = float( entrada_impuesto_dinero ))

    salario_neto = logica_liquidador.calcular_salario( liquidacion )

    print("El salario neto es:", salario_neto)

except Exception as err:
    print("Ocurrió un error:", err)
    print(str(err))