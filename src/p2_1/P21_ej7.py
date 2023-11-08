def tipo_impositivo(renta):
    if renta < 10000:
        tipo_renta = "Tu renta es del 5%"
    elif renta > 10000 and renta < 20000:
        tipo_renta = "tu renta es del 15%"
    elif renta > 20000 and renta < 35000:
        tipo_renta = "tu renta es del 20%"
    elif renta > 35000 and renta < 60000:
        tipo_renta = "tu renta es del 30%"
    elif renta > 60000:
        tipo_renta = "tu renta es del 45%"
    return tipo_renta

def main():
    try:
        renta = int(input("Dime tu renta anual: "))
        print(tipo_impositivo(renta))
    except ValueError:
        print("No tienes que poner € al final , tiene que ser un numero positivo y no pueden ser letras")




if __name__ == "__main__":
    main()
