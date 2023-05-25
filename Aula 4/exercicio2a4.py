#Escreva um algoritmo que solicita ao usuário N números inteiros, calcule e imprima na tela do computador a média(duas casas decimais) do aluno.
quantidade = int(input("Digite um número:"))
soma = 0
for c in range(0, quantidade):
    nota = float(input("Digite uma nota:"))
    soma += nota
    media = soma / quantidade


print(f"A media das notas digitadas é:{media:.2f}",)