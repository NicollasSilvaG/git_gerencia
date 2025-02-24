def bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

ano = int(input("Digite um ano: "))
if bissexto(ano):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
