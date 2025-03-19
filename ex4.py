valor = int(input("Qual valor do premio? "))
primeiro = str(input("Nome do Ganhador: "))
segundo = str(input("Nome do 2° lugar: "))
terceiro = str(input("Nome do 3° lugar: "))

premioPrimeiro = (valor * 47) / 100
premioSegundo = (valor * 34) / 100
premioTerceiro = (valor * 19) / 100

print("Premio do : "+ str(primeiro) + " é " + str(premioPrimeiro))
print("Premio do : "+str(segundo) + " é " + str(premioSegundo))
print("Premio do :"+str(terceiro) + " é " + str(premioTerceiro))