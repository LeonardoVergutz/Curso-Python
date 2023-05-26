#Faça um programa que receba 5 valores e faça a soma do primeiro e do terceiro valor, no final mostre o resultado na tela.

lista = []

for c in range(0,5):
    x=(int(input("Digite um valor:")))
    lista.append(x)
print(lista[0]+lista[2])
