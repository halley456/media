geral = []
while True:
    print('-' * 30)
    nome = str(input('NOME: '))
    print('-' * 30)
    nota1 = float(input('Primeira nota: '))
    print('-' * 30)
    nota2 = float(input('Segunda nota: '))
    print('-' * 30)
    media = (nota1 + nota2) / 2
    geral.append([nome, [nota1, nota2], media])
    res = str(input('Quer continuar? [S/N] '))
    print('-' * 30)
    if res in 'Nn':
        break

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(geral):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' * 30)

while True:
    bus = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print('-' * 30)
    if bus == 999:
        print('FINALIZANDO...')
        print('-' * 30)
        break
    if 0 <= bus < len(geral):
        print(f'Notas de {geral[bus][0]}: {geral[bus][1]}')
        print('-' * 30)

print('<<< VOLTE SEMPRE >>>')
