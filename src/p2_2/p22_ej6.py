def estrellas(numeestre):
    if numeestre < 0:
        print("el numero tiene que ser positivo")
        return "el numero tiene que ser positivo"
    cont = 0
    linea = ""
    while cont < numeestre:
        cont += 1
        linea = linea + "*"
        print(linea)
    return linea


def main():
    numeestre = int(input("dime asta el numero de estrellas que quieres que se cree: "))
    estrellas(numeestre)
    
if __name__ == "__main__":
    main()

"""
caracter = "*"
for i in range(1,numestre +1)
    print(caracter * i)
"""