import json

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

def cargar_datos_archivo():
    try:
        with open("gremio.json", "r") as f:
            datos = json.load(f)
            print("Datos cargados correctamente.")
            return datos
    except FileNotFoundError:
        print("No existe el archivo, se crea uno nuevo.")
        return []

def cargar_datos_usuario():
    datos = []
    while True:
        datos.append(cargar_dato())
        control = input("¿Desea ingresar otro dato? (s/n): ").lower()
        if control != 's':
            break
    return datos

def guardar_datos(datos):
    with open("gremio.json", "w") as f:
        # indent=4 hace que el archivo sea legible para humanos
        json.dump(datos, f, indent=4)
    print("¡Datos guardados con éxito en el archivo!")

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

def bienvenida(datos):
    for pj in datos:
        equipo = pj["equipo"]
        separador()
        
        if 18 <= pj["edad"] <= 40:
            print(f"\n😎¡Bienvenido al gremio, Nombre: {pj['nombre']}, Clase: {pj['clase']}!")
            print(f"Tu equipo inicial es: {equipo}\n")
        
        elif pj["edad"] < 18:
            print(f"\n😢Lo siento, {pj['nombre']}, vuelva cuando sea mayor de edad.\n")
        
        else:
            print(f"\n🫡Lo siento, {pj['nombre']}, sos un veterano consagrado y debe jubilarse.\n")
    
def main():
    datos_actuales = cargar_datos_archivo()
    
    print("\n--- REGISTRO DE NUEVOS AVENTUREROS ---")
    nuevos = cargar_datos_usuario()
    datos_actuales.extend(nuevos)
    
    guardar_datos(datos_actuales)
    
    separador()
    print(f"Total de aventureros registrados: {len(datos_actuales)}")
    
    mostrar_datos(datos_actuales)
    
    # 👇 ahora sí tiene sentido
    bienvenida(datos_actuales)

if __name__ == "__main__":
    main()