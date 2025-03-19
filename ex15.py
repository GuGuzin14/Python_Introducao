n = int(input("Digite o valor de n (inteiro positivo): "))


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


resultado = fibonacci(n)
print(f"O {n}-ésimo termo da sequência de Fibonacci é: {resultado}")
