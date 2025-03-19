a = int(input("Digite o valor de a (inteiro positivo): "))
b = int(input("Digite o valor de b (inteiro positivo): "))


def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(f"Números primos entre {a} e {b}:")
for num in range(a, b + 1):
    if eh_primo(num):
        print(num)