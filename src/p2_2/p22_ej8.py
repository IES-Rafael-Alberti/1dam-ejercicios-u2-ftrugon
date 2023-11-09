def numeserie():
    numero = input("Dime el numero de la serie: ")
    if numero.isnumeric() == True:
        numero = int(numero)
    else:
        print("Tienes que poner un numero y positivo")
    return numero

def escalera(numero):
    cont = 0
    nume1 = 1
    linea = f"{nume1}"
    while cont < numero:
        print(linea)
        nume1 += 2
        linea = linea + f" {nume1}"
        cont += 1
    
def main():
    
    numero = numeserie()
    escalera(numero)


if __name__ == "__main__":
    main()
