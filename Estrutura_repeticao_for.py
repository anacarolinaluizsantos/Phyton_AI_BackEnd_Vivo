texto = ""
VOGAIS = "AEIOU"

for letra in VOGAIS:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()

for numero in range(0, 51, 5):
    print(numero, end=" ")
