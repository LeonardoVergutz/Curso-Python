'''Crie uma variação do programa anterior, porém com os seguintes requisitos adicionais:
Calcule uma média ponderada: Peso da Nota 1 é 1, Peso da Nota 2 é 1.5 e Peso da Nota 3 é 2.
Ao invés de mostrar se o aluno foi aprovado ou não com base na média ponderada mostre uma menção de SR, II, MI, MM, MS ou SS, conforme a média ponderada e usando a escala:

SR - 0
II - < 2
MI - < 5
MM - < 7
MS - < 9
SS - >=9
'''

nota1 = int(input("Digite a sua primeira nota:"))
nota2 = int(input("Digite a sua segundo nota:"))
nota3 = int(input("Digite a sua terceira nota:"))

soma = (nota1 + (nota2 * 1.5) + (nota3 *2))
media = int(soma/ 4.5)

if 0< nota1 <= 10 and 0< nota2 <= 10 and 0< nota3 <= 10:
     if media == 0:
         print(f"A sua media final foi:{media}, e sua menção é SR")
     elif media < 2:
         print(f"A sua media final foi:{media}, e sua menção é II")
     elif media <5:
         print(f"A sua media final foi:{media}, e sua menção é MI")
     elif media <7:
         print(f"A sua media final foi:{media}, e sua menção é MM")
     elif media <9:
         print(f"A sua media final foi:{media}, e sua menção é MS")
     elif media >=9:
         print(f"A sua media final foi:{media}, e sua menção é SS")
else:
    print("Alguma nota digitada é invalida!")