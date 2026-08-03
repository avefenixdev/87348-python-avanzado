print("Hola mundo!")

""" 
! Python es un lenguaje:

* Alto nivel.
* Interpretado.
* Dinámicamente tipado.
* Sintaxis sencilla.
* Multiproposito -> Inicialmente se usaba para scripting
* Gran comunidad.

! Nos permite hacer

* Desarrollo Web
* Ciencia de datos
* Scripting (Administración de sistema)
* Backend
* Cyber Seguridad
* Video Juegos
* Automatizaciones
* Inteligencia artificial
* App de escritorio
"""

""" Print -> Permite imprimir en terminal/consola """

print("Hola tarolas")

print(10 + 20)

nombre = "Maxi"
version = 3

print(nombre)
print(version)

""" IMPORTANTE: El programa al ser interpretado. Las instrucciones se ejecutan de arriba para abajo y de izquierda a derechas.  """

""" VARIABLES """

nombre = "Luis"; """ cadena """
edad = 22; """ numero entero """
altura = 1.80; """ numero decimal """

""" Podemos en Python cambiar el valor de la variable """

""" ! Reasignación """

print(edad)
edad = 23
print(edad)
edad = 24
print(edad)

contador = 0

contador = contador + 1
contador = contador + 1

print(contador); """ 2 """

contador += 1

print(contador); """ 3 """

print(""" Entada de datos por el usuario """)

nombre = input("Ingrese su nombre: ")

print("Hola", nombre)
print(f"Hola, {nombre}!") # <-----
print("Hola %s" % nombre)

""" Ingrese la edad """

edad_input = input("Edad: ")
print(type(edad_input)) # cadena
print(edad_input)

""" ¿Cómo averiguo el tipo de dato de una variable? """

""" Casteando la edad """

edad_ingresada = int(input("Edad: "))
print(type(edad_ingresada)) # número
print(edad_ingresada)

""" ¿Qué tipos de datos tiene Python? """

""" 
* int
* float
* str
* bool
* None

type()
"""

cantidadad_alumnos = 50
precio = 33.30

print(type(cantidadad_alumnos)) # entero -> int
print(type(precio)) # flotante -> float

print("! Cadenas")

producto = 'PC Gamer'
memoria = 16

producto_caracteristicas = f"{producto} con {memoria}gb"

print(producto_caracteristicas)

edad = 55

es_mayor = edad >= 18

print(es_mayor) # True

"""
! Listas -> (list) -> Guardan varios valores en un orden fijo -> []

! Tuplas (tuple) -> Son parecidas a la listas pero tiene un orden y aceptan repetidos -> () 

! Diccionarios (dict) -> Guardan datos en parejas de clave, valor. No siguen un orden especifico {}

! Conjuntos (set) -> Guardan elementos únicos sin orden. No permiten que se repita un valor. -> {}
"""

print('LISTAS')

frutas = ["manzanas", "bananas", "pera"]

print(frutas)
print(frutas[2])
print(frutas[1])

frutas.append("kiwi")
frutas.append("uva")

print(frutas)

""" Tuplas y sets """
#            0        1       2
colores = ("rojo", "azul", "blanco", "rosa", "amarillo")

print(colores)
print(colores[2])
print(colores[4])

""" La tupla puede contenedor distintos tipos de dato """

persona = ("Max", 30, True)

print(persona[0]) # Max
print(persona[1]) # 30
print(persona[2]) # True

""" ¿Se puede modificar la tupla? """

numeros = (10, 20, 30)

# numeros[0] = 50 # ! No se puede modificar una tupla -> Las tuplas son inmutables

""" ¿Puedo desempaquetar? Si """

persona = ("Max", 22, "Argentina")

nombre, edad, pais = persona # Desestructuración de js. const {nombre, edad, pais} = persona

print(nombre)
print(edad)
print(pais)

# ! set -> es una colección de elementos sin duplicados y sin un orden
# Se puede crear con {} o mediante la set()

colores  = { "rojo", "verde", "azul", "rojo" }
#colores = set("rojo", "verde", "azul", "rojo")
print(colores)

numeros = { 0, -3, 1, 2, 3, 5, 7, -2, 2, 2, 8, 1, 1, 4, -5, -11, 2, 6, 5, 7}
print(numeros)

frutas = {"manzana"}


frutas.add("pera")
frutas.add("manzana")
frutas.add("pera")

print(frutas)

# frutas.remove("banana") # ! si quiero eliminar elementos dentro del set que no existen, KeyError
frutas.remove("pera")
print(frutas)

frutas.add("jamón")
frutas.add("sandia")
frutas.add("mandarina")
frutas.add("mango")
frutas.add("tomate")
frutas.add("melon")

print(frutas)

frutas.discard("chocolate")# No tira error si no es encontrada lo que quiero eliminar
frutas.remove("tomate")

print(frutas)

alumnos_python = { "Ana", "Juan", "Pedro" }
alumnos_java = { "Juan", "Pedro", "Lucía" }

# A partir de 2 sets puedo sacar la intercepción &

print( alumnos_python & alumnos_java )

# A partir de 2 sets puedo scar la unión |

print( alumnos_python | alumnos_java )

# A partir de 2 sets puedo sacar la diferencia -

print( alumnos_python - alumnos_java )
print( alumnos_java - alumnos_python )

print("# ! Operadores... ")

print("# ! aritmeticos")

a = 10
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b) 
print(a // b) # saca decimales. Devuelve el resultado entero
print(a % b) # el resto de la división
print(a ** b) # eleva. potenciación. 10^4

print("# ! Comparación")
# devuelve un booleano luego de hacer la comparacicón
print( a == b) # False
print( a != b) # True
print( a > b) # True -> 10 > 4
print( a < b) # False -> 10 < 4
print( a >= b) # True -> 10 >= 4
print( a <= b) # False -> 10 <= 4

print("Lógicos -> and")
# and | or | not
# ------------------------ AND -> todas premisas deben ser verdaderas para que el resultaod de verdadero
#           False
#      False and True
print(a == b and a != b)
#           True
#       True and True
print(a != b and a > b)

print("Lógicos -> or")
# ----------------------- OR -> Ambas premsisas deben ser falsas para que de como resultado false.
#           False
#      False or False
print(a < b or a <= b)
#          True
#      True or False
print(a != b or a < b)

print("Lógicos -> not")

print(not a != b) # True -> not True -> False

print("Ejemplo de operadores lógicos")

edad = 25
tiene_entrada = True
#                        True
#                  True     and  True
puede_ingresar = edad >= 18 and tiene_entrada
print(puede_ingresar) # True

edad = 15

es_menor = edad < 18
print(es_menor) # True
es_adulto = not es_menor
print(es_adulto) # False

print("Operador in")

frutas = ["manzana", "banana", "kiwi"]

print("pera" in frutas) # False
print("kiwi" in frutas) # True

""" 
Crear un programa en Python que simule el registro de una compra

El programa debe:

1. Pedir al usuario su nombre (almaccenarlo en una variable) -> input()
2. Pedir el producto que desea comprar. -> input()
3. Pedir el precio unitario. -> input()
4. Pedir la cantidad.
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