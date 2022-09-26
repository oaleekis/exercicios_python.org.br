# 8- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = float(input("Informe quantas horas você trabalhou esse mês: "))
salario = salario_hora * horas_trabalhadas

print(f"Seu salário esse mês, será de: R$ {salario}")