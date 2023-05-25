# Faça um programa que receba N números inteiros, e todos os números menores ou igual a 0 passem a ser 1 .

quantidade = int(input("Digite um numero:"))

for c in range(0, quantidade):
    numero = int(input("Digite um numero:"))

    if numero < 0:
        numero = 1
    print(numero)
