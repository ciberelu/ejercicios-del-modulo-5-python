
def encontrarPrimo():
    numero = int( input("por favor ingrese un numero y le diremos si es primo o no lo es"))

    if numero > 1:
        for i in range (2, numero):
            if (numero % i ) == 0:
                return (f"lo siento el numero {numero} no es primo es divisible en {i}")
                break
        else:
            return ("es primo")
    else:
        return ("ingrese un numero mayor a 1")
        
print(encontrarPrimo())

