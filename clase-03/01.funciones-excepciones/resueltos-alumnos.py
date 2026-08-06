# Gaston
def promedio(*argumentos):
    return sum(argumentos) / len(argumentos)

print("promedio de 2,5,8,9,20,44:", promedio(2,5,8,9,20,44))
print("promedio de 43,21,54,99:", promedio(43,21,54,99))
print("promedio de 12,27,34:", promedio(12,27,34))

# Diego
def promedio(*argumentos):
    print("---->",argumentos)
    return sum(argumentos) / len(argumentos)

print(f"El promedio es: {promedio(2, 5, 8, 9, 20, 44)}")
print(f"El promedio es: {promedio( 43, 21, 54, 99)}")
print(f"El promedio es: {promedio( 12, 27, 34)}")

# Luca
lista1= [2,5,8,9,20,44]
lista2= [43,21,54,99]
lista3= [12,27,34]
def promedio(*args):
    return sumar(*args) / len(args)
print("-------------- Promedios ---------------")
print(promedio(*lista1))
print(promedio(*lista2))
print(promedio(*lista3))

# Julio
def promedio(*args):
    total, cant, nombre = 0, 0, 'Maxi'
    
    for numero in args:
        total += numero
        cant += 1
        
    return total/cant
    
print(promedio(2,3,5,7,8))
print(promedio(2,3,4))

# Beta
print("Bienvenidos a la maquina del chambeo")
def sacar_promedio(*numeros):
    promedio= sum(numeros) / len(numeros)
    return promedio
clima = sacar_promedio(2, 5, 8, 9, 20, 44)
print(f"El promedio del clima esta temporada fue: {clima}°C")
pesos = sacar_promedio(43, 21, 54, 99)
print(f"Las personas aqui reunidas tienen un peso que ronda en: {pesos}")
edades = sacar_promedio(12, 27, 34)
print(f"El promedio de las edades de la familia Martinez es de: {edades}")

## -------------------------------------------------------
## -------------------------------------------------------

# Luca
nombre = input("Ingresar nombre: ")
edad = int(input("Ingresar edad: "))
ciudad = input("Ingresar ciudad: ")
profesion = input("Ingresar profesión: ")

def crear_perfiles(**usuarios):
    print(usuarios)
    
crear_perfiles(nombre= nombre,
               edad= edad,
               ciudad= ciudad,
               profesion = profesion)

notas= []
for i in range(3):
    notas.append(int(input(f"Ingresar nota {i+1}:")))
def calcular_promedio(*notas):
    return sum(notas)/len(notas)
print(calcular_promedio(*notas))

# Julio

def mostrarDatos(*notas, **user ):
    
    print("Usuarios -> ", user) 
    print("Notas -> ", notas) 
    total = 0
    cant = 0
    for numero in notas:
        total += numero
        cant += 1
        
    promedio = total/cant
    print("promedio: ",promedio)
    
mostrarDatos(
    5,6,7,
    nombre="pepe",
    edad=100,
    ciudad="Antartida",
    profesion="Forense"
    )

# Gastón
def crear_perfil(**kwargs):
    print('perfil creado con los datos ->',kwargs)
    
def calculo_de_promedio(*args):
    return sum(args) / len(args)

nombre = input(' ingresa tu nombre: ')
edad = int(input(' ingresa tu edad: '))
ciudad = input(' ingresa tu ciudad: ')
profesion = input(' ingresa tu profesion: ')
crear_perfil(
    nombre=nombre,
    edad=edad,
    ciudad=ciudad,
    profesion=profesion 
)
nota1 = float(input(' ingresa tu primera nota: '))
nota2 = float(input(' ingresa tu segunda nota: '))
nota3 = float(input(' ingresa tu tercera nota: '))
promedio = calculo_de_promedio(nota1, nota2, nota3)
print("---------Perfil---------")
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)
print("Profesión:", profesion)
print("Promedio:", promedio)
print("------------------------")
print('promedio de las notas:', promedio)

# Diego

def crear_perfil(**perfil):
    print("Perfil: ",perfil)
def promedio(*notas):
    print(f"el promedio es: {sum(notas) / len(notas)}")
crear_perfil(
    nombre=input("Ingrese nombre: "),
    edad = int(input("Ingrese la edad: ")),
    cuidad = input("Ingrese la cuidad: "),
    profesion = input("Ingrese la profesion: ")
)
promedio(
    int(input("Ingrese la primera nota: ")),
    int(input("Ingrese la segunda nota: ")),
    int(input("Ingrese la tercera nota: "))
)