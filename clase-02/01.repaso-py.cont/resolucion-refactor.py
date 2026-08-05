# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------
# ---------------------------------------------

def solicitar_datos():
    nombre = input("Nombre: ")
    producto = input("Producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    # Diccionario
    return { # retonar un diccionario
        "cliente": nombre,
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad
    }
    
def calcular_subtotal(compra):
    return compra['precio'] * compra['cantidad']

def calcular_descuento(subtotal):
    if subtotal >= 50_000:
        return subtotal * .10

    return 0

def calcular_total(subtotal, descuento):
    return subtotal - descuento

def mostrar_resumen(compra, subtotal, descuento, total):
    print("=========== RESUMEN DE COMPRA ========\n")
    # print()
    print(f"Cliente: {compra['cliente']}")
    print(f"Producto: {compra['producto']}") 
    print(f"Precio unitario: ${compra['precio']:.2f}") 
    print(f"Cantidad: {compra['cantidad']}") 
    print(f"Subtotal: ${subtotal:.2f}") 
    print(f"Descuento: ${descuento:.2f}") 
    print(f"Total: ${total:.2f}")
    
    if descuento > 0: 
        print('Obtuviste un descuento!')
    else:
        print('No aplicó el descuento')


# Programa principal

compra = solicitar_datos()
print(compra)

subtotal = calcular_subtotal(compra)
print(subtotal)

descuento = calcular_descuento(subtotal)

total = calcular_total(subtotal, descuento)

mostrar_resumen(
    compra,
    subtotal,
    descuento,
    total
)