nombre = input("Nombre: ")
producto = input("Producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

# Diccionario
compra = {
    "cliente": nombre,
    "producto": producto,
    "precio": precio,
    "cantidad": cantidad
}

# print(compra)
subtotal = compra["precio"] * compra["cantidad"]

if subtotal >= 50000:
    descuento = subtotal * 0.10
    obtuvo_descuento = True # creo una bandera que me va a servir para mostrar el mensaje en el futuro de que se pudo hacer el descuento
else: 
    descuento = 0
    obtuvo_descuento = False
    
total = subtotal - descuento

# 8. Mostrar un resumen de la compra
# 9. Informar si el cliente obtuvo descuento

print("=========== RESUMEN DE COMPRA ========\n")
# print()
print(f"Cliente: {compra['cliente']}")
print(f"Producto: {compra['producto']}") 
print(f"Precio unitario: ${compra['precio']:.2f}") 
print(f"Cantidad: {compra['cantidad']}") 
print(f"Subtotal: ${subtotal:.2f}") 
print(f"Descuento: ${descuento:.2f}") 
print(f"Total: ${total:.2f}") 

if obtuvo_descuento: 
    print('Obtuviste un descuento!')
else:
    print('No aplicó el descuento')

