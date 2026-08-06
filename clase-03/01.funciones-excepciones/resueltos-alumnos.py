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
