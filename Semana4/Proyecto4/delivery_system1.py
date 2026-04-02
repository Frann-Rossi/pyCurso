menu = {
    "entradas": {
        "Nachos": {"precio": 8.50, "tiempo": 10, "puntos": 50},
        "Alitas BBQ": {"precio": 12.00, "tiempo": 15, "puntos": 80},
        "Ensalada César": {"precio": 9.00, "tiempo": 8, "puntos": 60},
        "Croquetas": {"precio": 7.50, "tiempo": 12, "puntos": 45}
    },
    "principales": {
        "Pizza Margherita": {"precio": 15.00, "tiempo": 20, "puntos": 100},
        "Pizza Pepperoni": {"precio": 16.50, "tiempo": 20, "puntos": 110},
        "Hamburguesa Clásica": {"precio": 13.50, "tiempo": 18, "puntos": 90},
        "Hamburguesa BBQ": {"precio": 14.50, "tiempo": 18, "puntos": 95},
        "Pasta Carbonara": {"precio": 14.00, "tiempo": 15, "puntos": 95},
        "Pasta Bolognesa": {"precio": 13.00, "tiempo": 15, "puntos": 85}
    },
    "postres": {
        "Helado": {"precio": 5.00, "tiempo": 2, "puntos": 30},
        "Tarta de Queso": {"precio": 6.50, "tiempo": 3, "puntos": 40},
        "Brownie": {"precio": 5.50, "tiempo": 3, "puntos": 35},
        "Flan": {"precio": 4.50, "tiempo": 2, "puntos": 25}
    },
    "bebidas": {
        "Refresco": {"precio": 3.00, "tiempo": 1, "puntos": 15},
        "Agua": {"precio": 2.00, "tiempo": 1, "puntos": 10},
        "Jugo Natural": {"precio": 4.50, "tiempo": 3, "puntos": 25},
        "Café": {"precio": 2.50, "tiempo": 2, "puntos": 15}
    }
}

clientes_vip = {
    "juan": {"puntos": 500, "pedidos": 12},
    "maria": {"puntos": 1200, "pedidos": 28},
    "pedro": {"puntos": 300, "pedidos": 7},
    "ana": {"puntos": 850, "pedidos": 19},
    "luis": {"puntos": 150, "pedidos": 3}
}

combos_del_dia = {
    "Combo Italiano": {
        "items": {"Pizza Margherita", "Refresco"},
        "descuento": 15  # Porcentaje de descuento
    },
    "Combo Burger": {
        "items": {"Hamburguesa Clásica", "Nachos", "Refresco"},
        "descuento": 20
    },
    "Combo Light": {
        "items": {"Ensalada César", "Agua", "Flan"},
        "descuento": 10
    }
}

# ===== FUNCIONES DEL SISTEMA =====

def mostrar_bienbenida():
    print("=" * 60)
    print(" " * 15 + "🍕 ¡Bienvenido a Python Eats! 🍕")
    print("=" * 60)
    print()
    
def verficar_cliente():
    """
    Verifica si el cliente está registrado y retorna su información.

    Returns:
        tuple: (nombre_cliente, puntos_disponibles, es_vip)
    """
    es_cliente = ""
    
    while es_cliente not in ["s","n","si", "no"]:
        es_cliente = input("¿Eres un cliente registrado? (si/no): ").lower()
        if es_cliente not in ["s","n","si", "no"]:
            print("❌ Por favor, ingresa 's' para si o 'n' para no.")
            
    if es_cliente in ["s", "si"]:
        nombre = input("Ingresa tu nombre: ")
        if nombre in clientes_vip:
            puntos = clientes_vip[nombre]["puntos"]
            print(f"\n✨ ¡Hola {nombre}! Tienes {puntos} puntos acumulados.")
            print(f"📊 Has realizado {clientes_vip[nombre]['pedidos']} pedidos con nosotros.")
            return nombre, puntos, True
        else:
            print(f"\n👋 Hola {nombre}! No estás registrado como cliente VIP.")
            print("Te registraremos automáticamente después de tu pedido.")
            return nombre, 0, False
    else:
        print("\n👋 ¡Bienvenido nuevo cliente!")
        nombre = input("¿Cómo te llamas? ")
        print(f"    Gracias {nombre}, te registraremos después del pedido.")
        return nombre, 0, False
    
def mostrar_menu_principal():
    """Muestra el menú principal de opciones."""
    print("\n" + "=" * 40)
    print("     MENÚ PRINCIPAL")
    print("=" * 40)
    print("1. 📖 Ver menú completo")
    print("2. 🛒 Realizar pedido")
    print("3. 🎁 Ver ofertas del día")
    print("4. ⭐ Canjear puntos")
    print("5. 🚪 Salir")
    print("=" * 40)
    
def mostrar_menu_completo():
    """Muestra todos los productos disponibles organizados por categoría."""
    print("\n" + "=" * 50)
    print("         MENÚ COMPLETO")
    print("=" * 50)
    
    for categoria in menu:
        print(f"\n🍴 {categoria}")
        print("-" * 30)
        contador = 1
        productos = menu[categoria]
        for nombre in productos:
            info = productos[nombre]
            precio = info["precio"]
            tiempo = info["tiempo"]
            puntos = info["puntos"]
            print(f"  {contador}. {nombre}")
            print(f"     💵 ${precio:.2f} | ⏱️ {tiempo} min | ⭐ {puntos} pts")
            contador += 1

    print("\n" + "=" * 50)
    input("\nPresiona Enter para continuar...")
    
def mostrar_ofertas():
    """Muestra los combos especiales del día."""
    print("\n" + "=" * 50)
    print("       🎁 OFERTAS DEL DÍA 🎁")
    print("=" * 50)

    contador = 1
    for nombre_combo in combos_del_dia:
        info_combo = combos_del_dia[nombre_combo]
        productos = ""
        for item in info_combo['items']: 
            productos += f'{item}, '
        print(f"\n{contador}. {nombre_combo}")
        print(f"   Incluye: {productos[:-2]}")
        print(f"   💥 {info_combo['descuento']}% de descuento")
        contador += 1

    print("\n" + "=" * 50)
    input("\nPresiona Enter para continuar...")