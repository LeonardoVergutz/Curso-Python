#Faça uma calculadora que receba números inteiros e posteriormente a operação a ser feita com esse número e então retorne o resultado.

def calculator(a,b,operacao):
    if operacao == "Soma":
        print("A soma dos numeros informados é:", a+b)
    elif operacao == "Subtração":
        print("A subtração dos numeros informados é:", a-b)
    elif operacao == "Multiplicação":
        print("A multiplicação dos números informados é:", a*b)
    elif operacao == "Divisão":
        print("A divisão dos numeros informados é:", a/b)
    else:
        print("Operação digitada incorretamente")

if __name__ == '__main__':
    a = int(input("Digite o primeiro numero:"))
    b = int(input("Digite o segundo numero:"))
    print("Operações disponiveis: Soma, Subtração, Multiplicação e Divisão (favor escrever igual ao informado)")
    operacao = str(input("Digite a operação a ser realizada:"))
    calculator(a,b,operacao)