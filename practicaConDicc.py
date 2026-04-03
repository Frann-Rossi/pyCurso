def cargar_dato():
    
    nombre = input("Ingrese su nombre: \n")
    while True:
        try:
            edad = int(input("Ingrese su edad: \n"))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.\n")
    clase = input("(por ejemplo: Guerrero, Mago o Arquero): \n").strip().lower()
    
    pj = {
        "nombre": nombre,
        "edad": edad,
        "clase": clase,
        "equipo": obtener_equipo(clase)
    }
    return pj

def cargar_datos():
    datos = []
    while True:
        datos.append(cargar_dato())
        control = input("🤔¿Desea ingresar otro dato? (s/n): \n").strip().lower()
        if control != 's':
            break
    return datos

def mostrar_dato(pj):
    print(f"Nombre: {pj['nombre']}, Edad: {pj['edad']}, Clase: {pj['clase']}, Equipo: {pj['equipo']}")

def mostrar_datos(datos):
    for pj in datos:
        mostrar_dato(pj)
        
def obtener_equipo(clase):
    equipo = {
        "guerrero": "Espada y Escudo",
        "mago": "Báculo y Libro de Hechizos",
        "arquero": "Arco y Flechas"
    }
    return equipo.get(clase.lower(), "Un palo del piso")

def separador():
    print("-" * 60)

def bienvenida():
    datos = cargar_datos()
    for pj in datos:
        equipo = pj["equipo"]
        separador()
        if 18 <= pj["edad"] <= 40:
            print(f"\n😎¡Bienvenido al gremio, Nombre: {pj['nombre']}, Clase: {pj['clase']}!")
            print(f"Tu equipo inicial  es: {equipo}\n")
        elif pj["edad"] < 18:
            print(f"\n😢Lo siento, {pj['nombre']}, vuelva cuando sea mayor de edad.\n")
        else:
            print(f"\n🫡Lo siento, {pj['nombre']}, sos un veterano consagrado y debe jubilarse.\n")

    separador()
    print("📋 LISTADO DE PERSONAJES")
    separador()
    mostrar_datos(datos)

def main():
    bienvenida()
if __name__ == "__main__":    
    main()