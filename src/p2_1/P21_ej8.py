def latabla():
    print("Recuerda que estas son las puntuaciones:")
    print("NIVEL -------- PUNTUACION")
    print("Inaceptable -- 0.0")
    print("Aceptable ---- 0.4")
    print("Meritorio ---- 0.6 o más")

def puntuacion():
    print("Dime tu puntuacion, recuerda que solo puede ser 0.0, 0.4 y 0.6 o mas")
    numpunt = float(input("dime el numero: "))
    if numpunt == 0.0:
        return numpunt
    elif numpunt == 0.4:
        return numpunt
    elif numpunt >= 0.6:
        return numpunt
    else:
        print("el numero tiene que ser uno de los de la tabla de arriba")

def niveles(numpunt):
    cobrado = 2400 * numpunt
    if numpunt == 0.0:
        print(f"Tu nivel es inaceptable ,vas a recibir {cobrado}€")
    elif numpunt == 0.4:
        print(f"Tu nivel es aceptable, vas a recibir {cobrado}€")
    elif numpunt >= 0.6:
        print(f"Tu nivel es meritario, vas a recibir {cobrado}€")

def main():
    latabla()
    numpunt = puntuacion()
    niveles(numpunt)

if __name__ == "__main__":
    main()