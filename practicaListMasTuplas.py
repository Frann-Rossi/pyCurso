def cargar_dato():
    nombre = input("Ingrese su nombre: \n")
    while True:
        try:
            edad = int(input("Ingrese su edad: \n"))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.\n")
    clase = input("(por ejemplo: Guerrero, Mago o Arquero): \n")
    return nombre, edad, clase

def cargar_datos():
    datos = []
    while True:
        datos.append(cargar_dato())
        control = input("🤔¿Desea ingresar otro dato? (s/n): \n").strip().lower()
        if control != 's':
            break
    return datos

def bienvenida():
    datos = cargar_datos()
    for nombre, edad, clase in datos:
        if edad >= 18 and edad <= 40:
            print(f"😎¡Bienvenido al gremio, {nombre} el {clase}!\n")
        elif edad < 18:
            print(f"😢Lo siento, {nombre}, vuelva cuando sea mayor de edad.\n")
        else:
            print(f"🫡Lo siento, {nombre}, sos un veterano consagrado y debe jubilarse.\n")

def main():
    bienvenida()
if __name__ == "__main__":    
    main()