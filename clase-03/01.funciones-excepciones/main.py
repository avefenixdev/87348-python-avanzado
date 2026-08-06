print("Clase 03")

print("# ! Funciones normales")

def recibe_argumentos(num1, num2, num3, num4): 
    print(num1)
    print(num2)
    print(num3)
    print(num4)

recibe_argumentos(5, 9, 7, 4)

print("# ! Funciones con *args")

def sumar(*argumentos): # args
    total = 0
    print("----------->  ", argumentos)    
    for numero in argumentos:
        total += numero
    
    return total

print(sumar(10, 20)) # 2
print(sumar(10, 20, 30)) # 3
print(sumar(7, 2, 3, 4, 5, 6, 7, 10)) # 8

# Lista = datos que pueden cambiar -> [] -> mutables
# Tupla = datos que deberían permanecer iguales -> () -> No mutables

# Enunciado -> Promedio variable -> Voy a tener varias listas de numeros y quiero sacar el promedio de todas las listas que tengo -> *args

# -> 2, 5, 8, 9, 20, 44 -> promedio -> [suma de todos los valoes] / [cantidad de elementos]
# -> 43, 21, 54, 99 -> promedio -> 
# -> 12, 27, 34 -> promedio -> 

# 5 minutos para crear una función que recibe una cantidad de argumentos variables y calcular el promedio.

# ----> *args -> argumentos posicionales -> 
# ----> **kwargs -> keyword -> argumentos nombrados -> dic

def mostrar_usuarios(**datos):
    print(datos) # <---- dic -> kwargs recibe los argumentos como diccionarios
    

mostrar_usuarios(
    nombre="Laura",
    edad=25,
    activo=True
)

# Ejemplo *args + **kwargs

def registrar_evento(*usuarios, **datos):
    print("Usuarios -> ", usuarios) # <---- tupla
    print("Datos -> ", datos) # <---- dic

registrar_evento(
    "Lorena",
    "Ana",
    "Silvina",
    fecha="2026-08-06",
    lugar="Buenos Aires"
)

# Desafío integrador
# El programa debe pedir lo siguiente:
""" 
1. Pedir el nombre.
2. Pedir edad.
3. Pedir ciudad.
4. Pedir profesión.
5. Crear el perfil usando **kwargs
6. Pedir 3 notas
7. Calcular el promedio utilizando *args
8. Mostrar todos los datos """

# 8 minutos -> para realizar este ejercicio

""" def crear_perfil(**perfil):
    print("\nPerfil creado:")
    for clave, valor in perfil.items(): # py despaquetar -> destructurando en js
        print(f"{clave}: {valor}")
    
def promedio(*notas):
    return sum(notas) / len(notas)
    
# Crear perfil
nombreInput = input('Ingrese nombre: ')
edadInput = int(input('Ingrese la edad: '))
ciudadInput = input('Ingrese la ciudad: ')
profesionInput = input('Ingrese la profesión: ')

crear_perfil(
    nombre=nombreInput,
    edad=edadInput,
    ciudad=ciudadInput,
    profesion=profesionInput
)

# Ingresar notas
notas = []

while True:
    nota = float(input("Ingrese una nota: "))
    notas.append(nota)
    
    # Bandera
    continuar = input('¿Desea ingresar otra nota(s/n): ')
    
    if continuar.lower() != "s":
        break
    
# Mostrar promedio
print(f"\n El promedio es: {promedio(*notas):.2f}") """

# ! ---------------------------------------------
# ! ---------------------------------------------

print("# ! Funciones anónimas -> sin usar def")

# anatomía de una función lambda
# lambda parametros: expresión

doble = lambda numero: numero * 2

print(doble(5)) # 10

# Dos parámetros
sumar = lambda a, b : a + b
print(sumar(10, 20))

# lambdas y cadenas

obtener_logitud = lambda texto: len(texto)
print(obtener_logitud("Python"))

# Lambdas para ordenar

personas = [
    { "nombre": "Ana", "edad": 30 },
    { "nombre": "Juan", "edad": 20 },
    { "nombre": "Pedro", "edad": 25 }
]

personas.sort(key=lambda persona: persona["edad"])

print(personas)

# Funciones de orden superior ->> recibe otra funcion como argumneto o devuelve una función

def aplicar(callback, numero):
    return callback(numero)

def doble(numero):
    return numero * 2 

def triple(numero):
    return numero * 3

resultado = aplicar(lambda n: n * 2, 10) # 20
print(resultado)
resultado = aplicar(triple, 10) # 30
print(resultado)

# map()

numeros = [1, 2, 3, 4, 5]

dobles = map(lambda num: num * 2, numeros) # devuelve una lista de la misma cantidad de elementos de la original

print(list(dobles))

# filter

pares = filter(lambda numero: numero % 2 == 0, numeros) # devuelve una lista de solo los elementos que coincinda con lo que se haya decidido en el callback

print(list(pares))

print("# ! Excepciones")
# Un programa puede encontrarse con situaciones inesperadas

# * El usuario introduce texto cuando esperamos un número
# * Un archivo no existe
# * Intentamos dividir por cero.
# * Accedemos a una posición inexistente.
# * Una clave no existe en un diccionario.

print('Inicio del programa')
numero = 10
divisor = 0 # ZeroDivisionError

# resultado = numero / divisor

try:
    resultado = numero / divisor
except ZeroDivisionError:
    print("No se puede dividir por cero")

print('Fin del programa')

# Casteo inválido

try:
    edad = int(input("Ingrese su edad: "))
    print(edad)
except ValueError:
    print('Debe ingresar un número')
    
# Varias excepciones

try: 
    numero = int(input("Número: "))
    resultado = 100 / numero
    
    print(f"{resultado:.2f}")
except ValueError:
    print("Debe ingresar un número")
    
except ZeroDivisionError:
    print("El número no puede ser cero")
    
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

def cargar_producto():
    print("cargar_producto")

def mostrar_productos():
    print("mostrar_productos")
    
def buscar_producto(nombre):
    print("buscar_producto")
    
def calcular_precio_final(precio, descuento):
    print("calcular_precio_final")
    return 0


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