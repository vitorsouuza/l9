frase = input("Digite uma frase: ")
nova_frase = ""
for letra in frase:
    codigo_ascii = ord(letra)
    if codigo_ascii >= 65 and codigo_ascii <= 90:
        novo_codigo_ascii = codigo_ascii - 32
        nova_letra = chr(novo_codigo_ascii)
    else:
        nova_letra = letra
    nova_frase += nova_letra
print(nova_frase)