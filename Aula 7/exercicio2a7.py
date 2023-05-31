'''a. Digite a condição de saída de primeira e mostre a mensagem:
    "Nenhum dado foi fornecido."

b. Quantas empresas foram processadas?

c. Mostre também o CNPJ e a quantidade de funcionários da menor empresa.
'''

quantidade = 0
print("Digite -1 para sair do loop")
print(f"Nenhum dado foi fornecido \n")

listafuncionarios = []
listacnpj = []
maiorcnpj = 0
maiorqtd_funcionarios = 0
indicemaior = 0
indicemenor = 0
menorcnpj = 0
menorqtd_funcionarios = 0
i = 0

while True:
    cnpj = int(input("Digite o CNPJ da empresa:"))
    if cnpj == -1: break
    listacnpj.append(cnpj)
    funcionarios = listafuncionarios.append(int(input("Digite a quantidade de funcionarios da empresa:")))
    quantidade+= 1
    if listafuncionarios:
        indicemaior = listafuncionarios.index(max(listafuncionarios))
        maiorcnpj = listacnpj[indicemaior]
        maiorqtd_funcionarios = listafuncionarios[indicemaior]
    if listafuncionarios:
        indicemenor = listafuncionarios.index(min(listafuncionarios))
        menorcnpj = listacnpj[indicemenor]
        menorqtd_funcionarios = listafuncionarios[indicemenor]

print(f"{quantidade} empresas foram processadas nesse loop!")
print(f"Maior empresa: CNPJ: {maiorcnpj},Quantidade de funcionarios:{maiorqtd_funcionarios}")
print(f"Menor empresa: CNPJ: {menorcnpj},Quantidade de funcionarios:{menorqtd_funcionarios}")