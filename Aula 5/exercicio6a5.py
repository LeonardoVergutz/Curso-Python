#Faça um programa que vai ler 5 números e colocar em uma lista. Após isso, esse programa vai reorganizar a lista na ordem numérica.

lista = []

for c in range(0,5):

 lista.append(int(input("Digite um valor:")))
 lista.sort()
print(lista)