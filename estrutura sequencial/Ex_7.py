# 7- Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

largura = float(input("Informe a largura do quadrado: "))
comprimento = float(input("Informe o comprimento do quadrado: "))

area = largura * comprimento
dobro_area = area * 2
print(f"O dobro da area é: {dobro_area}")