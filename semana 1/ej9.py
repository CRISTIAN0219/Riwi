año = int(input("Ingresa un año:  "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(" Es un año biciesto")
else:
    print("No es un año biciesto")