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


# ! ----------------------------------------------
# ! Módulos y paquetes
# ! ----------------------------------------------

# Modulos
# Un módulo es un archivo que puede contener una funcionalidad o varias.

# Paquetes 
# Los paquetes nos permite agrupar módulos

# ! ----------------------------------------------
# ! Objetos
# ! ----------------------------------------------

# Crear una clase Persona

class Persona:
    
    # Método constructor -> Que se ejecuta siempre que haga un new (Siempre que cree una instancia) -> El new no existe
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, soy {self.nombre}")
        
        
persona1 = Persona("Romina", 25)
persona2 = Persona("Nicolas", 30)

persona1.saludar()
persona2.saludar()

# Otra clase más para poder crear objetos

class Rectangulo: 
    
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)
    
rectangulo1 = Rectangulo(10, 5)
rectangulo2 = Rectangulo(8, 4)

print("Area rectangulo 1: ", rectangulo1.calcular_area())
print("Area rectangulo 2: ", rectangulo2.calcular_area())
print("Perímetro rectangulo 1: ", rectangulo1.calcular_perimetro())
print("Perímetro rectangulo 2: ", rectangulo2.calcular_perimetro())


