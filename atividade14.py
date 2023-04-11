palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
quantidade_vogais = 0
for letra in palavra:
    if letra in vogais:
        quantidade_vogais += 1
caractere_substituto = input("Digite um caractere (vogal ou consoante): ")
nova_palavra = ""
for letra in palavra:
    if letra in vogais:
        nova_palavra += caractere_substituto
    else:
        nova_palavra += letra
print(f"A palavra {palavra} possui {quantidade_vogais} vogais.")
print(f"A nova palavra é: {nova_palavra}")