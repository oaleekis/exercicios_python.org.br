# 9- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

temperatura_fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))

temperatura_Celsius = (temperatura_fahrenheit - 32) * (5/9)

print(f"á temperatura {temperatura_fahrenheit}F° em Celsius é: {temperatura_Celsius:.2f}C°")