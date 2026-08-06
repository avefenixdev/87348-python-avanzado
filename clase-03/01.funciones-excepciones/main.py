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






