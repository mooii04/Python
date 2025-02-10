numeros_div7 = [num for num in range(1, 1001) if num % 7 == 0]

digito_3 = [num for num in range(1, 1001) if '3' in str(num)]

cadena = "Hola mundo, esto es un ejercicio de Python."
espacios = cadena.count(' ')

discurso = "A los yaks amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos"
consonantes = [c for c in discurso if c.lower() in "bcdfghjklmnpqrstvwxyz"]

elementos = ["hi", 4, 8.99, 'apple', ('t,b','n')]
indices_valores = [(i, v) for i, v in enumerate(elementos)]

lista_a = [1, 2, 3, 4]
lista_b = [2, 3, 4, 5]
numeros_comunes = [num for num in lista_a if num in lista_b]

oracion = "En 1984 hubo 13 casos de protesta con más de 1000 asistentes"
numeros_en_oracion = [int(palabra) for palabra in oracion.split() if palabra.isdigit()]

numbers = range(20)
pares_impares = ["par" if num % 2 == 0 else "impar" for num in numbers]

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]
tuplas_coincidentes = [(num, num) for num in list_a if num in list_b]

cadena_palabras = "El sol brilla y la luna también"
palabras_cortas = [palabra for palabra in cadena_palabras.split() if len(palabra) < 4]

numeros_divisibles = [num for num in range(1, 1001) if any(num % d == 0 for d in range(2, 10))]

print("Ejercicio 1:", numeros_div7)
print("")
print("Ejercicio 2:", digito_3)
print("")
print("Ejercicio 3:", espacios)
print("")
print("Ejercicio 4:", consonantes)
print("")
print("Ejercicio 5:", indices_valores)
print("")
print("Ejercicio 6:", numeros_comunes)
print("")
print("Ejercicio 7:", numeros_en_oracion)
print("")
print("Ejercicio 8:", pares_impares)
print("")
print("Ejercicio 9:", tuplas_coincidentes)
print("")
print("Ejercicio 10:", palabras_cortas)
print("")
print("Ejercicio 11:", numeros_divisibles)
