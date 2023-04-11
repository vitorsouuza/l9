frase = input("Digite uma frase: ")
quantidade_brancos = 0
for letra in frase:
    if letra == " ":
        quantidade_brancos += 1
print(f"A frase digitada possui {quantidade_brancos} caracteres em branco.")