nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435
dados = {"nome": "Guilherme","idade":28}


print("Nome: {} Idade: {}".format(nome,idade))

print("Nome: {0} Idade: {1}".format(nome,idade))

print("Nome: {0} Idade: {1} Nome:{1}{1}".format(nome,idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome,idade=idade))

print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))

print ("Nome:{nome}Idade:{idade}".format(**dados))

print(f"Nome:{nome} Idade:{idade}")

print(f"Nome:{nome} Idade:{idade} Saldo: {saldo:.2f}")