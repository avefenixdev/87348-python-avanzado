# Luca

nombreInput= input("Ingresar nombre: ")
try:
    edadInput = int(input("Ingresar edad: "))
except ValueError:
    print("Edad ingresada inválida!")
ciudadInput = input("Ingresar ciudad: ")
def escribir_archivo():
    with open("ejercicio.txt","w") as archivo:
        archivo.write(
            f"Nombre: {nombreInput}\n"
            f"Edad: {edadInput}\n"
            f"Ciudad: {ciudadInput}\n"
            )
def leer_linea_a_linea():
    with open("ejercicio.txt","r") as archivo:
        for linea in archivo:
            print(linea.strip())
escribir_archivo()
leer_linea_a_linea()

# Valentina
nombre = input("Nombre: ")
edad = input("Edad: ")
ciudad = input("Ciudad: ")
def escribir_archivo(nombre,edad,ciudad):
    
    with open("persona.txt", "w") as archivo:
        archivo.write(" Nombre: " + nombre + "\n")
        archivo.write(" edad: " + edad + "\n" )
        archivo.write(" ciudad: " + ciudad + "\n")

def leer_linea_a_linea():
    with open("persona.txt", "r") as archivo:
        
        for linea in archivo:
            print(linea.strip())

escribir_archivo(nombre,edad,ciudad)
leer_linea_a_linea()