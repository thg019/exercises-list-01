# Maior de dois:
# Faça um programa que pede 2 números inteiros
# para o usuário e mostra na tela qual o maior dos
# dois ou se ele são iguais

num1 = int(input("Digite aqui o primeiro número: "))
num2 = int(input("Digite aqui o segundo número: "))

if num1 > num2:
    print(f"O {num1} é maior.")
elif num2 > num1:
    print(f"O {num2} é maior.")
else:
    print("Os números são iguais.")

# -------------------------------------------#
# Positivo ou negativo:
# Faça um programa que pede para o usuário digitar
# um número inteiro e mostra na tela se o número
# digitado é positivo, negativo ou neutro

numero = int(input("Digite aqui um número: "))   

if numero == 0:
    print("O número é neutro.")
elif numero > 0:
    print("É positivo.")
else:
    print("É negativo.")

# -------------------------------------------#
# Par ou Ímpar
# Faça um programa que pede um número inteiro e
# positivo para o usuário e mostre na tela se aquele
# número é par ou ímpar.

numero = int(input("Digite aqui um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O númerp é ímpar.")

# -------------------------------------------#
# # Vogal ou Consoante:
# # Faça um programa que pede para o usuário
# # escrever uma letra qualquer e mostre na tela se ele
# # digitou uma vogal ou uma consoante ou outro
# # caracter.

letra = str(input("Digite aqui uma letra: ")).lower().strip()

if letra in 'aeiou':
    print("É uma vogal.")
elif letra in 'bcdfghjklmnpqrstvwxyz':
    print("É uma consoante.")
else:
    print("É um caracter fora do alfabeto.")

# -------------------------------------------#
# Masculino ou Feminino:
# Faça um programa que pede para o usuário digitar
# uma letra (M ou F) e mostra uma mensagem
# respectiva M - Masculino, F - Feminino ou Sexo
# inválido.

letra = str(input("Digite aqui uma letra (M ou F): ")).lower().strip()

if letra in 'm':
    print("Masculino.")
elif letra in 'f':
    print("Feminino.")
else:
    print("Sexo inválido.")


