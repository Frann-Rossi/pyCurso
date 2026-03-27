def cabecera():
    """Muestra cabecera de la app"""
    titulo = r"""
 _____                             _____ ___  _____  _____    _         _                          _         _ 
|  __ \                           |_   _/ _ \|  __ \/  ___|  (_)       (_)                        (_)       (_)
| |  \/ __ _ _ __ ___   ___ _ __    | |/ /_\ \ |  \/\ `--.    _         _   ______       ______    _         _ 
| | __ / _` | '_ ` _ \ / _ \ '__|   | ||  _  | | __  `--. \  | |       | | |______|     |______|  | |       | |
| |_\ \ (_| | | | | | |  __/ |      | || | | | |_\ \/\__/ /  | |  _ _  | |           _            | |  _ _  | |
 \____/\__,_|_| |_| |_|\___|_|      \_/\_| |_/\____/\____/   |_| (_|_) |_|          (_)           |_| (_|_) |_|
                                                                                                               
                                                                                                               
"""
    print(titulo)

def crear_tag_basico(nombre):
    """
    Crea un gamerTag basico usando las primeras 4 letras

    Parametros:
    nombre (str):El nombre del usuario

    Retorna:
    str: GamerTag basico
    """

    tag = nombre[:4]
    return tag

def crear_tag_invertido(nombre):
     """
    Crea un gamerTag invertido.

    Parametros:
    nombre (str):El nombre del usuario

    Retorna:
    str: Nombre invertido
    """
     
     tag = nombre[::-1]
     return tag

def crear_tag_intercalado(nombre, apellido):
    tag = nombre[0] + apellido[0]
    tag2 = nombre[1:] + apellido[1:]
    return tag + tag2
    

def crear_tag_elite(nombre):
    tag = nombre[:2]
    tag2 = nombre[-2:]
    return tag+tag2

def crear_tag_con_numero(nombre, numero_favorito):
    tag = nombre[:5]
    return tag + str(numero_favorito)

def mostrar_estadisticas(nombre):
    longitud_nombre = len(nombre)

    print("ESTADISTICAS DE TU NOMBRE:")
    print(f"Nombre completo: {nombre}")
    print(f"Longitud del nombre: {longitud_nombre}")
    print(f"Primera letra: {nombre[0]}")
    print(f"Ultima letra: {nombre[-1]}")


def pedir_datos():
    print("Ingrese sus datos para el programa"),
    nombre = input("Tu Nombre: ")
    apellido = input("Tu Apellido: ")
    num = input("Numero Favorito: ")

    return nombre,apellido,num


def main():
    nombre,apellido,num  = pedir_datos();
    cabecera()
    tag_basico = crear_tag_basico(nombre)
    tag_invertido = crear_tag_invertido(nombre)
    tag_intercalado = crear_tag_intercalado(nombre, apellido)
    tag_elite = crear_tag_elite(nombre)
    tag_num = crear_tag_con_numero(nombre,num)
    print(tag_basico)
    print(tag_invertido)
    print(tag_intercalado)
    print(tag_elite)
    print(tag_num)
    mostrar_estadisticas(nombre)

main()
