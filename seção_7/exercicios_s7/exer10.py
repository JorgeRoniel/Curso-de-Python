lista_medias = []

for i in range(1, 16):
    nota = float(input('Insira sua nota: '))
    lista_medias.append(nota)

media = sum(lista_medias) / 15

print(f'A media geral da turma foi {media:.2f}')