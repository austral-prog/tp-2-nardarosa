def change():
    expense = 23.75
    money = 100
    vuelto = str(money - expense)
    position = vuelto.find(".")
    pesos = vuelto[:position]
    centavos = vuelto[position + 1:]
    print("Ingresar gasto:")
    print(f"{expense}")
    print("Dinero recibido")
    print(f"{money}")
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(f"{pesos}")
    print("")
    print("Centavos:")
    print(f"{centavos}")
change()
