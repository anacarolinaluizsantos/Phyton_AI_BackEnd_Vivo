curso = "pYtHon"

print(curso.upper())
print(curso.lower())
print(curso.title())

texto =  "  Olá mundo !!!"
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(20,'#'))
print("P-y-t-h-o-n")
print("-".join(menu))

for letra in menu:
    print(letra, end="-")
print()
