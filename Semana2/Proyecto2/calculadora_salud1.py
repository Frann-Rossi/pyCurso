#====================
#Calculadora de Fitness y Salud Personal
#====================

def calcular_imc(peso_kg,alt_m):
    """
    Calcula el indice de la Masa Corporal (IMC)

    Fornmula: IMC = peso / (alt^2)

    Parametros:
    peso_kg(float): Peso en kg
    alt_m(float): Altura en metros

    Retorna:
    float: El IMC calculado
    """

    imc = peso_kg / (alt_m ** 2)
    return imc

def peso_saludable(imc):
    """
    Determina si el IMC esta en rango saludable (18.5 - 24.9)

    Parametros:
    imc(float): Indice de masa corporal

    Retorna:
    bool: True so esta en rango saludable, False si no
    """
    return imc >= 18.5 and imc <= 24.9

def tiene_sobrepeso(imc):
    return imc >= 25 

def tiene_bajo_peso(imc):
    return imc < 18.5

def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    calorias_hombre = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)
    calorias_mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)
    if(es_hombre):
        return calorias_hombre
    else:
        return calorias_mujer
    
def calcular_agua_diaria(peso_kg):
    return (peso_kg * 35) / 1000

def calcular_ritmo_cardiaco_maximo(edad):
    return 220 - edad

def pedir_datos():
    peso_kg = float(input("Ingrese su Peso en kg (ejemplo: 87): "))
    altura_cm = float(input("Ingrese su Altura en centímetros (ejemplo: 175): "))
    edad = int(input("Ingrese su edad:"))
    entrada_sexo = input("Ingrese 1 si es HOMBRE o 0 si es MUJER:")
    es_hombre = (entrada_sexo == "1")

    return peso_kg,altura_cm,edad,es_hombre

def main():
    peso_kg,altura_cm,edad,entrada_sexo= pedir_datos()
    altura_m = altura_cm / 100
    imc = calcular_imc(peso_kg,altura_m)
    calorias_diarias = calcular_calorias_diarias(peso_kg,altura_cm,edad,entrada_sexo)
    agua_diaria = calcular_agua_diaria(peso_kg)
    ritmo_cardiaco = calcular_ritmo_cardiaco_maximo(edad)

    print("\n====================")
    print("   TUS RESULTADOS   ")
    print("====================")

    print(f"Tu IMC es: {imc:.2f}")

    if tiene_bajo_peso(imc):
        print("Categoría: Tienes bajo peso. ¡Consulta a un especialista para subir de forma saludable!")
    elif peso_saludable(imc):
        print("Categoría: ¡Felicidades! Tu peso es saludable.")
    elif tiene_sobrepeso(imc):
        print("Categoría: Tienes sobrepeso. ¡Cuidar tu alimentación y hacer ejercicio te ayudará mucho!")

    print(f"Calorías Diarias (mantenimiento): {calorias_diarias:.0f} kcal")
    print(f"Agua diaria a tomar: {agua_diaria:.1f} litros")
    print(f"Tu ritmo cardíaco máximo debe ser de: {ritmo_cardiaco} latidos por minuto")
    print("====================\n")

main()