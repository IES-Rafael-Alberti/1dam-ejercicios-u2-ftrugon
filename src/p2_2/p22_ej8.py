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
    linea = ""
    while cont < numero:
        linea =f"{nume1}" + f" {linea}" 
        print(linea)
        nume1 += 2
        cont += 1
    return linea


def main():
    
    numero = numeserie()
    escalera(numero)

if __name__ == "__main__":
    main()

"""
BUCLE FOR EJEMPLO DE CESAR 

for i in range(0, numero +1)
    for j in range(2 * 1 - 1,0,-2)
        print(j,end=" ")
    print()
"""