'''Faça o código necessário para calcular a sequencia de
Fibonacci usando for e depois faça o mesmo usando função

Exemplo de Saída:
Quantos termos? 7
Sequência de Fibonacci:
0
1
1
2
3
5
8
'''

quantidade = int(input("Digite um numero:"))
sequencia = [0,1]

for c in range(2,quantidade):
    sequencia.append(sequencia[c-1]+sequencia[c-2])
print(f"A sequencia de fibonacci até a quantidade do termo inserido é:{sequencia}")