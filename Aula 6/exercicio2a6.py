''' Achar o maior e o menor número de uma série de números inteiros positivos fornecidos pelo usuário via teclado.
O programa deve solicitar valores até que o usuário entre com -1. (Usando while e condicionais)'''

i = 0
maior = 0
menor = 0
while i != -1:
    if i == -1:
        break

    print("Digite (-1) para sair!")
    i = int(input("Digite um valor:"))
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f"O maior numero informado é:{maior}")
print(f"O menor numero informado é:{menor}")


