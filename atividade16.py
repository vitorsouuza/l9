palavra = input("Digite uma palavra: ")
nova_palavra = ""
for letra in palavra:
    novo_codigo_ascii = ord(letra) + 1
    nova_letra = chr(novo_codigo_ascii)
    nova_palavra += nova_letra
print(nova_palavra)