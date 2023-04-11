vetA = list("COMPUTACAO")
vetB = input("Digite uma palavra de 10 letras: ")
for i in range(len(vetA)):
    if vetA[i].lower() == vetB[i].lower():
        print("A letra", vetB[i], "na posição", i, "é igual à letra de COMPUTACAO.")