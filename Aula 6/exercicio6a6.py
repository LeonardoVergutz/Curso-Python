#Faça um código em Python que leia o nome do aluno, leia uma quantidade indefinida de notas digitadas pelo professor e, ao final,
# faça o cálculo da média e imprima o nome do aluno e sua média correspondente.
nome = input("Digite o nome do aluno:")
notas = 0
soma = 0
quantidade = 0
media = 0
while notas != -1:
    notas = int(input("Digite a nota do aluno:"))
    if notas == -1:
        break
    soma += notas
    quantidade += 1
media = soma / quantidade
print(f"O aluno {nome} ficou com uma media final de: {media} ")
