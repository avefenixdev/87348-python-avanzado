# Beta

print("Bienvenido a Himalaya")
def pedir_datos():
    nombre = input("¿Cómo quieres que te llamemos?: ")
    edad = int(input("¿Qué edad tienes?: "))
    altura = float(input("¿Cuánto mides? (No me juzgues pidió que lo preguntara Maxi, el es un poco rarito pero buena gente): "))
    return {
        "nombre": nombre,
        "edad": edad,
        "altura" : altura
    }
def mostrar_tipo(datos):
    print (f"Tu nombre: {datos["nombre"]} y su tipo: {type(datos["nombre"])}")
    print(f"Tu edad: {datos["nombre"]} y su tipo: {type(datos["edad"])}")
    print(f"Tu altura: {datos["nombre"]} y su tipo: {type(datos["altura"])}")
datos = pedir_datos()
mostrar_tipo(datos)

# Dani

def datos_personales():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura: "))
    return {
        "nombre": nombre,
        "edad": edad,
        "altura": altura
    }
usuario = datos_personales()
def mostrar_datos(usuario):
    print("====== DATOS PERSONALES DEL USUARIO ======\n")
    print(f"Nombre: {usuario['nombre']} \nTipo de dato: {type(usuario['nombre'])}")
    print(f"Edad: {usuario['edad']} \nTipo de dato: {type(usuario['edad'])}")
    print(f"Altura: {usuario['altura']} \nTipo de dato: {type(usuario['altura'])}")
mostrar_datos(usuario)

# Ejercicio 2
def calcular_notas():
    notas = [2, 4, 5, 6, 9, 10]
    cantidad_notas = len(notas)
    suma = sum(notas)
    nota_minima = min(notas)
    nota_maxima = max(notas)
    promedio = suma / cantidad_notas
    print("===== NOTAS =====\n ")
    print("Cantidad de notas: ", cantidad_notas)
    print("Suma de notas: ", suma)
    print("Nota mínima: ", nota_minima)
    print("Nota máxima: ", nota_maxima)
    print("Promedio de notas: ", promedio)
calcular_notas()

# luca

# Ejercicio 1

def datos_personales():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    altura = float(input("Ingrese su altura: "))
    return {
        "usuario":nombre,
        "edad": edad,
        "altura": altura,
    }
datos = datos_personales()
print(f"Tipo de dato del nombre: {type(datos['usuario'])}")
print(f"Tipo de dato de la edad: {type(datos['edad'])}")
print(f"Tipo de dato de la altura: {type(datos['altura'])}")


## Ejercicio 2:
notas = [7,4,8,10,9,2]
print(f"Cantidad de notas: {len(notas)}")
print(f"Sumatoria de notas: {sum(notas)}")
print(f"Nota mínima: {min(notas)}")
print(f"Nota maxima: {max(notas)}")
print(f"Promedio:  {sum(notas)/len(notas)}")

# Ejercicio 3
# Pedir una palabra y dar la cantidad de caracteres
palabra = input("Ingresar palabra: ")
print(f"Longitud de la palabra ingresada: {len(palabra)}")

# Ejercicio 4
edad_actual = int(input("Ingresar edad: "))
print(f"En 10 años tendrás {edad_actual+10} años")

# Ejercicio 5
# Dar numeros del 1 al 10 usando una función integrada
lista = range(1,11,1)
print(list(lista))