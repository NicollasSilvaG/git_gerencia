def bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

while True:
    ano = input("Digite um ano (ou 'sair' para encerrar): ")
    if ano.lower() == "sair":
        break
    elif ano.isdigit():
        if bissexto(int(ano)):
            print(f"{ano} é um ano bissexto.")
        else:
            print(f"{ano} não é um ano bissexto.")
    else:
        print("Entrada inválida. Digite um ano válido ou 'sair'.")
