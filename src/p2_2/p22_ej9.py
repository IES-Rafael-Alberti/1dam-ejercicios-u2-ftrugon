def comprobrar(pwd):
    comprobado = input("Escribe la contraseña: ")
    while comprobado != pwd:
        comprobado = input("Contraseña incorrecta, Escribe la contraseña de nuevo: ")
    return comprobado

def main():
    pwd = input("Escribe tu contraseña: ")
    comprobrar(pwd)


if __name__ == "__main__":
    main()
