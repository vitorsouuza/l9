frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
frase_sem_vogais = ""
for letra in frase:
    if letra not in vogais:
        frase_sem_vogais += letra
print(frase_sem_vogais)