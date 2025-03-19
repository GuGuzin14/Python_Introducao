
media_final = float(input("Digite a média final do aluno: "))
numero_faltas = int(input("Digite o número de faltas do aluno: "))

if media_final >= 9.0:
    conceito = 'A' if numero_faltas <= 14 else 'B'
elif 7.5 <= media_final < 9.0:
    conceito = 'B' if numero_faltas <= 14 else 'C'
elif 6.0 <= media_final < 7.5:
    conceito = 'C' if numero_faltas <= 14 else 'D'
elif 4.0 <= media_final < 6.0:
    conceito = 'D' if numero_faltas <= 14 else 'E'
else:
    conceito = 'E'

print(f"O conceito final do aluno é: {conceito}")