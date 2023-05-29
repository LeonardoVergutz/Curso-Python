# Escreva um algoritmo que solicita ao usuário N notas, calcula e imprime na tela do computador a média do aluno.
# O programa deve continuar solicitando notas até que o usuário entre com -1. (Usando while)
i = 0
soma = 0
quantidade = 0
while i != -1:


    print("Digite (-1) para sair")
    i = int(input("Digite uma nota:"))
    if i == -1:
        break
    soma = soma + i
    quantidade += 1

media = soma / quantidade

print(f"A media final é:{media}")
