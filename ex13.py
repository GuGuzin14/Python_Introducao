
p = int(input("Digite um número inteiro positivo: "))


if p < 2:
    primo = False
else:
    primo = True
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            primo = False
            break


if primo:
    print(f"{p} é um número primo.")
else:
    print(f"{p} não é um número primo.")