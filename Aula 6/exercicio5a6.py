''' O professor aplicou a avaliação em sua turma e deseja selecionar a maior nota e
sua respectiva frequência, ou seja, a quantidade de alunos que conseguiu a maior
nota. Desenvolva o programa que leia a nota dos alunos e gere a tela de saída com
as informações solicitadas.


Entrada 1: Nota: 6.5, 8.5, 4.0, -1           		Saída 1: Maior nota: 8.5, Qtd.: 1
Entrada 2: Nota: 8.5, 6.5, 8.5, -1           	    Saída 2: Maior nota: 8.5, Qtd.: 2
Entrada 3: Nota: 8.5, 6.5, 8.5, 9.0, -1    		    Saída 3: Maior nota: 9.0, Qtd.: 1
'''

i = 0
quantidade = 0
maior = 0
menor = 0
while i != -1:
    i = int(input("Digite sua nota:"))
    if i == -1:
        break
    if i > maior:
        maior = i
        quantidade+= 1
    if i < menor:
        menor = i
        quantidade += 1
print(f"A maior nota foi {maior} e {quantidade} pessoas tiraram essa nota!")
print(f"A menor nota foi {menor} e {quantidade} pessoas tiraram essa nota!")