peso = float(input("ingresa tu peso en KG:  "))
altura = float(input("ingresa tu altura M.  "))

imc = peso / (altura**2)

if imc <= 18.5:
    print("bajo peso")
elif imc <=24.9:
    print("normal")
elif imc <=29.9:
    print("Sobrepeso")
elif imc >=30:
    print("Obesidad")


    







