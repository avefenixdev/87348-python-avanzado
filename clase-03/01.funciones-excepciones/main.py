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



