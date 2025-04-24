numero_1 = int(input("Ingrea tu primer numero: "))
numero_2 = int(input("Ingresa tu segundo numero: "))
numero_3 = int(input("Ingresa tu tercer numero: "))

if numero_1 <= numero_2 and numero_1 <= numero_3:
    print(f"El numero menor es: {numero_1}")
elif numero_2 <= numero_3 and numero_2 <= numero_1:
    print(f"El numero menor es: {numero_2}")
elif numero_3 <= numero_1 and numero_3 <= numero_2:
    print(f"El numero menor es {numero_3}")