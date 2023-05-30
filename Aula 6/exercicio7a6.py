#Desenvolva um programa que recebe N números inteiros e retorna o maior deles. Se os números forem iguais, retorne um deles.(usando while )
i = 0
maior = 0
menor = 0
while i != -1:

    print("Digite (-1) para sair!")
    i = int(input("Digite um valor:"))
    if i == -1:
        break
    if i > maior:
        maior = i
    if i < menor:
        menor = i

if menor == menor:
    print(maior)
else:
    print(f"O maior numero informado é:{maior}")
    print(f"O menor numero informado é:{menor}")
