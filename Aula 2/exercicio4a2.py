#Crie um programa que receba duas notas e informe se a pessoa passou ou não.
# Considere que o usuário irá informar uma nota de 0 à 10 e que média a partir de 5 leva o aluno a aprovação

nota1 = int(input("Digite a primeira nota:"))
nota2 =int(input("Digite a segunda nota:"))

media = int((nota2 + nota1)/2)

if  0 <= nota2 < 10 and 0 <= nota1 < 10:
    if media >= 5:
        print(f"Sua nota final foi: {media}. Voce foi aprovado!")
    else:
         print(f"Sua nota final foi: {media}.Voce foi reprovado!")
else:
    print("Nota invalida digitada!")