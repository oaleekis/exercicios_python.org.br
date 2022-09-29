# 10- Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperatura_celsius = float(input("Insira a temperatura em Celsius: "))

temperatura_fahrenheit = (temperatura_celsius * (9/5)) + 32

print(f"á temperatura {temperatura_celsius}C° em Fahrenheit é: {temperatura_fahrenheit:.2f}C°")