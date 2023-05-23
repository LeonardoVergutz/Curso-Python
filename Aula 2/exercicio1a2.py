#Crie um programa que receba três notas de 0 até 10 (faça as validações para aceitar apenas esse intervalo), depois faça o cálculo da média aritmética e então mostre a média calculada e também se o aluno passou ou não.
#A escola aceita notas 7 (sete) acima para aprovação.

nota1 = int(input("Digite a sua primeira nota:"))
nota2 = int(input("Digite a sua segundo nota:"))
nota3 = int(input("Digite a sua terceira nota:"))

media = int((nota1 + nota2 + nota3)/ 3)

if 0< nota1 <= 10 and 0< nota2 <= 10 and 0< nota3 <= 10:
    if media >= 7:
        print(f"Sua nota final foi: {media}.  Voce foi aprovado!")
    else:
        print(f"Sua nota final foi: {media}. Voce foi reprovado!")
else:
    print("Alguma nota digitada é invalida!")