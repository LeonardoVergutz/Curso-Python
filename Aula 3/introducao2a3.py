#Crie uma função para mostrar o valor recebido.
# A função main (principal) chama a função três vezes, passa um valor inteiro, um valor float e depois um negativo.
import random
def valor(numero):
    print("Valor recebido:", numero)

if __name__ == '__main__':


    x = random.randint(1,100)
    y = random.randint(1,100)
    z = random.randint(-100, -1)
    w = float(y)


    valor(x)
    valor(w)
    valor(z)
