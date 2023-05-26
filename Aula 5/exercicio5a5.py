#Faça um programa que receba 5 valores e coloque-os em uma lista. Após isso calcule a média dessa lista

lista = []

for c in range(0,5):
    lista.append(int(input("Digite um valor:")))
print(sum(lista)/len(lista))
