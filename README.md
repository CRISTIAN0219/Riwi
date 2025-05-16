# Semana 1
# Fundamentos
## Qué es programar?
La creacion de programas o aplicaciones a traves de lenguajes de programacion

## ¿Qué es Python y para qué sirve? 
Es un lenguaje de programacion de alto nivel, que es utilizado por programadores experimentados, tanto por los que empizan dado a que se le con facilidad el contenido de este

## ¿Qué es un programa y cómo se ejecuta?
Es un cojunto de instrucciones escritas en un lenguaje de programacion que se utiliza para realiazar una tarea esprecifica

## ¿Qué es una variable?
Es un espacio en el que se almacena un valor, y los cuales los valores de las variales se pueden cambiar a medida de la ejecuccion del programa

## Tipos de datos basicos
### Str:
Se utiliza para ingresar palabras o frases, se utiliza dentro de comillas simples o dobles segun la tarea
### Int:
Se usa para ingresa numeros enteros (Sin decimales)
### Float:
Este se agrega para ingresar numeros los cuales cuentan con decimales
### Bool:
Se usa para darle un valor a una respuesta que sea verdadera (True) o falsa (False)

## Operaciones basicas

1 Suma (+)

2 Resta (-)

3 Multiplicacion (*)

4 Division (/)

## Mostrar información en pantalla: print().
Este se utiliza cuando se quiere imprimir un texto o depurar.

## Pedir información al usuario: input().
Permite que el usuario ingrese datos, siempre devuelve una cadena de texto.

## Convertir tipos de datos:
    Int: numero = int("10")

    Float: decimal = float("3.14")

    Str: texto = str(123)

## Que es un error? Errores comunes en principiantes
-Error de sintaxis: Ocurren cuando se escribe el código de manera incorrecta (por ejemplo, olvidando un paréntesis) O  "unas comillas".

Errores de tipo: Cuando se intenta hacer una operación con tipos de datos incompatibles (por ejemplo, sumar un texto con un número).


# ¿Qué es una lista y para qué sirve?
Una lista es una colección ordenada de elementos que pueden ser de cualquier tipo: números, texto, otras listas, etc. 
# Crear listas: [ ]
Las listas se crean con corchetes y los elementos se separan con comas.

    numeros = [1, 2, 3, 4, 5]
    vacia = []

# Acceder a elementos de una lista (lista[0]).
Se puedes acceder a un elemento usando su índice. Los índices empiezan en 0.

    print(frutas[0])  # "manzana"
    print(frutas[1])  # "banana"

# Modificar elementos de una lista.
Puedes cambiar el valor de un elemento indicando su posición.

    frutas[1] = "pera"
    print(frutas)  # ["manzana", "pera", "naranja"]


# Agregar elementos a una lista: append()
Usamos append() para agregar un elemento al final de la lista.
# Eliminar elementos de una lista: remove() y pop().
remove(valor) elimina el primer elemento que coincida.

pop() elimina el último elemento (o uno por índice).

    frutas.remove("pera")
    print(frutas)  # ["manzana", "naranja", "uva"]

    frutas.pop()
    print(frutas)  # ["manzana", "naranja"]

# Conocer la cantidad de elementos: len().
La función len() devuelve el número de elementos en una lista.
# Recorrer listas con un for.
Puedes usar un for para recorrer todos los elementos:


# Logica de programacion
## Comparacion de datos
Se usan para comparar valores

==: Igual a

!=: No igual a

<: Menor que

>: Mayor que

<=: Menor o igual que

>=: Mayor o igual que

## Tomar decisiones
Usamos if, else y elif para ejecutar diferentes bloques de código dependientes de una condición.

    if numero > 100:

    print("numero es mayor que 100")
    
    elif numero == 100:

    print("numero es 100")
    
    else:

    print("numero es menor que 100")

## Combinar condiciones
Se usa para combinar condiciones

    if numero > 100 and (y) < 50:

    print("Las condiciones son verdaderas")
    
## Como escribir comentarios en codigo
Se esrciben con el numeral (#), generalmete este se añade al visual studio code para generar un comentario

## Qué es la indentación y por qué es tan importante en Python?
Identacion: Se refiere al uso de espacios o tabuladores para identar líneas de código y definir bloques de código. Es importante en python ya que: Define bloques de codigo, determina la estructura del codigo y evita errores de la sintaxis.

## Buenas prácticas al nombrar variables (nombres claros, sin espacios)
Es muy importante nombrar claramente una variable, para esto debo tener en cuenta:

-Usar nombres descriptivos y claros

-Usar nombres que describan el tipo de dato

-Evitar nombres ambiguos

## ¿Qué hacer cuando algo no funciona? 
Leer el mensaje: Python generalmete indica cual es el error y donde se encuentra

Bucar en linea: Usa google o foros como StackOverflow para encontrar soluciones

No fustrarse: El programar es un proceso de errores y intentos en el cual se debe tener paciencia en los intentos fallidos, ya que la practica ayuda a mejorar


# Qué es un bucle anidado.
Un bucle anidado es un bucle dentro de otro bucle. Se usa cuando necesitas recorrer estructuras más complejas, como listas de listas (por ejemplo, una matriz).
# Cómo funcionan los índices y rangos en listas (range()).
Los índices comienzan en 0. Cada elemento de una lista tiene una posición:
# Introducción a las funciones: ¿qué es una función y por qué usarlas?
Una función es un bloque de código que se puede usar varias veces. Sirve para organizar mejor tu programa, evitar repetir código y hacerlo más legible.

Piensa en una función como una "máquina" a la que le das algo y te devuelve algo (o hace una acción).
# Definir funciones con def.
Se usa la palabra clave def para crear una función:

    def saludar():
    print("Hola, mundo!")

# Llamar (usar) funciones.
Para usar una función que ya definiste, solo tienes que escribir su nombre con paréntesis:
# Parámetros y argumentos en funciones. 
#### Parámetros
Son variables que usas dentro de la función. Se escriben entre paréntesis al definirla.

#### Argumentos

Son los valores reales que le pasas cuando llamas a la función.
# Qué es el retorno de una función: return.
Una función puede devolver un valor usando return. Esto te permite guardar el resultado y usarlo más adelante.


# Estructura de control
## Repetir acciones con bucles
For: Se usa cuando se sabe cuántas veces se quiere repetir algo.

While: Se usa cuando se quiere repetir algo mientras se cumpla una condicion.

## Salir de un bucle antes de tiempo
break: Sale del bucle.

Continue: Salta a la siguiente iteración del bucle.

## Manejo básico de errores 
Usamos try-except para manejar errores sin detener el programa.










    




















































