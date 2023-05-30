'''Desenvolva o programa que leia vários(N) números e mostre estas informações:
A) Quantidade de elementos dados ;
B) Soma dos valores ;
C) media dos valores ;
D) porcentagem de números pares ate dois casas decimais
(( Pode usar o comando While ou For ))'''

i = 0
soma = 0
quantidade = 0
pares = 0
porcentagem = 0
while i != -1:
    i = int(input("Digite um número:"))
    if i == -1:
        break
    soma += i
    quantidade += 1

    if i % 2== 0:
        pares += 1

porcentagem = (pares/quantidade) * 100
media = soma / quantidade

print("\n")
print(f"A quantidade de elementos inseridos é:{quantidade}")
print(f"A soma dos valores é:{soma}")
print(f"A media dos valores é:{media:.2f}")
print(f"A porcentagem dos valores é:{porcentagem:.2f}%")
