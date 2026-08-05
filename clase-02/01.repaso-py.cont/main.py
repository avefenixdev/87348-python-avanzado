
""" 
Crear un programa en Python que simule el registro de una compra

El programa debe:

1. Pedir al usuario su nombre (almaccenarlo en una variable) -> input()
2. Pedir el producto que desea comprar. -> input()
3. Pedir el precio unitario. -> input()
4. Pedir la cantidad. -> input()
5. Guardar los datos de la compra en un diccionario.
6. Calcular el subtotal
7. Si el subtotal es mayor o igual a $50.000, aplicar un 10% de descuento
8. Mostrar un resumen de la compra
9. Informar si el cliente obtuvo descuento

# ------------- #
Nombre: Ana
Producto: Teclado
Precio: 35000
Cantidad: 2

=========== RESUMEN DE COMPRA ========

Cliente: Ana
Producto: Teclado
Precio unitario: $35000
Cantidad: 2
Subtotal: $70000
Descuento: 10% si supera los $50000
Total: $63000

Obtuviste un descuento
"""

print('# ! Colecciones')

""" 
list -> [10, 20, 30] -> Ordenada y mutable (array de javascript)
tuple -> (10, 20, 30) -> Ordenada e inmutable
set -> {10, 20, 30} -> No admite duplicados 
dict -> {"nombre": "Ana"} -> Clave -> valor (objeto de javascript)
"""

""" 
--- # ! estructuras de control
if
if / else
if / elif / else
--- # ! estructuras de repetición
for
while
---
break
continue
"""

# Prueba de escritorio -> 2 y con 5
# numero -> 2 -> No se va a imprimir
# numero -> 5 -> Se imprime el valor
for numero in range(1, 11):
    
    if numero % 2 == 0:
        # print('par -> ', numero)
        continue
    
    print(numero)

# Aplicación de Datos personales
# Pedir al usuario

# -> nombre
# -> edad
# -> altura

# Mostrar el tipo de dato ingreado

""" 
print()
input()
type()
len()
int()
float()
str()
bool()
range()
sum()
min()
max()
"""

## Ejercicio 2: Crear un array (lista) de notas

# notas = [2, 4] con 5 o 6 notas

# Calcular

# * Cantidad de notas
# * Suma
# * Nota mínima
# * Nota máxima
# * promedio





