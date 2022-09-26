# 4- Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Informe a nota da sua primeira prova:  "))
nota2 = float(input("Informe a nota da sua segunda prova:  "))
nota3 = float(input("Informe a nota da sua terceira prova:  "))
nota4 = float(input("Informe a nota da sua quarta prova:  "))
SOMATORIA = nota1 + nota2 + nota3 + nota4
media_final = SOMATORIA / 4
print(f"Sua média é: {media_final}")