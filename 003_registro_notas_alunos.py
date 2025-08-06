notas = []

for x in range(5):
    codigo_do_aluno  = input('Qual a rm: ')
    nota = float(input('Nota do aluno: '))
    resultado = [codigo_do_aluno, nota]
    notas.append(resultado)

print('Quantidade de notas', len(notas))

for n in notas:
    codigo_do_aluno = n[0]
    nota = n[1]
    print(f"O RM {codigo_do_aluno} tirou a nota {nota}")

       
