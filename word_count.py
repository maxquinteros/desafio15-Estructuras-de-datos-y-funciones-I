stream = open("lorem_ipsum.txt", "r")

texto = stream.read()

caract_dist = len(set(texto))
palabras_dist = len(set(texto.split(" ")))
print(f"El número de caracteres distintos es: {caract_dist}")
print(f"El número de palabras distintas es: {palabras_dist}")

stream.close()