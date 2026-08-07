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