#Faça um programa que receba 5 valores e me mostre o somatório dos valores.

lista = []
for c in range(0, 5):
    lista.append(int(input("Digite um valor:")))

print(sum(lista))