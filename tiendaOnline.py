# Declaramos nuestra lista de productos
productos = ["laptop", "mouse", "teclado", "audifonos", "monitor"]
# Y tambien la de precios
precios = [2500, 50, 120, 80, 300]
# Y un arreglo para los producto que iran al carrito de compras
carrito = []

# Hacemos una función para mostrar producto
def mostrar_productos():
    print("\nPRODUCTOS DISPONIBLES:")
    for i in range(len(productos)):
        print(f"{i+1}. {productos[i]} - ${precios[i]}")

# Hacemos una función para agregar un producto al carrito
def agregar_al_carrito():
    # Mostramos que productos se tienen
    mostrar_productos()
    try:
        # Aqui el usuario elige el producto
        opcion = int(input("Ingresa el número del producto a comprar: ")) - 1
        # Si la opción del usuario esta en el rango de los productos
        if 0 <= opcion < len(productos):
            # Realiza la adicción al carrito
            carrito.append(precios[opcion])
            print(f"{productos[opcion]} agregado al carrito")
        else:
            # De lo contrario no añade nada al carrito
            print("Opción no válida")
    except ValueError:
        print("Debes ingresar un número válido")

# Hacemos una función para mostrar los productos en el carrito
def mostrar_total():
    if not carrito:
        print("Carrito vacío")
    else:
        total = sum(carrito)
        print(f"Total a pagar: ${total}")

# Hacemos una función para el menú de compras
def menu():
    while True:
        print("\nMENU TIENDA ONLINE TECH")
        print("1. VER PRODUCTOS")
        print("2. AGREGAR PRODUCTO AL CARRITO")
        print("3. VER EL TOTAL A PAGAR")
        print("4. SALIR")
        # Según la opción del usuario el programa ejecuta
        try:
            opcion = int(input("Digite la opción: "))
            if opcion == 1:
                mostrar_productos()
            elif opcion == 2:
                agregar_al_carrito()
            elif opcion == 3:
                mostrar_total()
            elif opcion == 4:
                print("¡Hasta la próxima!")
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Debes ingresar un número.")

# Llamamos la función menú       
menu()