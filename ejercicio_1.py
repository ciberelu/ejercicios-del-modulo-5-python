import math
## programa para sacar area de un triangulo

def areaTriangulo(base, altura):
    return (base *altura)/ 2
print(f" area de triangulo: {areaTriangulo(20, 30)}")

# programa para sacar area de un circulo
def areaCirculo(radio):
    return math.pi * (radio **2) 

print(f"El area del ciruclo es: {areaCirculo(19)}")
