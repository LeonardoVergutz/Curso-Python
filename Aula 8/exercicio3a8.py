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


def sequencia (quantidade):
    fibo = [0,1]

    for c in range(2,quantidade):
        fibo.append(fibo[c-1]+fibo[c-2])

    return fibo

quantidade = int(input("Digite a quantidade de termos a serem utilizados na Fibonacci:"))
final = sequencia(quantidade)
print(f"A sequencia de Fibonacci disponivel com o termo informado é:{final}")