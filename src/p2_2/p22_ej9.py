def comprobrar(pwd):
    comprobado = input("Para iniciar sesion escribe la contraseña: ")
    while comprobado != pwd:
        comprobado = input("Contraseña incorrecta, Escribe la contraseña de nuevo: ")
    else:
        print("Iniciando sesion")
    return comprobado

def main(): 
    pwd ="asd"
    #pwd = input("Escribe tu contraseña: ")
    comprobrar(pwd)


if __name__ == "__main__":
    main()
