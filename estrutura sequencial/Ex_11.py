 #Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 # A -o produto do dobro do primeiro com metade do segundo.
 # B -a soma do triplo do primeiro com o terceiro.
 # C -o terceiro elevado ao cubo.


numero1 = int(input("Informe um número inteiro: "))
numero2 = int(input("Informe outro número inteiro: "))
numero3 = float(input("Informe um número real: "))

conta_a = ((numero1 * 2) * (numero2 / 2))
conta_b = (numero1 * 3) + numero3
conta_c = (numero3 ** 3)

print(f"o produto do dobro de {numero1} com metade de {numero2} é: {conta_a}")
print()
print(f"a soma do triplo de {numero1} com o {numero3} é: {conta_b} ")
print()
print(f"o {numero3} elevado ao cubo é: {conta_c}")
print()