hora = int(input("Digite o horáio de agora:"))

if  0 <= hora < 6:
   horario = print(f"Agora são {hora} horas, vai dormir!")
elif  6 <= hora <12:
   horario = print(f"Agora são {hora} horas, bom dia flor do dia!")
elif  12<= hora <18:
    horario = print(f"Agora são {hora} horas, flor da tarde!")
elif  18<= hora <24:
    horario = print(f"Agora são {hora} horas, boa noite!")
else:
    print("Horário informado inválido!")