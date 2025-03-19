
n = int(input("Digite um número inteiro positivo (maior ou igual a 10): "))

n_str = str(n)

if n_str == n_str[::-1]:
    print(f"{n} é um número palíndromo.")
else:
    print(f"{n} não é um número palíndromo.")