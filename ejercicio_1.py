import math


def areaTriangulo(base, altura):
    base = (base * altura)/2
    return base

resultado = areaTriangulo(20, 30)
print(resultado)

def areaCirculo(radio):
    resultado = math.pi * (radio *radio) 
    return resultado 

resultadoCirculo = areaCirculo(19)
print(resultadoCirculo)
