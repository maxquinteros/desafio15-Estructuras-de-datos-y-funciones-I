import sys

tasa_peru = float(sys.argv[1])
tasa_argentino = float(sys.argv[2])
tasa_americano = float(sys.argv[3])
valor_a_convertir = float(sys.argv[4])

valor_convertido_peru = tasa_peru * valor_a_convertir
valor_convertido_argentino = tasa_argentino * valor_a_convertir
valor_convertido_americano = tasa_americano * valor_a_convertir

print(f"Los {valor_a_convertir} pesos equivalen a:")
print(f"{valor_convertido_peru} Soles")
print(f"{valor_convertido_argentino} Argentinos")
print(f"{valor_convertido_americano} Dólares")