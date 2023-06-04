'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

A) Faça uma tabuada usando FOR dentro de um WHILE.
B) Faça um código, usando for , que mostre todas as tabuadas(1 até 10).'''

num = int(input("Digite um número:"))

print(f"A tabuada de {num} é:\n")
for c in range(0, 11):
   tabuada = c * num
   print(f"{num}*{c}={tabuada}")