# Faça uma função que receba uma variável e mostre na tela se ele for múltiplo de 2

def multiplo(a):
    if a % 2 == 0:
        print(f"O numero {a} é multiplo de 2.")
    else:
        print(f"O numero {a} é não multiplo de 2.")


if __name__ == '__main__':
    a = int(input("Digite um numero:"))
    multiplo(a)
