# Se hace un diccionario inventario, con diccionarios para cada item
inventario = {
    "laptop": {"precio": 2500, "stock": 10},
    "mouse": {"precio": 50, "stock": 50},
    "teclado": {"precio": 120, "stock": 30},
    "audifonos": {"precio": 80, "stock": 25},
    "monitor": {"precio": 300, "stock": 15}
}
# Se crea el carrito de compras como un diccionario
carrito = {}
# Se crea función para controlar las entradas del usuario
def obtener_entrada_numerica(mensaje: str, tipo_dato=float, minimo=0):
    while True:
        entrada = input(mensaje)
        try:
            numero = tipo_dato(entrada)
            if numero >= minimo:
                return numero
            else:
                print(f"Error: El número debe ser mayor o igual a {minimo}.")
        except ValueError:
            print(f"Error: Por favor ingrese un valor numérico válido.")
# Se crea función para obtener el nombre del producto
def obtener_nombre_producto(mensaje: str):
    while True:
        nombre = input(mensaje).strip().lower()
        if nombre:
            return nombre
        else:
            print("Error: El nombre no puede estar vacío.")
# Se creaa función para mostrar la lista de productos
def mostrar_lista_productos(lista: dict):
    if not lista:
        return False

    print("\n--- LISTA DE PRODUCTOS ---")
    for i, nombre in enumerate(lista.keys(), start=1):
        info = lista[nombre]
        
        if isinstance(info, dict):
            print(f" {i}. {nombre.capitalize():<15} - ${info['precio']:>8.2f} (Stock: {info['stock']})")
        else:
            precio = inventario[nombre]['precio']
            print(f" {i}. {nombre.capitalize():<15} - {info} unidad(es) - Subtotal: ${precio * info:>8.2f}")
    return True
# Se crea función para seleccionar cada producto
def seleccionar_producto(lista: dict):
    if not mostrar_lista_productos(lista):
        print("No hay productos para seleccionar.")
        return None

    while True:
        nombres_productos = list(lista.keys())
        try:
            opcion = int(input("\nSeleccione el número del producto: \n--> ")) - 1
            
            if 0 <= opcion < len(nombres_productos):
                return nombres_productos[opcion]
            else:
                print("Error: Número fuera de rango.")
        except ValueError:
            print("Error: Por favor ingrese un número.")
# Se crea función para agregar producto al inventario
def agregar_producto_inventario():
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    nombre = obtener_nombre_producto("Ingrese el nombre del nuevo producto: \n--> ")
    
    if nombre in inventario:
        print("\nError: Ya existe un producto con ese nombre.")
        opcion = input("¿Desea actualizar su precio y stock? (s/n): ").lower()
        if opcion == 's':
            actualizar_producto_inventario(nombre_existente=nombre)
    else:
        precio = obtener_entrada_numerica("Ingrese el precio: \n--> $", minimo=0.01)
        stock = obtener_entrada_numerica("Ingrese el stock inicial: \n--> ", tipo_dato=int, minimo=0)
        
        inventario[nombre] = {"precio": precio, "stock": stock}
        print(f"\n¡Producto '{nombre.capitalize()}' agregado con éxito!")
# Se crea función para actualizar los productos
def actualizar_producto_inventario(nombre_existente=None):
    print("\n--- ACTUALIZAR PRODUCTO ---")
    if nombre_existente:
        nombre = nombre_existente
        print(f"Actualizando '{nombre.capitalize()}'...")
    else:
        nombre = seleccionar_producto(inventario)
        if nombre is None:
            return

    print("¿Qué desea actualizar?")
    print("1. Precio")
    print("2. Stock")
    print("3. Ambos")
    opcion = input("--> ")

    if opcion == '1' or opcion == '3':
        nuevo_precio = obtener_entrada_numerica(f"Ingrese el nuevo precio para '{nombre.capitalize()}': \n--> $", minimo=0.01)
        inventario[nombre]['precio'] = nuevo_precio
        
    if opcion == '2' or opcion == '3':
        nuevo_stock = obtener_entrada_numerica(f"Ingrese el nuevo stock para '{nombre.capitalize()}': \n--> ", tipo_dato=int, minimo=0)
        inventario[nombre]['stock'] = nuevo_stock
        
    print(f"\n¡Producto '{nombre.capitalize()}' actualizado con éxito!")
# Se crea función para eliminar un producto del inventario
def eliminar_producto_inventario():
    print("\n--- ELIMINAR PRODUCTO ---")
    nombre = seleccionar_producto(inventario)
    if nombre is None:
        return

    confirmar = input(f"¿Está seguro de que desea eliminar '{nombre.capitalize()}'? Esta acción es permanente. (s/n): ").lower()
    
    if confirmar == 's':
        del inventario[nombre]
        if nombre in carrito:
            del carrito[nombre]
        print(f"\n¡Producto '{nombre.capitalize()}' eliminado con éxito!")
    else:
        print("Eliminación cancelada.")
# Se crea función para agregar producto al carrito
def agregar_al_carrito():
    print("\n--- AGREGAR AL CARRITO ---")
    nombre = seleccionar_producto(inventario)
    if nombre is None:
        return

    stock_disponible = inventario[nombre]['stock']
    
    if stock_disponible == 0:
        print(f"Lo sentimos, '{nombre.capitalize()}' está agotado.")
        return

    print(f"Stock disponible de '{nombre.capitalize()}': {stock_disponible}")
    
    cantidad = obtener_entrada_numerica(
        "¿Cuántas unidades desea agregar?: \n--> ", 
        tipo_dato=int, 
        minimo=1
    )
    
    if cantidad > stock_disponible:
        print(f"Error: Solo hay {stock_disponible} unidades disponibles.")
        return

    carrito[nombre] = carrito.get(nombre, 0) + cantidad
    print(f"\n¡Agregados {cantidad} x '{nombre.capitalize()}' al carrito!")
# Se crea función para mostrar el carrito de compras
def mostrar_carrito():
    print("\n--- MI CARRITO DE COMPRAS ---")
    if not mostrar_lista_productos(carrito):
        print("El carrito está vacío.")
        return 0

    total = 0
    for nombre, cantidad in carrito.items():
        total += inventario[nombre]['precio'] * cantidad
    
    print("---------------------------------")
    print(f"TOTAL A PAGAR:      ${total:>10.2f}")
    return total
# Se crea función eliminar producto del carrito
def eliminar_del_carrito():
    print("\n--- ELIMINAR DEL CARRITO ---")
    nombre = seleccionar_producto(carrito)
    if nombre is None:
        return

    cantidad_en_carrito = carrito[nombre]
    print(f"Tiene {cantidad_en_carrito} unidad(es) de '{nombre.capitalize()}'.")
    cantidad_a_eliminar = obtener_entrada_numerica(
        "¿Cuántas unidades desea eliminar? (0 para cancelar): \n--> ",
        tipo_dato=int,
        minimo=0
    )

    if cantidad_a_eliminar == 0:
        print("Eliminación cancelada.")
    elif cantidad_a_eliminar >= cantidad_en_carrito:
        del carrito[nombre]
        print(f"Se eliminó '{nombre.capitalize()}' completamente del carrito.")
    else:
        carrito[nombre] -= cantidad_a_eliminar
        print(f"Se eliminaron {cantidad_a_eliminar} unidad(es). Quedan {carrito[nombre]}.")
# Se crea función para realizar compra del producto o productos
def realizar_compra():
    print("\n--- FINALIZAR COMPRA ---")
    total = mostrar_carrito()
    if total == 0:
        print("No puede comprar un carrito vacío.")
        return

    confirmar = input(f"¿Desea pagar ${total:.2f}? (s/n): ").lower()
    
    if confirmar == 's':
        for nombre, cantidad in carrito.items():
            inventario[nombre]['stock'] -= cantidad
            
        carrito.clear()
        
        print("\n¡Gracias por su compra!")
        print("El stock ha sido actualizado y su carrito está vacío.")
    else:
        print("Compra cancelada.")
# Se crea función para mostrar el menú del administrador
def menu_administrador():
    while True:
        print("\n---- 🛠️ MENÚ ADMINISTRADOR ---- ")
        print("1. Ver Inventario Completo")
        print("2. Agregar Producto")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Volver al Menú Principal")
        
        opcion = input("\nDigite una opción: \n--> ")
        
        if opcion == '1':
            mostrar_lista_productos(inventario)
        elif opcion == '2':
            agregar_producto_inventario()
        elif opcion == '3':
            actualizar_producto_inventario()
        elif opcion == '4':
            eliminar_producto_inventario()
        elif opcion == '5':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")
# Se crea función para mostrar el menú para los clientes
def menu_cliente():
    while True:
        print("\n---- 🛒 MENÚ CLIENTE ---- ")
        print("1. Ver Productos Disponibles")
        print("2. Agregar Producto al Carrito")
        print("3. Ver mi Carrito")
        print("4. Eliminar Producto del Carrito")
        print("5. Pagar y Finalizar Compra")
        print("6. Volver al Menú Principal")
        
        opcion = input("\nDigite una opción: \n--> ")
        
        if opcion == '1':
            mostrar_lista_productos(inventario)
        elif opcion == '2':
            agregar_al_carrito()
        elif opcion == '3':
            mostrar_carrito()
        elif opcion == '4':
            eliminar_del_carrito()
        elif opcion == '5':
            realizar_compra()
        elif opcion == '6':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida.")
# Se crea función main para contener los menus creados
def main():
    while True:
        print("\n====== TIENDA ONLINE TECH ======")
        print("1. Modo Cliente (Comprar)")
        print("2. Modo Administrador (Inventario)")
        print("3. Salir")
        
        opcion = input("\nSeleccione un modo: \n--> ")
        
        if opcion == '1':
            menu_cliente()
        elif opcion == '2':
            menu_administrador()
        elif opcion == '3':
            print("Hasta la próxima...\n")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
# Aqui aseguramos que solo se ejecute cuando main es llamado directamente
if __name__ == "__main__":
    main()