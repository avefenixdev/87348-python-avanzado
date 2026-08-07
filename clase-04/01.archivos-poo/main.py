print("Clase 04")

print("# ! Lanzar una excepcón con raise")
# Hasta ahora vimos cómo capturar excepciones
# Queremos lanzar -> generar nosotros la excepción

def validar_edad(edad):
    
    if edad < 0:
        raise ValueError("La edad no puede ser negativa") # break
    
    return edad


try: 
    edad = validar_edad(-55)
    print(edad)
except ValueError as error:
    print('ERROR: ', error)

print("# ! ARCHIVOS")

""" 
open() 
"""

""" archivo = open("datos.txt") """

def escribir_archivo(texto):
    
    with open("datos.txt", "w") as archivo:
        archivo.write(texto)
        
#  escribir_archivo("Hola Python!")

def leer_archivo():
    with open("datos.txt", "r") as archivo:
        contenido= archivo.read()
    
    print(contenido)
    
leer_archivo()

def escribir_varias_lineas():
    with  open("alumnos.txt", "w") as archivo:
        archivo.write("Laura\n")
        archivo.write("Juan\n")
        archivo.write("Pedro\n")
        
# escribir_varias_lineas()

def leer_linea_a_linea():
    with open("alumnos.txt", "r") as archivo:
        
        for linea in archivo:
            print(linea.strip())

# leer_linea_a_linea()

def agregar_contenido_al_archivo(): 
    with open("alumnos.txt", "a") as archivo:
        archivo.write("Maria\n")
        
# agregar_contenido_al_archivo()

# -----------------------------
# Desafío con archivos
# -----------------------------

# Crear un programa que solicite una persona

# - Nombre
# - Edad
# - Ciudad

# > archivo -> persona.txt

# El archivo debe contenedor lo siguiente:

# Nombre: Romina
# Edad: 25
# Ciudad: Buenos Aires

# Segunda etapa -> leer el archivo y mostrar esos datos



