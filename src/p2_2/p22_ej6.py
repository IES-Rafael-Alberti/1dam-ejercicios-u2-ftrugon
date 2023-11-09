def estrellas(numeestre):
    if numeestre < 0:
        print("el numero tiene que ser positivo")
    cont = 0
    linea = ""
    while cont <= numeestre:
        print(linea)
        linea = linea + "*"
        cont += 1



def main():
    numeestre = int(input("dime asta el numero de estrellas que quieres que se cree: "))
    estrellas(numeestre)
    
if __name__ == "__main__":
    main()
