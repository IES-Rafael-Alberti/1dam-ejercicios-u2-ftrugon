def serienum():
    num = int(input("dame los numeros, 0 si no quieres cadena: "))
    linea = f"{num}"
    sumanum2 = num
    while num != 0:
        num = int(input("Dame otro numero, 0 si quieres que acabe: "))
        linea = linea + f" + {num}"
        sumanum2 = sumanum2 + num
    serie = f"Serie => {linea} = {sumanum2}"
    print(serie)
    return serie

def main():
    serienum()
    
if __name__ == "__main__":
    main()