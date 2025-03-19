
preco_produto = float(input("Digite o preço do produto: R$ "))

if preco_produto < 250.00:
    imposto = 0.15
else:
    imposto = 0.25


novo_preco = preco_produto * (1 + imposto)

print(f"O novo preço do produto com o imposto aplicado é: R$ {novo_preco:.2f}")