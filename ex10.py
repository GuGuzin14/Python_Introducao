
peso = float(input("Digite o peso da pessoa (kg): "))
altura = float(input("Digite a altura da pessoa (m): "))


imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso esperado"
elif 25 <= imc < 30:
    classificacao = "Acima do peso"
else:
    classificacao = "Muito acima do peso"

print(f"O IMC é: {imc:.2f}")
print(f"A classificação é: {classificacao}")