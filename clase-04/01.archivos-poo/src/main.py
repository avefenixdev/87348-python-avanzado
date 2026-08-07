# from operaciones import sumar, restar, multiplicar
# ! ===============================
from operaciones import *
# ! ===============================

# ! -------------------------------------------------
""" from utilidades.calcular_promedio import calcular_promedio
from utilidades.contar_caracteres import contar_caracteres """
# ! -------------------------------------------------

# ! ////////////////////////////////////////////////////
""" import operaciones

resultado = operaciones.sumar(10, 5)
print(resultado)

print(operaciones.restar(8, 5))
print(operaciones.multiplicar(8, 5)) """
# ! ////////////////////////////////////////////////////

# ! ===============================
print(sumar(10, 2))
print(restar(7, 2))
print(multiplicar(9, 2))
# ! ===============================

# ! -------------------------------------------------
""" texto = "Python"
notas = [ 8, 7, 9]

print(contar_caracteres(texto))
print(calcular_promedio(notas)) """
# ! -------------------------------------------------

import utilidades

promedio = utilidades.calcular_promedio([8, 7, 9])
cantidad = utilidades.contar_caracteres("Python")

print(promedio)
print(cantidad)