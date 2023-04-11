nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ")
idade = int(input("Digite a idade: "))
if sexo.upper() == "F" and idade < 25:
    print(nome, "ACEITA")
else:
    print("NÃO ACEITA")