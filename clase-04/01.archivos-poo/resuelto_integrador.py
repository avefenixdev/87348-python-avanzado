# Desafío integrador
# Gestión de productos

# La idea es crear un pequeño programa que permita:

# * Agregar un producto.
# * Guardarlos en una lista de diccionario
# * Mostrar productos
# * Calcular precios con lambda
# * Manejar error con try/except
# * usar funciones.
# * Practicar *args y **kwargs
""" 
El programa va a tener un menú 

1. Agregar producto
2. Mostrar productos
3. Buscar producto (no es obligatorio -> punto extra)
4. Calcular precio con descuento (no es obligatorio -> punto extra)
5. Salir

"""

# Programa principal

# menu()
# agregar_producto(**producto)
# mostrar_productos()
# descuento_aplicado = calcular_precio_final(precio, descuento)
# buscar_producto(nombre) -> Muestra en terminal el producto encontrado o no se encontró el producto
# cargar_producto() -> input(Nombre), input(Precio), input(Stock)

productos = []

def agregar_producto(**producto):
    productos.append(producto)
    print("Producto agregado correctamente")

def cargar_producto():
    try:
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        
        if precio < 0:
            print("El precio no puede ser negativo")
            return # break
    
        if stock < 0:
            print("El stock no puede ser negativo")
            return # break
            
        agregar_producto(
            nombre=nombre,
            precio=precio,
            stock=stock
        )
        
        
    except:
        print("Error: debes ingresar números válidos")

def mostrar_productos():
    if len(productos) == 0:
        print("No hay productos cargados.")
        return 
    
    print("\n--- PRODUCTOS ---")
    
    for producto in productos:
        print(
            f"Nombre: {producto['nombre']} | "
            f"Precio: {producto['precio']} | "
            f"Stock: {producto['stock']}"
        )
    
def buscar_producto(nombre):
    print(nombre)
    
    encontrados = list(
        filter(lambda producto: producto["nombre"].lower() == nombre.lower(), productos)
    )
    
    if len(encontrados) == 0:
        print("Producto no encontrado.")
    else: 
        for producto in encontrados:
            print(producto) 
    
def calcular_precio_final(precio, descuento):
    aplicar_descuento = lambda precio: precio - (precio * descuento / 100)
    # print(type(aplicar_descuento))
    precio_con_descuento = aplicar_descuento(precio)
    return precio_con_descuento

def menu():
    
   while True: 
        print("""
           --- MENÚ ---
           
           1. Agregar producto
           2. Mostrar productos
           3. Buscar producto 
           4. Calcular precio con descuento
           5. Salir
           
                 
           """)
           
        try:
            opcion = int(input("Selecione una opción: "))
                    
            match opcion:
                case 1:
                    cargar_producto()
                case 2: 
                    mostrar_productos()
                case 3:
                    nombre = input("Nombre a buscar: ")
                    buscar_producto(nombre) 
                case 4:
                    # si el usuario me ingresa una cadena
                    try: 
                        precio = float(input("Precio: "))
                        descuento = float(input("Descuento (%): "))
                        
                        precio_final = calcular_precio_final(
                            precio,
                            descuento
                        )
                        
                        print(f"Precio final: ${precio_final:.2f}")
                    except ValueError:
                        print("Debes ingresar valores númericos")
                case 5:
                    print("Programa finalizado.")
                    break
                    
                case _:
                    print("Opción incorrecta.")
        except ValueError:
            print("Debes ingresar un número")
    
menu()