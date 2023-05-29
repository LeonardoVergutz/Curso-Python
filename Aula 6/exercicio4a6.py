#Repita o exercício 1, so que dessa vez você deve utilizar o break (Usando while)

i =0
soma = 0
quantidade = 0

while i != -1:

    i = int(input("Digite um número:"))
    if i == -1:
        break
    soma += i
    quantidade +=1

print(f"A media dos valores é:{soma/quantidade}")