palavra = input("Digite uma palavra de até 10 caracteres: ")
vogais = "aeiouAEIOU"
cont = 0
for letra in palavra:
    if letra in vogais:
        cont += 1
print("A palavra", palavra, "tem", cont, "vogais.")