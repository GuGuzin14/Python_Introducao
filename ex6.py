codigo = int(input("Digite o código do produto: "))

if(codigo == 1):
    print("Produto: Alimento Não-perecível")
elif(codigo == 2 or codigo == 3):
    print("Produto: Alimento Perecivel")
elif(codigo == 4 or codigo == 5 or codigo == 6):
    print("Produto: Vestuário")
elif(codigo == 7 or codigo == 8 or codigo == 9):
    print("Produto: Limpeza")
elif(codigo == 10):
    print("Produto: Utensilios domesticos")
elif(codigo == 11 or codigo == 12):
    print("Produto: Eletronicos")
else:
    print("Código invalido")


