#Escrever um programa que solicita ao usuário um conjunto de 10 valores reais e mostrar a média dos 10 números .(usando só o FOR)(dois casa decimal)
print("Vamos inserir dez numeros!")
soma = 0
for c in range(0,10):
    numero = float(input("Digite um número:"))
    soma += numero
    media = soma / 10
print(f"A media dos numeros informados é:{media:.2f}")