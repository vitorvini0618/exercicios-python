numeros = [2, 12, 6, 55, 3, 25]
for n in numeros:
    if n % 2 != 0:
        continue
    print(f"O numero {n} é par")

dados = {"nome": "Vitor", "idade": 18, "Genero": "masculino"}

for c, v in dados.items():
    print(f"{c}: {v}")

#c = chave, v = valor    