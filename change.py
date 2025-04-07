def change():
    expense = 23.75
    money = 100
    vuelto = str(money - expense)
    position = vuelto.find(".")
    pesos = vuelto[:position]
    centavos = vuelto[position + 1:]
    print(f"Ingresar gasto:")
    print(f"{expense}")
    print(" ")
    print(f"Dinero resibido:")
    print(f"{money}")
    print(" ")
    print(f"Vuelto:")
    print(" ")
    print(f"Pesos:")
    print(f"{pesos}")
    print(" ")
    print(f"Centavos:")
    print(f"{centavos}")
change()
