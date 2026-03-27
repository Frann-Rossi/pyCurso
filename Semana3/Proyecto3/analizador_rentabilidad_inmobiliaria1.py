# =======================================
# Analizador de Rentabilidad Inmobiliaria
# =======================================

# ITP = Impuesto de Transmisiones Patrimoniales
tasas_itp = {
    'Madrid': 0.06,
    'Barcelona': 0.08,
    'Valencia': 0.07
}

def crear_propiedad(direccion,precio,metros,habitaciones,comunidades_autonomas,tipo_inmueble):
    """
    Crea un diccionario con toda la información de la propiedad.
    
    Retorna:
        dict: Un diccionario con la información de la propiedad.
    """
    propiedad = {
        'direccion': direccion,
        'precio': precio,
        'metros': metros,
        'habitaciones': habitaciones,
        'comunidades_autonomas': comunidades_autonomas,
        'tipo_inmueble': tipo_inmueble,
        'precio_metro_cuadrado': precio / metros
    }
    return propiedad

def crear_financiamiento(entrada_porcentaje, tasa_anual, plazo_anos, precio_total):
    """
    Crea un diccionario con la información del financiamiento.
    
    Retorna:
        dict: Un diccionario con la información del financiamiento.
    """
    entrada_monto = precio_total * (entrada_porcentaje / 100)
    monto_financiado = precio_total - entrada_monto
    tasa_mensual = (tasa_anual / 100) / 12
    num_pagos = plazo_anos * 12
    cuota_mensual = (monto_financiado * tasa_mensual) / (1 - (1 + tasa_mensual) ** -num_pagos)
    
    financiamiento = {
        'entrada_porcentaje': entrada_porcentaje,
        'entrada_monto': entrada_monto,
        'monto_financiado': monto_financiado,
        'tasa_anual': tasa_anual,
        'plazo_anos': plazo_anos,
        'cuota_mensual': cuota_mensual,
        'total_a_pagar': cuota_mensual * num_pagos
    }
    return financiamiento

def calcular_ibi(precio_compra, tipo_inmueble):
    tasa_ibi = 0.00428 * (tipo_inmueble == "Urbano") + 0.00567 * (tipo_inmueble == "Rústico")
    return precio_compra * tasa_ibi

def calcular_total_lista(lista_gastos):
    total = 0
    for gasto in lista_gastos:
        total += gasto[1]
    return total
    
def crear_ingresos_alquiler(renta_mensual, meses_ocupados):
    ingresos = {
        'renta_mensual': renta_mensual,
        'meses_ocupados': meses_ocupados,
        'ingresos_anuales': renta_mensual * meses_ocupados
    }
    return ingresos

def calcular_gastos_compra_iniciales(precio, comunidad_autonoma):
    tasa_itp = tasas_itp[comunidad_autonoma]
    impuesto = precio * tasa_itp
    notaria = precio * 0.015
    total = impuesto + notaria
    return (impuesto, notaria, total)

def calcular_metricas_rentabilidad(ingresos_anuales, gastos_anuales_operativos, gastos_anuales_totales, precio_propiedad, inversion_inicial):
    rentabilidad_bruta = (ingresos_anuales / precio_propiedad) * 100
    beneficio_neto = ingresos_anuales - gastos_anuales_totales
    rentabilidad_neta = (beneficio_neto / inversion_inicial) * 100
    noi = ingresos_anuales - gastos_anuales_operativos
    cap_rate = (noi / precio_propiedad) * 100
    roi_años = inversion_inicial / beneficio_neto

    return (rentabilidad_bruta, rentabilidad_neta, cap_rate, roi_años)

def pedir_datos_propiedad():
    print("=== Datos de la Propiedad ===")
    direccion = input("Dirección: ")
    precio = float(input("Precio (€): "))
    metros = float(input("Metros cuadrados: "))
    habitaciones = int(input("Cantidad de habitaciones: "))
    
    print("Comunidades disponibles:", list(tasas_itp.keys()))
    comunidad = input("Comunidad autónoma: ")
    
    tipo = input("Tipo de inmueble (Urbano/Rústico): ")
    
    return crear_propiedad(direccion, precio, metros, habitaciones, comunidad, tipo)


def pedir_datos_financiamiento(precio_total):
    print("\n=== Datos del Financiamiento ===")
    entrada = float(input("Entrada (%): "))
    tasa = float(input("Tasa anual (%): "))
    plazo = int(input("Plazo (años): "))
    
    return crear_financiamiento(entrada, tasa, plazo, precio_total)


def pedir_datos_alquiler():
    print("\n=== Datos de Alquiler ===")
    renta = float(input("Renta mensual (€): "))
    meses = int(input("Meses ocupados al año: "))
    
    return crear_ingresos_alquiler(renta, meses)


def pedir_gastos_operativos():
    print("\n=== Gastos Operativos Anuales ===")
    
    mantenimiento = float(input("Mantenimiento (€): "))
    seguros = float(input("Seguros (€): "))
    otros = float(input("Otros gastos (€): "))
    
    return [
        ("Mantenimiento", mantenimiento),
        ("Seguros", seguros),
        ("Otros", otros)
    ]


def main():
    propiedad = pedir_datos_propiedad()
    
    financiamiento = pedir_datos_financiamiento(propiedad['precio'])
    
    ingresos = pedir_datos_alquiler()
    
    gastos_operativos = pedir_gastos_operativos()
    total_gastos_operativos = calcular_total_lista(gastos_operativos)
    
    ibi = calcular_ibi(propiedad['precio'], propiedad['tipo_inmueble'])
    
    impuesto, notaria, gastos_compra = calcular_gastos_compra_iniciales(
        propiedad['precio'],
        propiedad['comunidades_autonomas']
    )
    
    gastos_totales = total_gastos_operativos + ibi + financiamiento['cuota_mensual'] * 12
    
    inversion_inicial = financiamiento['entrada_monto'] + gastos_compra
    
    metricas = calcular_metricas_rentabilidad(
        ingresos['ingresos_anuales'],
        total_gastos_operativos,
        gastos_totales,
        propiedad['precio'],
        inversion_inicial
    )
    
    print("\n=== RESULTADOS ===")
    print(f"Rentabilidad Bruta: {metricas[0]:.2f}%")
    print(f"Rentabilidad Neta: {metricas[1]:.2f}%")
    print(f"Cap Rate: {metricas[2]:.2f}%")
    print(f"Años para recuperar inversión: {metricas[3]:.2f}")


if __name__ == "__main__":
    main()