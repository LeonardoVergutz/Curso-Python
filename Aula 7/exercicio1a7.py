'''Uma agência de publicidade quer prestar seus serviços somente para a maior companhia, considerando a quantidade de funcionários.
Para tal, conseguimos um conjunto de dados com o CNPJ (Cadastro Nacional de Pessoa Jurídica) e a quantidade de funcionários de várias empresas.
Construa o programa que leia esses dados de entrada e mostre o CNPJ e a quantidade de funcionários da maior empresa, ou seja, da empresa com maior recursos humanos.

Teste 1: Entrada: 111, 15;  110, 20;                Saída: Maior empresa: 110, qtd 20
Teste 2: Entrada: 111, 15;  112, 20;  113, 10;  Saída: Maior empresa: 112, qtd 20'''

listafuncionarios = []
listacnpj = []
maior = 0
menor = 0
i = 0

while True:
    cnpj = listacnpj.append(int(input("Digite o CNPJ da empresa:")))
    if cnpj == -1:
        break
        False

    funcionarios = listafuncionarios.append(int(input("Digite a quantidade de funcionarios da empresa:")))
    if listafuncionarios:
        indicemaior = listafuncionarios.index(max(listafuncionarios))
        maiorcnpj = listacnpj[indicemaior]
        maiorqtd_funcionarios = listafuncionarios[indicemaior]
print(f"Maior empresa: CNPJ: {maiorcnpj},Quantidade de funcionarios:{maiorqtd_funcionarios}")
