#Faça um programa que receba N valores e após isso calcule a média desses valores. (Usando while)
#obs: não use o break

i = 0
soma = 0
repe = 0
quantidade = int(input("Quantos numeros vc deseja informar?"))

while i < quantidade:
    i = int(input("Digite um número:"))
    soma += i
    repe += 1
print(f"A media dos valores é:{soma/repe}")
